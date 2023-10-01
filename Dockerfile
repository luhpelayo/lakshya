# Usa una imagen base de Python 3.8-slim
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala Django 4.2
RUN pip install Django==4.2

# Copia todo el contenido de tu proyecto Django al contenedor
COPY . .

# Expón el puerto en el que se ejecuta tu aplicación Django (por ejemplo, el puerto 8000)
EXPOSE 8000

# Comando para ejecutar tu aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
