from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
def my_fun(item_id: int):
    return {"item_id" : item_id}

@app.get('/categories/{name}')
def my_fun(name: str):
    return {"name": name}