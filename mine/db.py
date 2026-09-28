from fastapi import FastAPI,HTTPException
from sqlalchemy.orm import *
from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv
load_dotenv()


database_url=os.getenv("URL")
if not database_url:
    raise ValueError("url not found in dot env")
engine=create_engine(database_url)

class Base(DeclarativeBase):
    pass


try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))


    print("db connected")
    
except Exception as error:
    print("db was not connected")
    print("error:",error)








