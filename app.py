from flask import Flask, render_template, Response, request, redirect, url_for
from test import get_stats

app = Flask(__name__)

textOutput = {
    0 : "loading images",
    1 : "loading unknown images",
    2 : "processing started see below for results",
}

test=get_stats()
@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.method)
    if request.method == 'POST':
        if request.form.get('known') == 'known':
            return render_template(
                "index.html",
                text_output=textOutput[0]
                )
        elif request.form.get('unknown') == 'unknown':
            # pass # do something else
            return render_template(
                "index.html",
                text_output=textOutput[1]
                )
        elif request.form.get('start') == 'start':
            # pass # do something else
            return render_template(
                "processing_images.html",
                text_output=textOutput[2]
                )
        else:
            # pass # unknown
            return render_template("index.html")
    else:
    # return render_template("index.html")
        return render_template("index.html")





if __name__ == "__main__":
    app.run()