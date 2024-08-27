from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    # return 'Heyyyy'
    return {"Data":{"Name":"Mukul"}}


@app.get('/about')
def index():
    return {"Data":{"About":"About me data"}}