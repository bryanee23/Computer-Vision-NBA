import os
from flask import Flask, flash, render_template, Response, request, redirect, url_for
from test import get_stats
from uploads import upload_images

app = Flask(__name__)
app.secret_key = os.urandom(24)

textOutput = {
    0 : "Go to Step 1",
    1 : "Known person loaded, proceed to Step 2",
    2 : "Verification images loaded, proceed to Step 3",
    3 : "Processing started see results below:",
}

test=get_stats()
@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.method)
    if request.method == 'POST':

        if request.form.get('known') == 'known':
            # print(request.files['known'])
            upload_images(request, 'known', 'known')

            return render_template(
                "index.html",
                text_output=textOutput[1],
                step1=False,
                step2=True,
                step3=False,
                )

        elif request.form.get('unknown') == 'unknown':

            upload_images(request, 'unknown', 'test')
            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=False,
                step2=False,
                step3=True
                )

        elif request.form.get('more') == 'more':

            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=True,
                step2=False,
                step3=False
                )

        elif request.form.get('start') == 'start':

            return render_template(
                "processing_images.html",
                text_output=textOutput[3]
                )
        else:
            return render_template("index.html")

    else:

        return render_template(
            "index.html",
            step1=True,
            text_output=textOutput[0],
            )

if __name__ == "__main__":
    app.run()