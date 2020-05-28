import os
from flask import Flask, render_template, Response, request, redirect, url_for
from werkzeug.utils import secure_filename
from test import get_stats
app = Flask(__name__)


UPLOAD_FOLDER = '/Users/bryanevangelista/Documents/projects/flask-site/test'





textOutput = {
    0 : "Proceed with Step 1",
    1 : "loading images",
    2 : "loading unknown images",
    3 : "processing started see below for results",
}

test=get_stats()


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_images(request):
    if request.method == 'POST':
        print(request.files.getlist('images'))
        if 'images' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['images']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):

            for image in request.files.getlist('images'):
                image.filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            return redirect(request.url)


@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.method)
    if request.method == 'POST':
        if request.form.get('known') == 'known':
            upload_images(request)
            return render_template(
                "index.html",
                text_output=textOutput[1],
                step1=False,
                step2=True,
                step3=False,
                )
        elif request.form.get('unknown') == 'unknown':
            upload_images(request)
            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=False,
                step2=False,
                step3=True
                )
        elif request.form.get('start') == 'start':
            # pass # do something else
            return render_template(
                "processing_images.html",
                text_output=textOutput[3]
                )
        else:
            # pass # unknown
            return render_template("index.html")
    else:
    # return render_template("index.html")
        return render_template(
            "index.html",
            step1=True,
            text_output=textOutput[0],
            )






if __name__ == "__main__":
    app.run()