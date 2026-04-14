# Usa una imagen base de Python ligera
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala las dependencias necesarias (si tienes un requirements.txt)
# Si no, al menos instalamos PyBuilder para que el contenedor pueda testearse
RUN pip install --no-cache-dir pybuilder

# Expone el puerto que usa Flask (5000 por defecto)
EXPOSE 5000

# Comando para arrancar la aplicación
# Ajusta 'inventory.py' si el nombre de tu archivo principal es distinto
CMD ["python", "src/main/python/bioguard/inventory.py"]
