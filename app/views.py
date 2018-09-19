import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import app
import logging as log

log.basicConfig(filename="LOG_Server.log", level=log.INFO)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print("Имя:", request.form['user'])
        print("Почта:", request.form['mail'])

        listFile = request.files.getlist("file")
        log.info("Добовления изображения количества: "+str(len(listFile)))
        for file in listFile:
            log.info("Имя: "+str(file))

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))

    return render_template("index.html")

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)