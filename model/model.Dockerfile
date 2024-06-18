FROM python:3.12.3
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
COPY . .
EXPOSE 5000:5000
CMD [ "python3", "api.py" ]
