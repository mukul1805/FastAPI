#uvicorn Blog.main:app --reload to run this main.py

from typing import List
from fastapi import FastAPI, Depends , status, Response , HTTPException
# from pydantic import BaseModel
from . import schemas,models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import blog,user

from .hashing import Hash       

app=FastAPI()

models.Base.metadata.create_all(engine)


#as we have created the separate router,
app.include_router(blog.router)
app.include_router(user.router)

# @app.post('/blog')
# def create(title,body):
#     return {"Title":title,"Body":body}
#     return "creating"

# class Blog(BaseModel):        we can move this to schemas
#     title:str
#     body:str

# def get_db():         #moved to databse
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog',tags=['Blog'])                  #using tags for segregating 
# def create(request: schemas.Blog, db: Session = Depends(get_db)):        #request is of type Blog 
#     # return request
#     new_blog = models.Blog(title=request.title,body=request.body,user_id=1)     #Hardcoded user_id here
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# to get all the blogs
# @app.get('/blog', response_model=list[schemas.showBlog],tags=['Blog'])        #using List bcz ot multiple responses
# def all_blog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# to get blog with particular id
#@app.get('/blog/{id}', status_code=201)                  #we can manually add status_code also!
# @app.get('/blog/{id}', status_code=status.HTTP_201_CREATED)         #to get status auto

# @app.get('/blog/{id}', status_code=201, response_model=schemas.showBlog,tags=['Blog'])         #to get response_model as defined in schema
# def show_with_id(id, response=Response, db: Session = Depends(get_db)):
#     blog_with_id = db.query(models.Blog).filter(models.Blog.id == id).first()   #where condition in sqlalchemy
#     if not blog_with_id:
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {f"Blog with id {id} is not available!"}

#         # return Response(
#         #     content=f"Blog with id {id} is not available!",
#         #     status_code=status.HTTP_404_NOT_FOUND
#         # )

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} is not available!")
#     return blog_with_id




# #to delete  blog with particular id

# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=['Blog'])
# def destroy(id, db: Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     blog.delete(synchronize_session=False)
#     db.commit()     #after alterning DB always commit it!
#     return {"Delete Successfully...!"}


# #to update data

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['Blog'])
# def update(id, request= schemas.Blog ,db: Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail= f"Blog with id {id} is not found.")
#     blog.update(request)
#     db.commit()
#     return "Updated Successfully"



# # to create a new User

# @app.post('/user',response_model=schemas.showUser,tags=['User'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     # new_user = models.User(request)     #only request will not work, use 
#     # hashed_password = pwd_cxt.hash(request.password)
#     new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)        #refresh at new_user
#     return new_user

# @app.get('/user',tags=['User'])
# def all_user(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.get('/user/{id}',response_model=schemas.showUser,tags=['User'])
# def user_by_id(id=int, db: Session = Depends(get_db)):
#     user_with_id = db.query(models.User).filter(models.User.id == id).first()   #where condition in sqlalchemy
#     if not user_with_id:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id {id} is not available!")
#     return user_with_id