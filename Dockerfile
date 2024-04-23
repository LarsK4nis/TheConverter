FROM python:3.8-slim

WORKDIR /app

# Copia solo los archivos necesarios para la instalación de las dependencias
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY src/ /app/

# Define el comando por defecto
CMD ["python", "app.py"]
