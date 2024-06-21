from flask import Flask, render_template
import os

app = Flask(__name__)
BACKEND_HOST = os.environ["BACKEND_HOST"] if os.environ.get("BACKEND_HOST") else "localhost:5001"

@app.route("/digits", methods=["GET"])
def digits():
    return render_template("digits.html")

@app.route("/general_purpose", methods=["GET"])
def general_purpose():
    return render_template("webcam.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
