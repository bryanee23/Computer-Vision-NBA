import os
from flask import Flask, flash, render_template, Response, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = os.urandom(24)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_images(request, element_tag, save_location):
    UPLOAD_FOLDER = (f"/Users/bryanevangelista/Documents/projects/flask-site/static/images/{save_location}")

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if request.method == 'POST':
        if element_tag not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files[element_tag]

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

# if / found, create new dir, return newdir, new location of image.save

        if file and allowed_file(file.filename):
            create_new_DIR(file, UPLOAD_FOLDER)
            # for image in request.files.getlist(element_tag):
            #     image.filename = secure_filename(image.filename)
            #     image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            return redirect(request.url)

def create_new_DIR(name, project_dir):
    name = name.filename.split("/")
    new_dir = name[0]
    path = (f"{project_dir}/{new_dir}")
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)
