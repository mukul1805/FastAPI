from fastapi import FastAPI

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


@app.get('/blog/{id}')      #{} for dynamic routing
# def show(id):
def show(id:int):  #we can specify the datatype also
    #fetch blog with id=id
    return {"Data":id}

@app.get('/blog/{id}/comment') 
def show(id):
    #fetch comment of blog with id=id
    return {"Data":{'1','2'}}




#code is readed line by line, so pehle wo integer expect krega (dynamic routing), esliye error at unpublised


# so, move unpublised to above dynamic routing

# we can use swagger UI at / docs i.e.,http://127.0.0.1:8000/docs

# we can use redoc at / docs i.e.,http://127.0.0.1:8000/redoc