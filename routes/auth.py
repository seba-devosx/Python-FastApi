from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth.auth import authenticate_user,create_token, ACCESS_TOKEN_EXPIRE_MINUTES,get_current_active_user
from schemas.auth_token_schemas import Token,User
from  database.database_config import get_db_session
from datetime import datetime, timedelta, timezone

router_auth=APIRouter()

@router_auth.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    print('router_auth',form_data.username,form_data.password)
    user = authenticate_user(db,form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(
        data={"sub": user.email}, expire_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router_auth.get("/users/me/", response_model=User)
async def read_users_me(current_user: Token = Depends(get_current_active_user)):
    print("User",current_user)
    return current_user
