import models ,schemas,crud
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends,HTTPException,status
from db import SessionLocal,engine
from auth import hash_password
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from auth import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,authenticate_user
from datetime import timedelta
import os,uvicorn


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # fallback to 8000 for local dev
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

#dependency
def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()

@app.get("/")
def welcome():
    return {"message":"welcome"}

# Login endpoint
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}




# Create user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    hashed_pw = hash_password(user.password)
    return crud.create_user(db=db, user=user, hashed_pw=hashed_pw)

# Read user by ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/books/",response_model=schemas.BookOut)
def create_book(book : schemas.BookCreate,db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.get("/books/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted"}

@app.patch("/books/{book_id}", response_model=schemas.BookOut)
def book_patch_update(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict(exclude_unset=True).items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

