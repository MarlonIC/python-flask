from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/cookie/set')
def set_cookie():
    resp = make_response(render_template('index.html'))
    resp.set_cookie("username", "marlon")

    return resp


@app.route('/cookie/get')
def get_cookie():
    username = request.cookies.get("username", None)

    if username is None:
        return 'The cookie does not exists'
    return username


if __name__ == '__main__':
    app.run(debug=True)
