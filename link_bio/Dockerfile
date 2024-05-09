#usa esta instancia de python
FROM python:3.11

#/app es el nombre que va a manejar (el directorio de trabajo) y copy . . es copiar todo        Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

#crear una variable virtual que se va a copiar al trabajo final y tengo que tener mapeado en el path el entorno virutal
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/Scripts:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

#instalar los requerimientos
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#lanzar el backend en entorno produccion, solo backend
CMD reflex run --env prod --backend-only

#USAR COMILLAS DOBLES