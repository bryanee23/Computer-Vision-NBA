import os
from flask import Flask, flash, render_template, Response, request, redirect, url_for
from uploads import upload_images
from empty_folders import reset_all
from stats import get_API_info

print(get_API_info("Stephen Curry"))

app = Flask(__name__)
app.secret_key = os.urandom(24)

textOutput = {
    0 : "Go to Step 1",
    1 : "Known person loaded, proceed to Step 2",
    2 : "Verification images loaded, proceed to Step 3",
    3 : "Processing...",
}


MATCHES_DIR = (f"/Users/bryanevangelista/Documents/projects/flask-site/static/images/matches")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if request.form.get('known') == 'known' or request.form.get('add_unknowns') == 'add_unknowns':
            upload_images(request, 'known', 'known')
            return render_template(
                "index.html",
                text_output=textOutput[1],
                step1=False,
                step2=True,
                step3=False,
                )

        elif request.form.get('add_knowns') == 'add_knowns':
            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=True,
                step2=False,
                step3=False
                )

        elif request.form.get('unknown') == 'unknown':
            upload_images(request, 'unknown', 'unknown')
            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=False,
                step2=False,
                step3=True,
                )

        elif request.form.get('start') == 'start' or request.form.get('next') == 'next':
            current_image = os.listdir(MATCHES_DIR)
            return render_template(
                "index.html",
                text_output=textOutput[3],
                current_image=current_image[0],
                start=True
                )

        elif request.form.get('reset') == 'reset':
            reset_all()
            return render_template(
                "index.html",
                text_output=textOutput[0],
                step1=True
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