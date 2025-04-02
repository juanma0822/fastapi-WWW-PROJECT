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

@router.get("/users", response_class=HTMLResponse)
def get_users(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = service_get_users(db, skip=skip, limit=limit)
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

@router.get("/users", response_model=list[UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service_get_users(db, skip=skip, limit=limit)

@router.get("/users/{documento_identidad}", response_model=UserResponse)
def get_user_by_id(documento_identidad: str, db: Session = Depends(get_db)):
    user = service_get_user_by_id(db, documento_identidad)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{documento_identidad}", response_model=UserResponse)
def update_user(documento_identidad: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = service_update_user(db, documento_identidad, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{documento_identidad}", response_model=UserResponse)
def delete_user(documento_identidad: str, db: Session = Depends(get_db)):
    user = service_delete_user(db, documento_identidad)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user