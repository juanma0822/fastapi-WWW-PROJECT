# 🚀 Proyecto FastAPI - API de Usuarios 🧑‍💻🐍

Este proyecto contiene el código de una **API RESTful** desarrollada con **FastAPI** ⚡ para la gestión de usuarios. La API está desplegada en **Railway** 🚆 y **Render** 🎭, y utiliza **Aiven** 💾 como servicio de base de datos con **PostgreSQL** 🐘.

## ☁️ Despliegue en la Nube

🌎 La API está disponible en los siguientes servicios:
- 🚆 **Railway:** [🔗 fastapi-wwwproject.up.railway.app](https://fastapi-wwwproject.up.railway.app)
- 🎭 **Render:** [🔗 fastapi-www-project.onrender.com](https://fastapi-www-project.onrender.com)

🔹 Para visualizar los usuarios en una interfaz **HTML** amigable 🖥️:
- [🔗 fastapi-wwwproject.up.railway.app/api/users/users](https://fastapi-wwwproject.up.railway.app/api/users/users)
- [🔗 fastapi-www-project.onrender.com/users/users](https://fastapi-www-project.onrender.com/users/users)

Esto mostrará una 🖥️ interfaz visual con la lista de usuarios almacenados en la 📦 **BD**.

---

## 🛠 Instalación y Ejecución Local 🏠

### 1️⃣ Clonar el Repositorio 🛜
```bash
 git clone https://github.com/tu-usuario/tu-repositorio.git
 cd tu-repositorio
```

### 2️⃣ Crear un Entorno Virtual 🏗️ y Activarlo 🏃‍♂️
```bash
python -m venv venv
# 🪟 Windows:
venv\Scripts\activate
# 🍏 macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Instalar Dependencias 📦
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Variables de Entorno 🔑
📄 Crea un archivo **.env** en la raíz del proyecto y agrega:
```env
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_bd
```
Asegúrate de reemplazar los valores con los datos de la **BD** en **Aiven** 🐘.

### 5️⃣ Ejecutar el Servidor 🚀
```bash
uvicorn app.main:app --host 0.0.0.0 --reload
```
La API estará disponible en **🌐 http://127.0.0.1:8000**.

📜 Para ver la documentación interactiva:
- 📘 **Swagger UI:** [🔗 127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📕 **ReDoc:** [🔗 127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Endpoints de la API 🛣️

| 🛠️ Método | 🌍 Ruta | 📖 Descripción |
|---------|------|-------------|
| **GET** 🟢 | `/api/users/users` | 📜 Obtiene la lista de usuario en **JSON** y en una vista **HTML** 🖥️. |
| **POST** 🟡 | `/api/users/create` | ✍️ Crea un nuevo usuario en la **BD**. |
| **GET** 🔵 | `/api/users/{id}` | 🔍 Obtiene los detalles de un usuario específico. |
| **PUT** 🟠 | `/api/users/update/{id}` | ✏️ Actualiza la info de un usuario. |
| **DELETE** 🔴 | `/api/users/delete/{id}` | ❌ Elimina un usuario de la **BD**. |

Para probar los endpoints, usa **Swagger UI** 📘 o herramientas como **Postman** 📩.

---

## 📂 Base de Datos (PostgreSQL en Aiven) 🐘💾

La API usa una **BD** en **Aiven** 📦 con **PostgreSQL** 🐘.
La tabla principal **users** 📊 tiene la siguiente estructura:
```sql
CREATE TABLE users (
    documento_identidad VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

⚙️ Se implementó un **trigger** 🔄 para actualizar `fecha_actualizacion` cada vez que un 👤 es modificado.

---

## 📝 Autores ✍️
- **Juan Manuel Valencia** 🎓 Código: *202159859*
- **Isabella Rebellon Medina** 🎓 Código: *202059968*

Este proyecto fue desarrollado como parte de nuestras **prácticas** y aprendizaje en **desarrollo backend** con **FastAPI** para la materia de **Aplicaciones en la web y redes inalambricas**⚡🚀.

