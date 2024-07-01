import base64
from io import BytesIO
from PIL import Image

class StreamImageDTO:
    image: Image.Image

    def __init__(self, image: Image.Image) -> None:
        self.image = image

    @staticmethod
    def from_request(image_str: str):
        image_data: bytes = base64.b64decode(image_str)
        image_buffer: BytesIO = BytesIO(image_data)
        image: Image.Image = Image.open(image_buffer)
        b, g, r = image.split()
        image = Image.merge("RGB", (r, g, b))
        return StreamImageDTO(image)
