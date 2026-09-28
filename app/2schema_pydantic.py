from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    city:str

app=FastAPI()

@app.post("/users")
async def get_users(user: User):
    return{
        "message":"user created",
        "user_data":user
    }