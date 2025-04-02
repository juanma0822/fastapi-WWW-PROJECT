from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.users_service import (
    create_user as service_create_user,
    get_users as service_get_users,
    get_user_by_id as service_get_user_by_id,
    update_user as service_update_user,
    delete_user as service_delete_user,
)
from app.schemas.schemas import UserCreate, UserUpdate, UserResponse

router = APIRouter()

# Configurar Jinja2 para las plantillas
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", response_class=HTMLResponse, description="Muestra una lista de todos los usuarios en formato HTML.")
def get_users(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = service_get_users(db, skip=skip, limit=limit)
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

@router.get("/users", response_model=list[UserResponse], description="Obtiene una lista de todos los usuarios en formato JSON.")
def get_users_json(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service_get_users(db, skip=skip, limit=limit)

@router.get("/users/{documento_identidad}", response_model=UserResponse, description="Obtiene los detalles de un usuario específico por su documento de identidad.")
def get_user_by_id(documento_identidad: str, db: Session = Depends(get_db)):
    user = service_get_user_by_id(db, documento_identidad)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserResponse, description="Crea un nuevo usuario en la base de datos.")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service_create_user(db, user)

@router.put("/users/{documento_identidad}", response_model=UserResponse, description="Actualiza los datos de un usuario existente.")
def update_user(documento_identidad: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = service_update_user(db, documento_identidad, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{documento_identidad}", response_model=UserResponse, description="Elimina un usuario de la base de datos.")
def delete_user(documento_identidad: str, db: Session = Depends(get_db)):
    user = service_delete_user(db, documento_identidad)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user