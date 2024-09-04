from pydantic import BaseModel


#creating schema for user

class User(BaseModel):
    name: str
    email:str
    password:str

class showUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode =True          #to interact with another class


#schema from blog
class Blog(BaseModel): 
    title:str
    body:str
    creator: showUser 

#to show in this schema, we can use customised schema

class showBlog(BaseModel):       #we can use BaseModel as well, but is shows all of Blog Model
    title:str       #we want to show title only
    body:str
    class Config():
        orm_mode =True

