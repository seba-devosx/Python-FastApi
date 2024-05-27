from sqlalchemy.orm import Session
from database.models import model_user
from schemas import user_schema

#aca se debe almacenar cada unos de los metodos del crud
# para luego se utilizados en las routes.users
def create_user(db:Session,user:user_schema.UserCreate):
    db_user= model_user.User(name=user.name,lastname=user.lastname,email=user.email,address=user.address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(model_user.User).filter(model_user.User.email == email).first()

def get_all_user(db:Session, skip: int=0, limit : int=10):
    return db.query(model_user.User).offset(skip).limit(limit).all()

def update_user(db:Session,existing_user:model_user.User,user:user_schema.Update_user):
    existing_user.email=user.email
    existing_user.name=user.name
    existing_user.lastname=user.lastname
    existing_user.address=user.address
    db.commit()
    return db

def delete_user(db:Session, email:str):
    db.query(model_user.User).filter(model_user.User.email==email).delete()
    db.commit()
    return db
    