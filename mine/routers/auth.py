from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from sqlalchemy import select 
from mine import schemas
from mine.db import engine
from mine import models
from .. import utils

router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials:schemas.UserLogin):
    with Session(engine) as session:
        statement=select(models.User).where(models.User.email==user_credentials.email)
        user=session.scalar(statement)
        if not user:
            raise HTTPException (
                status_code=status.HTTP_404_NOT_FOUND,
                detail="invalid Credentials"
            )

        if not utils.verify(user_credentials.password,user.password):
            raise HTTPException (
                status_code=status.HTTP_404_NOT_FOUND,
                detail='email or password is wrong'
        )
    return {"message":"token created"}




        

