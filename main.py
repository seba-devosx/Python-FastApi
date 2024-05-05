
from fastapi import FastAPI
from routes.users import router_user

app = FastAPI()

##importacion de rutas
#al importar la roue_user se idica el prefijo que usara la api 
#y se define el tag que utilizara
app.include_router(router_user,prefix="/user",tags=["Users"])

