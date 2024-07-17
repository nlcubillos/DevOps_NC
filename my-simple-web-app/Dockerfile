# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Deshabilita la verificación SSL
ENV PYTHONHTTPSVERIFY=0

# Copia todos los archivos del directorio actual al directorio /app en el contenedor
COPY . .

# Instala las dependencias necesarias
RUN pip3 install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org Flask

# Expone el puerto 5000 para que Flask pueda ejecutarse
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python3", "./app.py"]
