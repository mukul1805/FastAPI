from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get('/')
def index():
    # return 'Heyyyy'
    return {"Data":{"Name":"Mukul"}}


@app.get('/about')      #operation #path    #@ is path decorator
def index():            #path operation function
    return {"Data":{"About":"About me data"}}

@app.get('/blog/unpublished')
def unpublised():
    return {"Data":"All unpublished data"}

#this is path parameter
@app.get('/blog/{id}')      #{} for dynamic routing
# def show(id):
def show(id:int):  #we can specify the datatype also
    #fetch blog with id=id
    return {"Data":id}

@app.get('/blog/{id}/comment') 
def show(id):
    #fetch comment of blog with id=id
    return {"Data":{'1','2'}}

#this is query Parameter
@app.get("/hello")
async def hello(name:str,age:int):
   return {"name": name, "age":age}
#http://127.0.0.1:8000/hello?name=mukul&age=20


#combination of path and query parameter
@app.get("/hello/{name}")
async def hello(name:str,age:int):
   return {"name": name, "age":age}
#http://127.0.0.1:8000/hello/mukul?age=21


@app.get("/bloging")
def index(limit=10,published:bool=True, sort: Optional[str]=None):      #default value setting, and setting optional
    if published:
        return {'Data': f'{limit} published blogs'}
    else:
        return {'Data': f'{limit} blogs'}



#to run it directly as python program
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
   # now we can use python main.py command to run it....



#code is readed line by line, 
# so it will expect integer (dynamic routing), thats why error at unpublised
# so, move unpublised to above dynamic routing

# we can use swagger UI at / docs i.e.,http://127.0.0.1:8000/docs
# we can use redoc at / docs i.e.,http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/openapi.json use this URL in the browser to generate automatically the interactive documentation.




# post methods..............

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]       #option h but show q nhi ho rha (Check it)



@app.post("/blog")
def create_blog(request: Blog):
    return {"Data": f'Blog is create with title as {request.title}'}
    return request
    return {"Data":"Blog is created"}