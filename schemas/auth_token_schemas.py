from pydantic import BaseModel

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
    username: str | None = None


class UserInDB(User):
    hashed_password: str