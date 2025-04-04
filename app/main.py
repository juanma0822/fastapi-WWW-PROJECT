from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.database import Base, engine
from app.routes.users import router as users_router
from app.controllers.root_controller import router as root_router

app = FastAPI(
    title="API RESTful de Usuarios",
    description=(
        "Bienvenido a la API RESTful construida enteramente en FastAPI para implementar un CRUD de usuarios dentro de un backend. "
        "Todo esto con fines de prácticas en la materia. Esperamos y encuentres la documentación necesaria y te guste! "
        "Desarrollado por: Juan Manuel Valencia - Isabella Rebellon Medina."
    ),
    version="1.0.0",
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Configurar Jinja2 para las plantillas
templates = Jinja2Templates(directory="app/templates")

# Incluir las rutas
app.include_router(users_router, prefix="/api", tags=["Users"])
app.include_router(root_router)  # Incluir el controlador para el endpoint raíz