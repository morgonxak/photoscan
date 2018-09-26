import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import config as conf
from modulSettings import Settings

pathFileSettings = 'app\settings'

app = Flask(__name__)
settings_obj = Settings(pathFileSettings)
settings = settings_obj.getSettings()

app.config['ID'] = settings['ID']
print('Последний Id пользователя = ', settings['ID'])
app.config['settings_obj'] = settings_obj

app.config['UPLOAD_FOLDER'] = conf.UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = conf.ALLOWED_EXTENSIONS
from app import views

