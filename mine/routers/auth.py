from fastapi import APIRouter,Depends,ststus,HTTPException,Response,
from sqlalchemy.orm import Session
from sqlalchemy import select 
from mine import schemas
from mine.db import engine
from mine.models import users

router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials:schemas.UserLogin):
    with Session(engine) as session:
        statement=select(users).where(users.email==user_credentials.email)



        

