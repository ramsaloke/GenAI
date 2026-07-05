from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"this is my home page"}

@app.get("/about")
def about():
    return {"message": "this is my about page"}

@app.get("/contact")
def contact():
    return {"message": "this is my contact page"}

@app.get("/orders")
def order():
    return {"message": "this is my orders page"}