from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace this with your Render PostgreSQL connection string
# Format: "postgresql://username:password@host:5432/dbname"
DATABASE_URL = "postgresql://bookapi_db_6ok6_user:g0zCkpD3MnWyiuLaRQNSO5TihbywcNBu@dpg-d2r8tbvdiees73e1ev80-a/bookapi_db_6ok6"

# Create engine (no connect_args needed for PostgreSQL)
engine = create_engine(DATABASE_URL)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class
Base = declarative_base()
