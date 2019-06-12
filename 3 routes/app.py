from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/user/<string:username>')
def user(username):
    return 'Hello ' + username


@app.route('/number/<int:n>')
def number(n):
    return 'Number: {}'.format(n)


@app.route('/user/<int:id>/<string:username>')
def user_name(id, username):
    return 'Id: {} and User name: {}'.format(id, username)


@app.route('/sum/<float:n1>/<float:n2>')
def sum(n1, n2):
    return "N1: {}, N2: {}, Sum: {}".format(n1, n2, n1 + n2)


@app.route('/default/')
@app.route('/default/<string:dft>')
def default(dft='default'):
    return 'The value of dft is: ' + dft


if __name__ == "__main__":
    app.run(debug=True)
