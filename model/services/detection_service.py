from typing import Tuple
from dtos.input.image_dto import ImageDTO
from dtos.input.stream_image_dto import StreamImageDTO
from dtos.output.evaluation_dto import EvaluationDTO
from models import GeneralPurpose


class DetectionService:
    model: GeneralPurpose = GeneralPurpose()
    
    def detect(self, request_image: ImageDTO | StreamImageDTO) -> Tuple[EvaluationDTO, int]:
        result, image = self.model.evaluate(request_image.image)
        response: EvaluationDTO = EvaluationDTO(result, image)
        return response, 200

    def stream_detect(self, message_image: StreamImageDTO) -> EvaluationDTO:
        results, image = self.model.evaluate(message_image.image)
        result = EvaluationDTO(results, image)
        return result
