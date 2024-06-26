from base64 import b64encode
from flask import Request
from io import BytesIO
from PIL import Image


class EvaluateDTO:
    def __init__(self, image: str, model: str):
        self.image = image
        self.model = model
    
    @staticmethod
    def from_request(request: Request):
        image = Image.open(request.files.get("image")).convert("RGB")
        b, g, r = image.split()
        image = Image.merge("RGB", (r, g, b))
        image_bin = BytesIO()
        image.save(image_bin, format="JPEG")
        image_b64 = b64encode(image_bin.getvalue()).decode("utf-8")

        model = request.args.get("model")
        return EvaluateDTO(image_b64, model) # type: ignore
