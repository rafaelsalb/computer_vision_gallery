from flask import Flask, render_template, request, make_response
from flask_socketio import SocketIO, send
import logging
from os import environ

from controllers.detection_controller import object_detection_controller, register_socketio_events
from controllers.segmentation_controller import segmentation_controller

logger = logging.getLogger("logs")
logging.basicConfig(
    filename="logs",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO
)

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

BACKEND_HOST = environ["BACKEND_HOST"] if environ.get("BACKEND_HOST") else "localhost:5001"
USE_HTTPS = environ["USE_HTTPS"] if environ.get("USE_HTTPS") else False

app.register_blueprint(object_detection_controller, url_prefix="/model")
app.register_blueprint(segmentation_controller, url_prefix="/model")

@app.route("/model/logs")
def logs():
    f = open("logs", "r")
    _logs = f.readlines()
    f.close()
    return render_template("logs.html", logs=_logs)

if __name__ == "__main__":
    register_socketio_events(socketio)
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True) # type: ignore
