from pydantic import BaseModel

class User(BaseModel):
    title:str
    content:str
    published:bool


class UpdatePost(BaseModel):
    title:str|None=None
    content:str|None=None
    published:bool|None=None
