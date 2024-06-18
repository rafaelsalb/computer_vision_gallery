from ultralytics import YOLO
import os
from pathlib import Path
import PIL

class Model:
    def __init__(self, model: int, mode: str = "classify"):
        BASE_DIR = Path(os.path.abspath(__file__)).resolve().parents[0]
        try:
            self.model = YOLO(os.path.join(BASE_DIR, "best.pt"))
        except FileNotFoundError:
            print("The weights file was not found.")
            quit(keep_kernel=True)

    def evaluate(self, image: PIL.Image):
        res = self.model.predict(image)
        print(res[0].tojson())
        return res[0].tojson()
