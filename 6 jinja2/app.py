from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Home'
    lista = ["footer", "header", "info"]
    return render_template('index.html', title=title, lista=lista)


if __name__ == "__main__":
    app.run(debug=True)
