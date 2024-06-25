import base64
from io import BytesIO
from PIL import Image
from flask import Request

class ImageDTO:
    image: Image.Image

    def __init__(self, image: Image.Image) -> None:
        self.image = image

    @staticmethod
    def from_request(request: Request):
        image: str = request.json["image"] # type: ignore
        return ImageDTO(Image.open(BytesIO(base64.b64decode(image))))
