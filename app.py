import os
from flask import Flask, flash, render_template, Response, request, redirect, url_for
from uploads import upload_images
from empty_folders import reset_all
from stats import get_API_info
from directory import *
from img_slider import img_slider
# from recognition import MATCHES_DIR, resize_images,load_known_person,initate_recognition

app = Flask(__name__)
app.secret_key = os.urandom(24)


textOutput = {
    0 : "Go to Step 1",
    1 : "Known person loaded, proceed to Step 2",
    2 : "Verification images loaded, proceed to Step 3",
    3 : "Processing...",
    4 : (f"Matches Found: {len(os.listdir(MATCHES_DIR))}")
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if request.form.get('known') == 'known' or request.form.get('add_unknowns') == 'add_unknowns':
            upload_images(request, 'known', 'known')
            # load_known_person()
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
            upload_images(request, 'unknown', 'uploads')
            # resize_images()
            # delete_folder_contents("uploads")
            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=False,
                step2=False,
                step3=True,
                )


        elif request.form.get('start') == 'start':
            stats=get_API_info("Stephen Curry")
            current_image = os.listdir(MATCHES_DIR)
            return render_template(
                "index.html",
                text_output=textOutput[4],
                current_image=current_image[0],
                start=True,
                stats=stats
                )

        elif request.form.get('next') == 'next':
            stats=get_API_info("Stephen Curry")
            current_image = img_slider("next")

            return render_template(
                "index.html",
                text_output=textOutput[4],
                current_image=current_image,
                start=True,
                stats=stats
                )

        elif request.form.get('prev') == 'prev':
            stats=get_API_info("Stephen Curry")
            current_image = img_slider("prev")

            return render_template(
                "index.html",
                text_output=textOutput[4],
                current_image=current_image,
                start=True,
                stats=stats
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