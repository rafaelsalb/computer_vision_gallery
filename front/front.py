from flask import Flask, render_template
import os

app = Flask(__name__)
BACKEND_HOST = os.environ["BACKEND_HOST"] if os.environ.get("BACKEND_HOST") else "localhost:5001"
MODEL_HOST =  os.environ["MODEL_HOST"] if os.environ.get("MODEL_HOST") else "localhost:5000"
USE_HTTPS = os.environ["USE_HTTPS"] if os.environ.get("USE_HTTPS") else False

@app.route("/digits", methods=["GET"])
def digits():
    return render_template("digits.html")

@app.route("/general_purpose", methods=["GET"])
def general_purpose():
    return render_template("detect_webcam.html", api_host=BACKEND_HOST, model_host=MODEL_HOST)

@app.route("/detect_stream", methods=["GET"])
def detect_stream():
    model_host = MODEL_HOST.split("/")[0]
    return render_template("detect_webcam_stream.html", api_host=BACKEND_HOST, model_host=model_host, use_https=True)

@app.route("/segment", methods=["GET"])
def segment():
    return render_template("segment_webcam.html", api_host=BACKEND_HOST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
