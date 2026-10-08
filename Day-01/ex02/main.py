from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
class Product(BaseModel):
    name: str
    price: int = Field(ge=0)
    in_stock: bool
    color: str = Field("red")

@app.post('/products')
def check_json(product: Product):
    print('in fonction')
    return product