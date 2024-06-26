from config import Settings
from flask import Flask, request, make_response
from json import dumps, loads
from os import environ
from prometheus_flask_exporter import PrometheusMetrics
import requests
from io import BytesIO

from controllers.computer_vision_controller import computer_vision_bp

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['CORS_HEADERS'] = 'Content-Type'
FRONTEND_HOST = environ["FRONTEND_HOST"] if environ.get("FRONTEND_HOST") else "localhost:5002"
MODEL_HOST = environ["MODEL_HOST"] if environ.get("MODEL_HOST") else "localhost:5001"
USE_HTTPS = environ["USE_HTTPS"] if environ.get("USE_HTTPS") else False

settings = Settings().setup(MODEL_HOST=f"https://{MODEL_HOST}")
app.register_blueprint(computer_vision_bp, url_prefix="/api")


@app.route("/api/healthz", methods=["GET"])
def healthz():
    return "Healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
