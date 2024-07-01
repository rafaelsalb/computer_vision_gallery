from flask import Blueprint, Response, make_response, request
from flask_socketio import SocketIO, emit, send
import logging
from threading import Thread

from dtos.input.image_dto import ImageDTO
from dtos.input.stream_image_dto import StreamImageDTO
from dtos.output.evaluation_dto import EvaluationDTO
from services.detection_service import DetectionService

logger = logging.getLogger("logs")

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

def register_socketio_events(socketio: SocketIO):
    @socketio.on("connect")
    def connect():
        print("connected!")
        send("connected!")

    @socketio.on("disconnect")
    def disconnect():
        print("disconnected!")
        send("disconnected!")

    @socketio.on("frame")
    def handle_frame(data):
        frame_data: StreamImageDTO = StreamImageDTO.from_request(data)
        # thread = Thread(target=process_frame, args=(frame_data,))
        # thread.start()
        res: EvaluationDTO = detection_service.stream_detect(frame_data)
        send(res.image)

    def process_frame(data: StreamImageDTO):
        res: EvaluationDTO = detection_service.stream_detect(data)
        send(res.image)
