from flask import Blueprint, Response, make_response, request

from dtos.input.evaluate_dto import EvaluateDTO
from services.computer_vision_service import ComputerVisionService

computer_vision_bp = Blueprint('computer_vision', __name__)

@computer_vision_bp.route("/evaluate/detect", methods=["POST"])
def evaluate() -> Response:
    evaluate_dto = EvaluateDTO.from_request(request)
    result, status_code = ComputerVisionService.general_purpose(evaluate_dto)
    res = make_response(result.to_dict(), status_code)
    res.headers['Access-Control-Allow-Origin'] = f"*"
    return res
