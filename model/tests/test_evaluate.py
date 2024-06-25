import os.path
from pathlib import Path
import sys
from PIL import Image
from json import loads

BASE_DIR = Path(os.path.abspath(__file__)).parent
sys.path.append(os.path.join(BASE_DIR, "../"))
from models import GeneralPurpose
from dtos.input.image_dto import ImageDTO 
from api import app

general_purpose = GeneralPurpose()

def test_evaluate():
    global general_purpose
    image = ImageDTO(
        Image.open(os.path.join(BASE_DIR, "escritorio.jpeg"))
    )
    result, image = general_purpose.evaluate(image.image)
    result_list = loads(result)
    print(result_list)
    assert isinstance(image, str)
    assert "name" in result_list[0]
    assert "confidence" in result_list[0]
