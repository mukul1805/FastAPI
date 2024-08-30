#uvicorn Blog.main:app --reload to run this main.py

from fastapi import FastAPI, Depends
# from pydantic import BaseModel
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine)

# @app.post('/blog')
# def create(title,body):
#     return {"Title":title,"Body":body}
#     return "creating"

# class Blog(BaseModel):        we can move this to schemas
#     title:str
#     body:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):        #request is of type Blog
    # return request
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# to get all the blogs
@app.get('/blog')
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# to get blog with particular id
@app.get('/blog/{id}')
def show_with_id(id,db: Session = Depends(get_db)):
    blog_with_id = db.query(models.Blog).filter(models.Blog.id == id).first()   #where condition in sqlalchemy
    return blog_with_id