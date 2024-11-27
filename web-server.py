from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_geek():
    return "<h1>Hello World!</h1>", 200


@app.route('/bad')
def stimulate_502():
    return "<h1>Bad Gateway</h1>", 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)