
from fastapi import FastAPI,status,Depends
from routes.users import router_user
from routes.auth import router_auth
from fastapi.middleware.cors import CORSMiddleware
from database.database_config import engine
from database.models import model_user
app = FastAPI()


#crecion de tablas en las base de datos
model_user.Base.metadata.create_all(bind=engine)

##importacion de rutas
#al importar la roue_user se idica el prefijo que usara la api 
#y se define el tag que utilizara

app.include_router(router_auth)
app.include_router(router_user,prefix="/v1/user",tags=["Users"])

#implementacion de cors y middleware

#origenes que estan permitido el cosumo de la api
origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
]

#añadir el middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,#permite los origenes que se definieron dentro de origins
    allow_credentials=True,
    allow_methods=["*"],#permite el uso de todos los metodos
    allow_headers=["*"],#permite todos los encabezados
)
