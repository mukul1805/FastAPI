from pydantic import BaseModel

class Blog(BaseModel): 
    title:str
    body:str

#to show in this schema, we can use customised schema

class showBlog(BaseModel):       #we can use BaseModel as well, but is shows all of Blog Model
    title:str       #we want to show title only
    body:str
    class Config():
        orm_mode =True