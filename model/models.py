from typing import Tuple
from ultralytics import YOLO
import os
from pathlib import Path
from PIL import Image
from io import BytesIO
from base64 import b64encode

class Model:
    def __init__(self, model: str):
        BASE_DIR = Path(os.path.abspath(__file__)).resolve().parents[0]
        try:
            self.model = YOLO(os.path.join(BASE_DIR, f"{model}.pt"))
        except FileNotFoundError:
            print("The weights file was not found.")
            quit()

    def evaluate(self, image: Image.Image):
        res = self.model.predict(image) # type: ignore
        return res[0].tojson()

class DigitClassifier(Model):
    def __init__(self):
        super().__init__("digit_classification")

class GeneralPurpose(Model):
    def __init__(self):
        super().__init__("general_purpose")

    def evaluate(self, image: Image.Image) -> Tuple[str, str]:
        res = self.model(image) # type: ignore
        annotated_image = Image.fromarray(res[0].plot()) # .convert("RGB")
        im = BytesIO()
        annotated_image.save(im, format="JPEG")
        img_str = b64encode(im.getvalue()).decode('utf-8')
        return (res[0].tojson(), img_str)

class Segmentation(Model):
    def __init__(self):
        super().__init__("yolov8n-seg")

    def evaluate(self, image: Image.Image) -> Tuple[str, str]:
        res = self.model(image) # type: ignore
        annotated_image = Image.fromarray(res[0].plot()) # .convert("RGB")
        im = BytesIO()
        annotated_image.save(im, format="JPEG")
        img_str = b64encode(im.getvalue()).decode('utf-8')
        return (res[0].tojson(), img_str)

