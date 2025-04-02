from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.schemas import UserCreate, UserUpdate

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, documento_identidad: str):
    return db.query(User).filter(User.documento_identidad == documento_identidad).first()

def update_user(db: Session, documento_identidad: str, user_update: UserUpdate):
    db_user = db.query(User).filter(User.documento_identidad == documento_identidad).first()
    if not db_user:
        return None
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, documento_identidad: str):
    db_user = db.query(User).filter(User.documento_identidad == documento_identidad).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user