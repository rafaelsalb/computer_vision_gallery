FROM python:3.12.3
ARG FRONTEND_HOST
ARG API_HOST
ARG MODEL_HOST
ENV FRONTEND_HOST=${FRONTEND_HOST}
ENV API_HOST=${API_HOST}
ENV MODEL_HOST=${MODEL_HOST}
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
COPY . .
EXPOSE 5000:5000
CMD [ "python3", "-u", "api.py" ]
