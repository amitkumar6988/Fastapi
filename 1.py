from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app=FastAPI()


@app.get("/")
async def secondapi():
    return {"amit":"kajal"}
@app.get("/firstapi")
async def firstapi():
    return {"i made my first api":"kajal"}

@app.post("/createpost")
def createpost(post: dict=Body(...)):
    print(post)
    return {"post":f"title{post["post"]}"} 
