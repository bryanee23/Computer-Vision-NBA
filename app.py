from flask import Flask, render_template, Response, request, redirect, url_for
from test import get_stats

app = Flask(__name__)

textOutput = {
    0 : "Proceed with Step 1",
    1 : "loading images",
    2 : "loading unknown images",
    3 : "processing started see below for results",
}

test=get_stats()
@app.route('/', methods=['GET', 'POST'])

def index():
    # print(request.method)
    if request.method == 'POST':
        if request.form.get('known') == 'known':
            return render_template(
                "index.html",
                text_output=textOutput[1],
                step1=False,
                step2=True,
                step3=False,
                )
        elif request.form.get('unknown') == 'unknown':
            # pass # do something else
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