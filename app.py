from flask import Flask, render_template, Response, request, redirect, url_for
from test import get_stats

app = Flask(__name__)


test=get_stats()
@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.method)
    if request.method == 'POST':
        if request.form.get('known') == 'known':
            return render_template("index.html", test=test)
        elif request.form.get('unknown') == 'unknown':
            # pass # do something else
            return render_template("index.html", test="unknown hit")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
    # return render_template("index.html")
        return render_template("index.html")





if __name__ == "__main__":
    app.run()