from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel

app = FastAPI()

books_db = {}
next_book_id = 1

def pagination(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=50)
):
    return {"skip": skip, "limit": limit}

def verify_api_key(
    api_key: str | None = None,
    x_api_key: str | None = Header(default=None)
):
    if api_key != "piscine-key" and x_api_key != "piscine-key":
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

class BookCreate(BaseModel):
    title: str
    author: str
    available: bool = True

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    available: bool

@app.post("/books", status_code=201)
def create_book(book: BookCreate, api_key = Depends(verify_api_key)):
    global next_book_id

    for existing_book in books_db.values():
        if existing_book["title"] == book.title:
            raise HTTPException(status_code=400, detail="Book already exists")

    new_book = {
        "id": next_book_id,
        **book.model_dump()
    }

    books_db[next_book_id] = new_book
    next_book_id += 1

    return new_book

@app.get("/books")
def get_books(p = Depends(pagination)):
    books = list(books_db.values())

    return books[p["skip"]:p["skip"] + p["limit"]]

@app.get("/books/{id}")
def get_book(id: int):
    if id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    return books_db[id]

@app.put("/books/{id}")
def update_book(
    id: int,
    book: BookCreate,
    api_key = Depends(verify_api_key)
):
    if id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    for existing_id, existing_book in books_db.items():
        if existing_id != id and existing_book["title"] == book.title:
            raise HTTPException(status_code=400, detail="Book already exists")

    updated_book = {
        "id": id,
        **book.model_dump()
    }

    books_db[id] = updated_book

    return updated_book