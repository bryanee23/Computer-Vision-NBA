import os
from flask import Flask, flash, render_template, Response, request, redirect, url_for
from uploads import upload_images
from empty_folders import reset_all, delete_folder_contents, delete_cache
from api_call import get_API_info
from directory import *
from img_slider import *
from runtime import *
from recognition import resize_images,initate_recognition


app = Flask(__name__)
app.secret_key = os.urandom(24)



def reload_server():
    f = open("runtime.py", "a")
    f.write("here")
    f.close()


match_list = os.listdir(MATCHES_DIR)
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
            resize_images()
            initate_recognition()
            print('list', match_list)
            reload_server()
            print('reload server', match_list)

            return render_template(
                "index.html",
                text_output=textOutput[2],
                step1=False,
                step2=False,
                step3=True,
                )

        elif request.form.get('start') == 'start':
            delete_folder_contents("uploads")
            print('list', match_list)
            current_image = match_list[image_slider(1)]

            stats=get_API_info(current_image)
            redirect(request.url) ##do I need this?##
            return render_template(
                "index.html",
                text_output=textOutput[4],
                current_image=current_image,
                start=True,
                stats=stats
                )

        elif request.form.get('next') == 'next':

            current_image = match_list[image_slider(1)]


            stats=get_API_info(current_image)
            return render_template(
                "index.html",
                text_output=textOutput[4],
                current_image=current_image,
                start=True,
                stats=stats
                )

        elif request.form.get('prev') == 'prev':

            current_image = match_list[image_slider(-1)]
            stats=get_API_info(current_image)

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


# if __name__ == "__main__":
#     app.run()
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()