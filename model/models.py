from ultralytics import YOLO
import os
from pathlib import Path
import PIL
from io import BytesIO
from base64 import b64encode

class Model:
    def __init__(self, model: int, mode: str = "classify"):
        BASE_DIR = Path(os.path.abspath(__file__)).resolve().parents[0]
        try:
            self.model = YOLO(os.path.join(BASE_DIR, f"{model}.pt"))
        except FileNotFoundError:
            print("The weights file was not found.")
            quit(keep_kernel=True)

    def evaluate(self, image: PIL.Image):
        res = self.model.predict(image)
        return res[0].tojson()

class DigitClassifier(Model):
    def __init__(self):
        super().__init__("digit_classification")

class GeneralPurpose(Model):
    def __init__(self):
        super().__init__("general_purpose")

    def evaluate(self, image: PIL.Image):
        res = self.model.predict(image)
        annotated_image = PIL.Image.fromarray(res[0].plot())
        im = BytesIO()
        annotated_image.save(im, format="JPEG")
        img_str = b64encode(im.getvalue()).decode('utf-8')
        return (res[0].tojson(), img_str)
