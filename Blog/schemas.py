from pydantic import BaseModel
from typing import List,Optional


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


#for login

class Login(BaseModel):
    username: str
    password: str



#for token

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None