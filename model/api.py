from digits import Model
from flask import Flask, request, make_response
from json import loads
from os import environ
from PIL import Image

model = Model(-1)
app = Flask(__name__)
API_ADDRESS = environ["API_ADDRESS"]

@app.route("/classify", methods=["POST"])
def classify():
    image = request.files['image']
    print(image)
    image_pil = Image.open(image)
    print(image)
    classification = model.evaluate(image_pil)
    print(classification)
    res_classification = loads(classification)
    print(res_classification)
    res = make_response(
        res_classification,
        200,
    )
    res.headers['Access-Control-Allow-Origin'] = API_ADDRESS
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

