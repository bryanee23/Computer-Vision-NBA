import os
from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24)

# directory setup, opencv border settings
ROOT_DIR = os.getcwd()
KNOWN_FACES_DIR = (f"{ROOT_DIR}/static/images/known")
UNKNOWN_FACES_DIR = (f"{ROOT_DIR}/static/images/unknown")
MATCHES_DIR = (f"{ROOT_DIR}/static/images/matches")
UPLOADED_IMAGES_DIR = (f"{ROOT_DIR}/static/images/uploads")
