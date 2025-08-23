# 📚 Book API (FastAPI + SQLAlchemy + JWT Auth)

A simple **Book Management API** built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**.  
This project is part of my learning journey in backend development and MLOps.

---

## 🚀 Features
- User registration with **password hashing (bcrypt)**  
- JWT-based authentication (login & token generation)  
- CRUD operations for books (Create, Read, Update, Delete)  
- Auto database session handling with `Depends(get_db)`  
- SQLite database (easy to switch to PostgreSQL/MySQL later)  

---

## 🛠 Tech Stack
- **FastAPI** – API framework  
- **SQLAlchemy** – ORM for database  
- **Pydantic** – Data validation  
- **Passlib** – Password hashing  
- **Python-Jose** – JWT tokens  
- **SQLite** – Database (default)  

---

## ⚡ Installation & Setup

Clone the repository:

git clone https://github.com/Dhinesh018/book_api.git

cd book_api

Create and activate a virtual environment:

python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run the API:

uvicorn main:app --reload

🔑 API Endpoints
Authentication

POST /users/ → Register a new user

POST /token → Login & get JWT access token

Books

GET /books/ → Get all books

POST /books/ → Add a new book

PUT /books/{id} → Update a book

DELETE /books/{id} → Delete a book

📖 Next Steps

Add more detailed book fields (author, year, genre, etc.)

Role-based access (Admin/User)

Dockerize the app for deployment

Integrate ML models for recommendations (future MLOps steps 🚀)
