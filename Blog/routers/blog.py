from fastapi import APIRouter, Depends, Response, status, HTTPException
from typing import List
from .. import schemas, database,models
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/blog', response_model=list[schemas.showBlog],tags=['Blog'])        #using List bcz ot multiple responses
def all_blog(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog',tags=['Blog'])                  #using tags for segregating 
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):        #request is of type Blog 
    # return request
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)     #Hardcoded user_id here
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog/{id}', status_code=201, response_model=schemas.showBlog,tags=['Blog'])         #to get response_model as defined in schema
def show_with_id(id, response=Response, db: Session = Depends(database.get_db)):
    blog_with_id = db.query(models.Blog).filter(models.Blog.id == id).first()   #where condition in sqlalchemy
    if not blog_with_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available!")
    return blog_with_id

#to delete  blog with particular id
@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=['Blog'])
def destroy(id, db: Session = Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.delete(synchronize_session=False)
    db.commit()     #after alterning DB always commit it!
    return {"Delete Successfully...!"}

#to update data
@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['Blog'])
def update(id, request= schemas.Blog ,db: Session = Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Blog with id {id} is not found.")
    blog.update(request)
    db.commit()
    return "Updated Successfully"

