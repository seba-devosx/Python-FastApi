from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import relationship
from database.database_config import Base


#para poder definir las tablas que se crearan dentro de la base de datos
#se deberan generar clases definiendo el table-name->nombre de la tabla
# y los tipos de datos que dese alamcenar dentro de la base de datos
#se hereda Base el cual se definio dentro de database_config.py
class User(Base):
    __tablename__= 'Usuarios'

    id=Column((Integer),primary_key=True,autoincrement='auto')
    name=Column(String(50),nullable=False)
    lastname=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False)
    address=Column(String(50),nullable=False)
   #passwd=Column(String(7),nullable=False)

#direcciones= relationship('Direccion',back_populates='Users')

# class Direccion(Base):
#     __tablename__='Direcciones'
#     id_direcciones=Column(Integer,primary_key=True,autoincrement='auto')
#     comuna=Column(String(50),nullable=False)
#     ciudad=Column(String(50),nullable=False)
#     direccion_usuario=Column(String(50),nullable=False)
#     active_direccion=Column(Boolean,default=True)

#     usuarios= relationship('Usuarios',back_populates='Direcciones')

