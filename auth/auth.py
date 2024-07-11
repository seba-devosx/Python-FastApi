from datetime import datetime,timedelta,timezone
from typing import Optional
import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from database.utils import crud
from fastapi import Depends, HTTPException, status
from schemas.auth_token_schemas import TokenData,User
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from database.database_config import get_db_session


SECRET_KEY = "82fcccd019fcd8092df06577b328737157932cf9c9cf5d265a0b74f77980d206"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
Oauth_schemes=OAuth2PasswordBearer(tokenUrl="token")



def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def create_token(data: dict, expire_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expire_delta:
        expire=datetime.now(timezone.utc)+expire_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def authenticate_user(db, email: str, password: str):
    user = crud.get_user_by_email(db,email)
    if not user:
        return False
    if not verify_password(password, user.paswrd):
        return False
    return user

async def get_current_user(token: str = Depends(Oauth_schemes), db:Session=Depends(get_db_session)):
   
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        print('token',username)
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = crud.get_user_by_email(db,token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User=Depends(get_current_user)):
    print("datos",current_user)
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


