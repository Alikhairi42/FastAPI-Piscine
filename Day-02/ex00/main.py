from fastapi import FastAPI

app = FastAPI()

records_db: dict ={
    1: {"id": 1, "name": "keyboard"},
    2: {"id": 2, "name": "Monitor"}
}

@app.get('/records')
def dic():
    return (list(records_db.values()))