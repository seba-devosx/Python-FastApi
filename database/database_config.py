from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv('helpers/.env')
URL=os.getenv('DATABASE_URL_MYSQL')


engine=create_engine(URL)

#session maker ayuda a poder generar una session cada ves que se quiera consultar a la base de deatos
sessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)

#permite por hacer uso ddel orm y poder crear cada uno de los modelos
Base = declarative_base()


