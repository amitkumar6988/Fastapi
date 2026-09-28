from fastapi import FastAPI,status
from mine import schemas
from pydantic import *
from mine.models import creatingrecord
from mine.db import engine,Base
from sqlalchemy.orm import Session

from mine.routers import users,auth


app=FastAPI()

Base.metadata.create_all(engine)
@app.post("/post",response_model=schemas.UserResponse)
def create_post(post:schemas.Create_record_posts):
    with Session(engine) as session:
        a=creatingrecord(title=post.title,content=post.content,published=post.published)
        session.add(a)
        session.commit()
        session.refresh(a)
        return {
            "id":a.id,
            "title":a.title,
            "content":a.content,
            "published":a.published,
            "created_at":a.created_at
        }

app.include_router(users.router)
app.include_router(auth.router)

