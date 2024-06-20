import flask
from backend import img

app = flask.Flask(__name__, static_url_path='/static')

@app.route('/', methods =["GET", "POST"])
def index():
    return flask.render_template('index.html', qr = img)


if __name__ == '__main__':
    app.run()


