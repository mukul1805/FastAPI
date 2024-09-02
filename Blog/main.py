#uvicorn Blog.main:app --reload to run this main.py

from fastapi import FastAPI, Depends , status, Response , HTTPException
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
#@app.get('/blog/{id}', status_code=201)                  #we can manually add status_code also!
@app.get('/blog/{id}', status_code=status.HTTP_201_CREATED)         #to get status auto
def show_with_id(id, response=Response, db: Session = Depends(get_db)):
    blog_with_id = db.query(models.Blog).filter(models.Blog.id == id).first()   #where condition in sqlalchemy
    if not blog_with_id:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {f"Blog with id {id} is not available!"}

        # return Response(
        #     content=f"Blog with id {id} is not available!",
        #     status_code=status.HTTP_404_NOT_FOUND
        # )

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available!")
    return blog_with_id




#to delete  blog with particular id

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()     #after alterning DB always commit it!
    return {"Delete Successfully...!"}