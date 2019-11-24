from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/main')
def mainPage():
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
