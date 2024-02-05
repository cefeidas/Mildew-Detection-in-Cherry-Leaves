# Uso de una imagen base de Python
FROM python:3.8-slim

# Configurar el entorno sin interacción durante la construcción
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar solo las dependencias necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Node.js para cualquier necesidad de frontend (si es necesario)
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs

# Crear y cambiar al directorio de trabajo
WORKDIR /app

# Copiar el modelo entrenado y los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# (Opcional) Si tienes un script para configurar Heroku o hacer otras configuraciones
# COPY ./build-assets/heroku_config.sh /app/heroku_config.sh
# RUN chmod +x /app/heroku_config.sh && /app/heroku_config.sh

# Comando para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "tu_app.py"]
