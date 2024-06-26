import flask
import qrcode
import os

app = flask.Flask(__name__, static_url_path='/static')


@app.route('/', methods =["GET", "POST"])
def index():
    if flask.request.method == "POST":
        link = flask.request.form.get("link")
        img = qrcode.make(link)
        img.save("static\images\some_file.png")

    return flask.render_template('index.html')



if __name__ == '__main__':
    default_qr = "https://github.com/SamQxd"
    img = qrcode.make(default_qr)
    img.save("static\images\some_file.png")
    app.run()

