from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date, datetime
from typing import Optional

class UserBase(BaseModel):
    documento_identidad: str
    nombre: str
    apellido: str
    edad: int
    genero: str
    fecha_nacimiento: date
    lugar_nacimiento: str
    pais_residencia: str
    correo: EmailStr
    telefono: Optional[str]
    direccion: Optional[str]

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    edad: Optional[int]
    genero: Optional[str]
    fecha_nacimiento: Optional[date]
    lugar_nacimiento: Optional[str]
    pais_residencia: Optional[str]
    correo: Optional[EmailStr]
    telefono: Optional[str]
    direccion: Optional[str]

class UserResponse(UserBase):
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    # Configuración para Pydantic v2
    model_config = ConfigDict(from_attributes=True)