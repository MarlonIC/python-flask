from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route('/start')
def start():
    return url_for('start', next="login")


@app.route('/google')
def go_to_google():
    return redirect('http://www.google.com')


@app.route('/posts/<int:id>')
def posts(id):
    return 'Show posts: {}'.format(id)


@app.route('/today')
def today():
    return redirect(url_for('posts', id=55, next="edit"))


if __name__ == '__main__':
    app.run(debug=True)