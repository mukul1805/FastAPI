from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from fastapi import HTTPException, status, Response

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog,db: Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)     #Hardcoded user_id here
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int,db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.delete(synchronize_session=False)
    db.commit()     #after alterning DB always commit it!
    return "Deleted Successfully...!"

def update(id:int , request: schemas.Blog, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Blog with id {id} is not found.")
    blog.update(request)
    db.commit()
    return "Updated Successfully"

def show(id:int, response: Response, db:Session):
    blog_with_id = db.query(models.Blog).filter(models.Blog.id == id).first()   #where condition in sqlalchemy
    print(f"Fetching blog with ID {id} from the database.")
    if not blog_with_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available!")
    return blog_with_id