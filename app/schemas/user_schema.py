from pydantic import BaseModel,Field


#ejemplo de como se hereda un basemodel para que tengan los mismo atributos
# class UserBase(BaseModel):
#     email:str =  Field(...,min_length=1,max_length=50,example='sebastianigna@gmail.com')

# class Password(UserBase):
#     Password:str
    
class UserCreate(BaseModel):
    #base model
    #se indica que tipos de dato son los respectibos datos los cuales se necesitan
    #se permite agregar el largo inimo y maximo ademas de agregae un ejemplo el cual se puede ver dentro del suagger 
    name:str =  Field(...,min_length=1,max_length=50,example='sebastian')
    lastname:str = Field(...,min_length=1,max_length=50,example='aravena')
    email:str =  Field(...,min_length=1,max_length=50,example='sebastianigna@gmail.com')
    address:str = Field(...,min_length=1,max_length=50,example='ave siempre viva')
    paswrd:str = Field(...,min_length=1,max_length=60,example='pasword')
    #disabled:bool=  Field(...,example='1')

    

class GetUser(UserCreate):
    email:str =  Field(...,min_length=1,max_length=50,example='sebastianigna@gmail.com')
    
class GetallUser(UserCreate):
    id:int


class Update_user(UserCreate):
    email:str =  Field(...,min_length=1,max_length=50,example='sebastianigna@gmail.com')

class Delete_user(BaseModel):
    message: str
    email: str 
    
class config:
        orm_mode=True

