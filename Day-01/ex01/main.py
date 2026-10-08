from fastapi import FastAPI

app = FastAPI();
@app.get('/item')
def read_pram(q:str = None,limit: int = 10,offset:int = 0):
    return {"q": q, "limit": limit, "offset": offset}