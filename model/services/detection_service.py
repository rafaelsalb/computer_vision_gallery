from typing import Tuple
from dtos.input.image_dto import ImageDTO
from dtos.output.evaluation_dto import EvaluationDTO
from models import GeneralPurpose


class DetectionService:
    model: GeneralPurpose = GeneralPurpose()
    
    def detect(self, request_image: ImageDTO) -> Tuple[EvaluationDTO, int]:
        result, image = self.model.evaluate(request_image.image)
        response: EvaluationDTO = EvaluationDTO(result, image)
        return response, 200
