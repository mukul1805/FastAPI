from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///C:/Users/mukulkumar.sahu/Desktop/FastAPI/Blog/blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

#creating a session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#declare a mapping
Base = declarative_base()