from flask import Blueprint, Response, make_response, request

from dtos.input.image_dto import ImageDTO
from dtos.output.evaluation_dto import EvaluationDTO
from services.detection_service import DetectionService

object_detection_controller = Blueprint('object_detection', __name__)

detection_service = DetectionService()

@object_detection_controller.route("/detect", methods=["POST"])
def detect():
    request_image: ImageDTO = ImageDTO.from_request(request)
    response, status_code = detection_service.detect(request_image)
    res: Response = make_response(
        response.to_dict(),
        status_code,
    )
    res.headers['Access-Control-Allow-Origin'] = f"*"
    return res
