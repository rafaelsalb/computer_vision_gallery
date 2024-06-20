FROM python:3.12.3-alpine3.20
ENV FRONTEND_ADDRESS=http://172.22.85.110:5002
ENV MODEL_ADDRESS=http://172.22.85.110:5000
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5001:5001
CMD [ "python3", "-u", "back.py" ]
