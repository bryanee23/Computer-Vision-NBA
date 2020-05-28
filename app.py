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



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'images' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['images']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # print(request.files.getlist('images'))
            for image in request.files.getlist('images'):
                image.filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            return redirect(request.url)

    return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=True,
                step2=True,
                step3=True
                )
        # elif request.form.get('unknown') == 'unknown':
        #     # pass # do something else
        #     return render_template(
        #         "index.html",
        #         text_output=textOutput[2],
        #         step1=False,
        #         step2=False,
        #         step3=True
        #         )
        # elif request.form.get('start') == 'start':
        #     # pass # do something else
        #     return render_template(
        #         "processing_images.html",
        #         text_output=textOutput[3]
        #         )
        # else:
        #     # pass # unknown
        #     return render_template("index.html")






if __name__ == "__main__":
    app.run()