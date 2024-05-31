from fastapi import FastAPI 
from models.product import Product

app = FastAPI()

@app.get('/')
def hello_world():
    """
    Primeiro Hello world!
    """
    return{"Hello":"world!"}

@app.get('/{nome}')
def hello(nome: str):
    if not nome:
        pass
    return {"hello": nome}

data = [
    Product (id=1, name='Tenis Nike Air', description= 'Cool shoes', price= 199.00),
    Product (id=2, name='Iphone', description= 'Mobile', price= 1999.00),
    Product (id=3, name='Samsung', description= 'Mobile', price= 2000.00),
    Product (id=4, name='Notebook', description= 'Eletronics', price= 4897.00),
]

@app.get ('/api/products')
def get_products():
    return data

@app.get ('/api/products/{id}')
def get_products_by_id(id: int):
    for product in data: 
        if product.id == id:
            return product
    return {"message": "no product found with the id."}
        

