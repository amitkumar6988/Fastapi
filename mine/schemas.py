from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import datetime

class User(BaseModel):#this was for request
    name:str
    age:int
    location:str

class Create_record_posts(BaseModel):
    title:str
    content:str
    published:bool

class UserResponse(Create_record_posts):#inheritance
    created_at:datetime
    id:int

#schema for verifying users when creation
class UserCreate(BaseModel):
    email:EmailStr
    password:str
#schema for response after user creation
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email:EmailStr
    password:str
