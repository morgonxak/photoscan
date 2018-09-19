import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import config as conf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = conf.UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = conf.ALLOWED_EXTENSIONS
from app import views