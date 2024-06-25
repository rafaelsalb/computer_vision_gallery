from typing import Tuple
from config import Settings
from dtos.input.evaluate_dto import EvaluateDTO
import json
import requests

from dtos.output.evaluation_dto import EvaluationDTO


class ComputerVisionService:
    @staticmethod
    def general_purpose(data: EvaluateDTO) -> Tuple[EvaluationDTO, int]:
        evaluation = requests.post(
            f"{Settings().MODEL_HOST}/detect",
            json = {
                "image": data.image
            }
        )
        evaluation_result = json.loads(evaluation.content)
        res = EvaluationDTO(evaluation_result)
        return res, 200
