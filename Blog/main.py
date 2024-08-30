#uvicorn Blog.main:app --reload to run this main.py

from fastapi import FastAPI
# from pydantic import BaseModel
from . import schemas
from . import models
from .database import engine

app=FastAPI()

models.Base.metadata.create_all(engine)

# @app.post('/blog')
# def create(title,body):
#     return {"Title":title,"Body":body}
#     return "creating"

# class Blog(BaseModel):        we can move this to schemas
#     title:str
#     body:str

@app.post('/blog')
def create(request: schemas.Blog):        #request is of type Blog
    return request