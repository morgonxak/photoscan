import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
#import config as conf
#from modulSettings import Settings
from app.workWithPhotos import workPhotos
from app.workWithDataBase import DBManager

#Константы
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG'])
SettingsPC = 'PC1'

#Открытия базы данных
DBObject = DBManager(r'C:\projectTree\database.db', SettingsPC)

settings = DBObject.getSettings()

##Класс с работай с фотографиями
wphotos = workPhotos(settings[0][0], settings[0][1])


app = Flask(__name__)
app.config['ID'] = settings[0][2]
print('Последний Id пользователя = ', settings[0][2])
app.config['DBObject'] = DBObject
app.config['workPhotos'] = wphotos


app.config['UPLOAD_FOLDER'] = settings[0][0]
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

from app import views

