from sqlalchemy.orm import Session
from sqlalchemy.sql import text

def get_all_users(db: Session):
    try:
        # Consultar todos los usuarios
        users = db.execute(text("SELECT * FROM users")).fetchall()
        
        # Convertir cada fila en un diccionario
        users_list = [dict(row._mapping) for row in users]  # Usar _mapping para convertir Row a dict
        
        return {"message": "✅ Conexión exitosa a Aiven PostgreSQL", "users": users_list}
    except Exception as e:
        return {"error": "❌ No se pudo conectar a la base de datos", "detail": str(e)}