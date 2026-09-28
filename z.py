from fastapi import FastAPI,HTTPException
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from ORM.SqlAlchemy2 import engine
from sqlalchemy import select
app=FastAPI()
from sqlalchemy2 import HealthRecord

class Base(DeclarativeBase):
    pass


@app.get("/posts/{id}")
def get_post(id:int):
    with Session(engine) as session:
        statement=select(HealthRecord).where(HealthRecord.id==id)
        post=session.scalars(statement).all()

        if not post:
            raise HTTPException(
                status_code=404,
                detail="post not found"
            )

        return post