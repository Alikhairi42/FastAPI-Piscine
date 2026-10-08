from fastapi import FastAPI , HTTPException


records_db: dict ={
    1: {"id": 1, "name": "keyboard"},
    2: {"id": 2, "name": "Monitor"}
}

app = FastAPI()

@app.get('/records/{id}')
def check_id(id: int):
        if id in records_db:
            return list(records_db[id])
        else:
            raise HTTPException(status_code=404, detail="Record not found")
        