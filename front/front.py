from flask import Flask, send_file
import os
from pathlib import Path


BASE_DIR = Path(os.path.abspath(__file__)).resolve().parents[0]
app = Flask(__name__)
API_ADDRESS = os.environ["API_ADDRESS"]

page_path = os.path.join(BASE_DIR, "pages")

@app.route("/", methods=["GET"])
def index():
    return send_file(os.path.join(page_path, "index.html"), "text/html")
