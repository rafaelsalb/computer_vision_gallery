from flask import Flask, request, make_response
from json import dumps, loads
from os import environ
from PIL import Image
from prometheus_flask_exporter import PrometheusMetrics
import requests

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['CORS_HEADERS'] = 'Content-Type'
FRONTEND_HOST = environ["FRONTEND_HOST"] if environ.get("FRONTEND_HOST") else "localhost:5002"
MODEL_HOST = environ["MODEL_HOST"] if environ.get("MODEL_HOST") else "localhost:5001"
USE_HTTPS = environ["USE_HTTPS"] if environ.get("USE_HTTPS") else False

def target_url(host: str, path: str = ""):
    global USE_HTTPS
    return f"{"https" if USE_HTTPS else "http"}://{host}{path}"

@app.route("/evaluate", methods=["POST"])
def evaluate():
    model = request.args.get("model")
    print(request.args, model)
    match model:
        case "digits":
            evaluation = digits_classification(request)
        case "general_purpose":
            evaluation = general_purpose(request)
        case _:
            res = make_response({"message": "Model not found."}, 404)
            res.headers['Access-Control-Allow-Origin'] = target_url(FRONTEND_HOST)
            return res
    res = make_response({
        "result": evaluation
    }, 200)
    res.headers['Access-Control-Allow-Origin'] = f"*"
    return res

@app.route("/healthz", methods=["GET"])
def healthz():
    return "Healthy"

def digits_classification(request):
    image = request.files['image']
    prediction = requests.post(target_url(MODEL_HOST, "/classify"), files={'image': (image.filename, image.stream, image.mimetype)})
    res = loads(prediction.content)[0]
    digit = res["name"]
    confidence = res["confidence"]
    return dumps({
        "digit": digit,
        "confidence": confidence
    })

def general_purpose(request):
    image = request.files['image']
    prediction = requests.post(target_url(MODEL_HOST, "/detect"), files={'image': (image.filename, image.stream, image.mimetype)})
    res = loads(prediction.content)
    names = [i["name"] for i in res]
    confidences = [i["confidence"] for i in res]
    image_str = [i["image"] for i in res]
    return dumps({
        "names": names,
        "confidences": confidences,
        "images": image_str
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
