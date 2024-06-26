from flask import Flask, render_template
import os

app = Flask(__name__)
BACKEND_HOST = os.environ["BACKEND_HOST"] if os.environ.get("BACKEND_HOST") else "localhost:5001"

@app.route("/digits", methods=["GET"])
def digits():
    return render_template("digits.html")

@app.route("/general_purpose", methods=["GET"])
def general_purpose():
    return render_template("detect_webcam.html", api_host=BACKEND_HOST)

@app.route("/segment", methods=["GET"])
def segment():
    return render_template("segment_webcam.html", api_host=BACKEND_HOST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
