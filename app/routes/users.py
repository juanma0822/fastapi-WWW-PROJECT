from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_user as crud_create_user, get_users as crud_get_users, get_user_by_id as crud_get_user_by_id, update_user as crud_update_user, delete_user as crud_delete_user
from app.schemas.schemas import UserCreate, UserUpdate, UserResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_create_user(db, user)

@router.get("/users", response_model=list[UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_get_users(db, skip=skip, limit=limit)

@router.get("/users/{documento_identidad}", response_model=UserResponse)
def get_user_by_id(documento_identidad: str, db: Session = Depends(get_db)):
    user = crud_get_user_by_id(db, documento_identidad)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{documento_identidad}", response_model=UserResponse)
def update_user(documento_identidad: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = crud_update_user(db, documento_identidad, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{documento_identidad}", response_model=UserResponse)
def delete_user(documento_identidad: str, db: Session = Depends(get_db)):
    user = crud_delete_user(db, documento_identidad)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user