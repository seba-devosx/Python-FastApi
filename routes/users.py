from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database.database_config import sessionLocal, engine
from database.models import model_user
from schemas import user_schema
from database.utils import crud


model_user.Base.metadata.create_all(bind=engine)



router_user=APIRouter()

#funcion para crea la session 
def get_db_session():
    db_session=sessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

#insert de usuarios 
@router_user.post("/create_user",response_model=user_schema.UserCreate)
async def create_user(user:user_schema.UserCreate, db:Session=Depends(get_db_session)):
    db_user=crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

#obtencion de usuarios por el email
@router_user.get("/get_user/{email}",response_model=user_schema.GetUser)
async def get_user_email(email : str, db:Session=Depends(get_db_session)):
    db_user = crud.get_user_by_email(db, email = email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router_user.get("/getAll_user", response_model=list[user_schema.GetallUser])
async def getAll_user(skip:int=0, limit:int=10,db:Session=Depends(get_db_session)):
    db_user=crud.get_all_user(db,skip=skip,limit=limit)
    return db_user

@router_user.put("/modify_user/{email}",response_model=user_schema.Update_user)
async def modify_user_by_email(email:str ,user:user_schema.Update_user,db:Session=Depends(get_db_session)):
    existing_user=crud.get_user_by_email(db=db,email=email)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.update_user(db,existing_user,user)
    return existing_user

@router_user.delete("/delete_user/{email}", response_model=user_schema.Delete_user)
async def delete_user_by_email(email:str, db:Session=Depends(get_db_session)):
    db_user= crud.delete_user(db,email=email)
    email_delete=email
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user_schema.Delete_user(message='Este usuarios fue elimnado',email=email)
