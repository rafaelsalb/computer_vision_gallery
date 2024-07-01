from typing import Tuple
from dtos.input.image_dto import ImageDTO
from dtos.input.stream_image_dto import StreamImageDTO
from dtos.output.evaluation_dto import EvaluationDTO
from models import Segmentation


class SegmentationService:
    model: Segmentation

    def __init__(self) -> None:
        self.model = Segmentation()

    def segment(self, request_image: ImageDTO | StreamImageDTO) -> Tuple[EvaluationDTO, int]:
        result, image = self.model.evaluate(request_image.image)
        response: EvaluationDTO = EvaluationDTO(result, image)
        return response, 200
