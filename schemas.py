from pydantic import BaseModel , EmailStr


class BookBase(BaseModel):
    title : str
    author : str
    year : int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None

class BookOut(BookBase):
    id : int
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username : str
    email: EmailStr

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id : int
    
    class config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
