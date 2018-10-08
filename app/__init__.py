import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import config as conf
from modulSettings import Settings
from app.workWithPhotos import workPhotos
from app import Server as PhotoscanServer

host = 'localhost'
port = 777
addr = (host, port)

pathFileSettings = 'app\settings'
pachTempImage = r'app\static\images'
pachDirWork = r'processing_photoscan'

app = Flask(__name__)
##Класс с работай с фотографиями
wphotos = workPhotos(pachTempImage, pachDirWork)

##Класс с настройками
settings_obj = Settings(pathFileSettings)
settings = settings_obj.getSettings()
##

def stastServerPhotoscan(addr):
    test = PhotoscanServer.socketServer(addr)
    test.runServer()
    print("Сервер запушен")
    return test

#app.config['test'] = stastServerPhotoscan(addr)

app.config['ID'] = settings['ID']
print('Последний Id пользователя = ', settings['ID'])
app.config['settings_obj'] = settings_obj
app.config['workPhotos'] = wphotos

app.config['UPLOAD_FOLDER'] = conf.UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = conf.ALLOWED_EXTENSIONS
from app import views

