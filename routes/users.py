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

@router_user.post("/create_user",response_model=user_schema.UserCreate)
async def create_user(user:user_schema.UserCreate, db:Session=Depends(get_db_session)):
    db_user=crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
    


#ejemplo
#queryparamater
#mostraar un limite de elementos correspondientes a fake items
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@router_user.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return { "items":fake_items_db[skip : skip + limit]}