FROM python:3.12.3-alpine3.20 as build
ARG FRONTEND_HOST
ARG API_HOST
ARG MODEL_HOST
ENV FRONTEND_HOST=${FRONTEND_HOST}
ENV API_HOST=${API_HOST}
ENV MODEL_HOST=${MODEL_HOST}
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "-u", "front.py" ]
