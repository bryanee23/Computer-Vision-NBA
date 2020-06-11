import os
from flask import Flask, flash, render_template, Response, request, redirect, url_for
from uploads import upload_images
from empty_folders import reset_all, delete_folder_contents
from api_call import get_stats
from directory import *
from img_slider import *
from reload_server import reload_server
from recognition import run_face_recognition_script


app = Flask(__name__)
app.secret_key = os.urandom(24)


match_list = os.listdir(MATCHES_DIR)
textOutput = {
    0 : "Directions:  see step 1",
    1 : "Directions:  (images loaded) proceed to step 2",
    2 : "Directions:  (images loaded), see results below",
    3 : "Processing...",
    4 : (f"Matches Found: {len(os.listdir(MATCHES_DIR))}")
}


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

            upload_images(request, 'unknown', 'uploads')
            run_face_recognition_script()
            reload_server()

            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=False,
                step2=False,
                step3=True,
                )

        elif request.form.get('start') == 'start':

            delete_folder_contents("uploads")
            current_image = match_list[0]
            stats=get_stats(current_image)

            return render_template(
                "index.html",
                results=textOutput[4],
                text_output=" ",
                current_image=current_image,
                start=True,
                stats=stats
                )

        elif request.form.get('next') == 'next':

            current_image = match_list[image_slider(1)]
            stats=get_stats(current_image)

            return render_template(
                "index.html",
                results=textOutput[4],
                text_output=" ",
                current_image=current_image,
                start=True,
                stats=stats
                )

        elif request.form.get('prev') == 'prev':

            current_image = match_list[image_slider(-1)]
            stats=get_stats(current_image)

            return render_template(
                "index.html",
                results=textOutput[4],
                text_output=" ",
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


# if __name__ == "__main__":
#     app.run()
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()