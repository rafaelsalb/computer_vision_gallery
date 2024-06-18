from flask import Flask, request, make_response
from digits import Model
from PIL import Image

model = Model(-1)
app = Flask(__name__)

@app.route("/classify")
def classify():
    image = request.files.get('image', '')
    image_pil = Image.open(image)
    classification = model.evaluate(image_pil)
    digit = classification['name']
    confidence = classification['confidence']
    res = make_response({
        "digit": digit,
        "confidence": confidence
    }, 200)
    res.headers['Access-Control-Allow-Origin'] = 'http://localhost:5001'
    return res

if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000)

