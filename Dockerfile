# Usa una imagen basada en Python 2.7
FROM python:2.7

# Establece las variables de entorno
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y supervisor

# Copia todo el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . /app/

COPY config/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]