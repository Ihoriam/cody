from app import app
from flask import render_template

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/main')
def mainPage():
    form = CheckerForm()
    return render_template('main.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()