from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name:str 
    lastname:str 
    email:str 
    address:str
    paswrd:str 
    disabled:bool

class auth_login(BaseModel):
    email:str 
    paswrd:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str]= None


class UserInDB(User):
    hashed_password: str