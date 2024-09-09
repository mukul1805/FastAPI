from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///C:/Users/mukulkumar.sahu/Desktop/FastAPI/Blog/blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})   #connection

#creating a session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)                 #interaction
                            #bind=engine ensures that all table is created that is specified in the engine

#declare a mapping  
Base = declarative_base()           #


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()