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