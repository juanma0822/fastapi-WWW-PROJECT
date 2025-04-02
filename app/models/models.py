from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, Text
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    documento_identidad = Column(String(20), primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    genero = Column(String(20), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    lugar_nacimiento = Column(String(255), nullable=False)
    pais_residencia = Column(String(100), nullable=False)
    correo = Column(String(255), unique=True, nullable=False)
    telefono = Column(String(20), unique=True)
    direccion = Column(Text)
    fecha_creacion = Column(TIMESTAMP, server_default=func.now())
    fecha_actualizacion = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())