from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
import time
from schema import User,UpdatePost

load_dotenv()



while True:
    try:
        conn=psycopg2.connect(host=os.getenv("DB_HOST"),
                            database=os.getenv("DB_NAME"),
                            user=os.getenv("DB_USER"),
                            password=os.getenv("DB_PASSWORD"),
                            cursor_factory=RealDictCursor)
        print("database connection was successful")
        cursor=conn.cursor()
    
        break


    except Exception as error:
        print("database connection was not successfull")
        print("error:",error)
        time.sleep(2)





app=FastAPI()


#get get posts from db
@app.get("/posts")
def get_posts():
    cursor.execute("""select * from posts""")
    posts=cursor.fetchmany(2)
    return {"data":posts}
#insert post into db
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:User):
    cursor.execute("""insert into posts (title,content,published) values(%s,%s,%s) returning *;""",(post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return {"data":new_post}

#get post where id=?
@app.get("/posts/{id}")
def get_post(id:int):
    cursor.execute("""select * from posts where id =%s""",(str(id)))
    post=cursor.fetchone()
    return {"post":post}


@app.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute("""delete from posts where id =%s returning *""",(id,))
    deleted_post=cursor.fetchone( )
    conn.commit()
    return {"message":f"{deleted_post} was deleted successfully"}



@app.patch("/posts/{id}")
def update_post(id:int,post:UpdatePost):
    cursor.execute("""update posts set title=%s,content=%s where id=%s returning *""",(post.title,post.content,id,))
    updated_post=cursor.fetchone()
    conn.commit()
    return {"data":updated_post}





    






