from flask import Flask, request, make_response
from json import dumps, loads
from os import environ
from PIL import Image
from prometheus_flask_exporter import PrometheusMetrics
import requests

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['CORS_HEADERS'] = 'Content-Type'
FRONTEND_ADDRESS = environ["FRONTEND_ADDRESS"]
MODEL_ADDRESS = environ["MODEL_ADDRESS"]

@app.route("/evaluate", methods=["POST"])
# @flask_cors.cross_origin(origins="http://localhost:8000")
def evaluate():
    global metrics
    image = request.files['image']
    # res = model.evaluate(image_pil)
    prediction = requests.post("http://172.22.85.110:5000" + "/classify", files={'image': (image.filename, image.stream, image.mimetype)})
    print(prediction.content)
    res = loads(prediction.content)[0]
    print(res)
    digit = res["name"]
    confidence = res["confidence"]
    resp = make_response({
        "result": dumps({
            "digit": digit,
            "confidence": confidence
        })
    }, 200)
    resp.headers['Access-Control-Allow-Origin'] = FRONTEND_ADDRESS
    return resp

@app.route("/healthz", methods=["GET"])
def healthz():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

