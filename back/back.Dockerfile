FROM python:3.12.3-alpine3.20
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5001:5001
CMD [ "flask", "--app back", "--host 0.0.0.0", "--port 5001" ]
