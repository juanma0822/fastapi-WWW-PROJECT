from fastapi import FastAPI
from app.database import Base, engine
from app.routes.users import router as users_router
from app.controllers.root_controller import router as root_router

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas
app.include_router(users_router, prefix="/api", tags=["Users"])
app.include_router(root_router)  # Incluir el controlador para el endpoint raíz