from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.models import Base
from sqlalchemy.sql import text
from app.routes.users import router as users_router  # Importar el router de users

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir el router de users
app.include_router(users_router, prefix="/api", tags=["Users"])  # Prefijo opcional y etiquetas para la documentación

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    try:
        # Consultar todos los usuarios
        users = db.execute(text("SELECT * FROM users")).fetchall()
        
        # Convertir cada fila en un diccionario
        users_list = [dict(row._mapping) for row in users]  # Usar _mapping para convertir Row a dict
        
        return {"message": "✅ Conexión exitosa a Aiven PostgreSQL", "users": users_list}
    except Exception as e:
        return {"error": "❌ No se pudo conectar a la base de datos", "detail": str(e)}