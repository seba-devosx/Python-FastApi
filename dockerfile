# Usa la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación
COPY . .

# Exponer el puerto para FastAPI
EXPOSE 80

# Comando para iniciar la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]