from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()
class User(BaseModel):
    name:str
    age:int
    location:str

@app.get("/")
async def  root():
    return {"message":"hey this is amit"}


@app.post("/about")
def about(user:dict):
    return {"message":"user created{user}"}


