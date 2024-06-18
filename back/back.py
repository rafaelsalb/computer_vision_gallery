from flask import Flask, request, make_response
import flask_cors
from json import dumps, loads
import requests
from PIL import Image

app = Flask(__name__)
cors = flask_cors.CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/evaluate", methods=["POST"])
# @flask_cors.cross_origin(origins="http://localhost:8000")
def evaluate():
    image = request.files.get('image', '')
    # image_pil = Image.open(image)
    # res = model.evaluate(image_pil)
    prediction = requests.post("http://localhost:5000", files=image)
    res = prediction.json()
    digit = res["digit"]
    confidence = res["confidence"]
    resp = make_response({
        "result": dumps({
            "digit": digit,
            "confidence": confidence
        })
    }, 200)
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:5002'
    return resp

@app.route("/healthz", methods=["GET"])
def healthz():
    return "Healthy"
