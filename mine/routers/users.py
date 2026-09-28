
from fastapi import status,HTTPException,APIRouter
from mine import schemas
from pydantic import *
from mine.models import User
from mine.db import engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
#creating users for the users table
pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto")

router=APIRouter()
@router.post("/create_users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_users(user:schemas.UserCreate):
    with Session(engine) as session:
        hashed_password=pwd_context.hash(user.password)
        user.password=hashed_password
        new_user=User(email=user.email,password=user.password)


        session.add(new_user)
        try:
            session.commit()
            session.refresh(new_user)

        except IntegrityError:
            session.rollback()
            raise HTTPException(status_code=400,
                                detail="email already registered")

        return new_user