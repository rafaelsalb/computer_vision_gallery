from flask import Flask, request, make_response
from json import loads
from models import DigitClassifier, GeneralPurpose
from os import environ
from PIL import Image
from controllers.detection_controller import object_detection_controller

digit_classifier = DigitClassifier()
general_purpose = GeneralPurpose()
app = Flask(__name__)

BACKEND_HOST = environ["BACKEND_HOST"] if environ.get("BACKEND_HOST") else "localhost:5001"
USE_HTTPS = environ["USE_HTTPS"] if environ.get("USE_HTTPS") else False

app.register_blueprint(object_detection_controller)

def target_url(host: str, path: str = ""):
    global USE_HTTPS
    return f"{"https" if USE_HTTPS else "http"}://{host}{path}"

@app.route("/classify", methods=["POST"])
def classify():
    image = request.files['image']
    image_pil = Image.open(image)
    classification = digit_classifier.evaluate(image_pil)
    res_classification = loads(classification)
    res = make_response(
        res_classification,
        200,
    )
    res.headers['Access-Control-Allow-Origin'] = f"*"
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
