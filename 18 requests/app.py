from flask import Flask, jsonify, render_template
from requests import get


app = Flask(__name__)

cns_videos = [
    {
        "id": 1,
        "title": "1.- Hello World - Curso Flask"
    },
    {
        "id": 2,
        "title": "2.- Metodo run - Curso Flask"
    }
]
isc_videos = [
    {
        "id": 1,
        "title": "1.- Hello World - Curso Flask"
    },
    {
        "id": 2,
        "title": "2.- Metodo run - Curso Flask"
    }
]


@app.route('/')
def index():
    return 'Hello World'


@app.route('/api/v1/videos/')
def get_all_videos():
    return jsonify({"videos": {"cns": cns_videos, "isc": isc_videos}})


@app.route('/video')
def video():
    videos = get('http://localhost:5000/api/v1/videos').json()
    return render_template("video.html", videos=videos)


if __name__ == '__main__':
    app.run(debug=True)
