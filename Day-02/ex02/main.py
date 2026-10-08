from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel

app = FastAPI()

records_db: dict ={
    1: {"id": 1, "name": "keyboard"},
    2: {"id": 2, "name": "Monitor"}
}

class RecordCreate(BaseModel):
    name: str

@app.post('/records',status_code=201)
def check(record: RecordCreate):
    for exit_rec in records_db.values():
        if exit_rec["name"] == record.name:
                    raise HTTPException(
                status_code=400,
                detail="Duplicate record"
            )
    new_id = max(records_db.keys()) + 1

    records_db[new_id] = {
        "id":new_id,
        "name": record.name
    }
    return records_db[new_id]
