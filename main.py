import flask

app = flask.Flask(__name__, static_url_path='/static')


@app.route('/', methods =["GET", "POST"])
def index():
    if flask.request.method == "POST":
        link = flask.request.form.get("link")


    return flask.render_template('index.html')



if __name__ == '__main__':
    app.run()


