import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
import logging as log
import json

log.basicConfig(filename="LOG_Server.log", level=log.INFO)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def serverFotoScan(UserID):

    dictParameters = dict()
    dictParameters['ID_User'] = UserID

    # Отправляем команду на запуск с параметрами
    app.config['test'].run(dictParameters)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        infoUser = {}
        infoUser['name'] = request.form['user']
        infoUser['mail'] = request.form['mail']

        listFile = request.files.getlist("file")
        log.info("Добовления изображения количества: "+str(len(listFile)))
        infoUser['lenPhoto'] = len(listFile)

        app.config['ID'] = app.config['ID'] + 1
        app.config['DBObject'].editUserId(app.config['ID'])

        ##Создаем рабочую дирикторию и перемещяем туда фотографии
        app.config['workPhotos'].creatDir('ID_' + str(app.config['ID']))
        app.config['DBObject'].pullData('treatment', [(app.config['ID'], 'Server', 'CreatDirProject', True)])

        for file in listFile:
            log.info("Имя: "+str(file))
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        app.config['workPhotos'].movePhoto('ID_' + str(app.config['ID']))
        app.config['DBObject'].pullData('treatment', [(app.config['ID'], 'Server', 'DowloadPhoto', True)])


        pullInfoUser = json.dumps(infoUser)

        return redirect(url_for('infoUser', infoUser=pullInfoUser))

    return render_template("index.html")


@app.route('/info/<infoUser>')
def infoUser(infoUser):
    infoUser = json.loads(infoUser)
    return render_template("info.html", User_ID=app.config['ID'], infoUser=infoUser)