# coding=utf-8
import os
import sys

import jsonpickle
from flask import Flask, request, redirect, url_for
from flask import render_template, send_from_directory
from werkzeug.utils import secure_filename

from recognizer.card_recognition import recognize_contact

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
path = os.path.dirname(os.path.abspath(__file__))


@app.route("/status")
def hello():
    return render_template('hello.html', messages=['Hello world', 'Your message'])


@app.route("/info")
def view_info():
    return render_template('card.html', filename='r_1.jpg', info='Just dumy information')


@app.route('/get/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/files/<path:path>')
def static_proxy(path):
  return app.send_static_file('uploads/' + path)


@app.route('/view/<filename>', methods=['GET'])
def uploaded_file(filename):
    file_path = (path + '/uploads/%s') % filename
    contact_info = recognize_contact(file_path)
    print jsonpickle.encode(contact_info)
    return render_template('card.html', filename=filename, info=contact_info)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print 'No file part'
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print 'No selected file'
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run()
