from flask import Blueprint, Response, make_response, request

from dtos.input.image_dto import ImageDTO
from dtos.output.evaluation_dto import EvaluationDTO
from services.segmentation_service import SegmentationService

segmentation_controller = Blueprint('segmentation_detection', __name__)

segmentation_service = SegmentationService()

@segmentation_controller.route("/segment", methods=["POST"])
def segment():
    request_image: ImageDTO = ImageDTO.from_request(request)
    response, status_code = segmentation_service.segment(request_image)
    res: Response = make_response(
        response.to_dict(),
        status_code,
    )
    res.headers['Access-Control-Allow-Origin'] = f"*"
    return res
