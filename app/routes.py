from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import CheckerForm

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/main', methods=['GET', 'POST'])
def mainPage():
    form = CheckerForm()
    if request.method == 'POST':
        return redirect(url_for('resultPage'))
    return render_template('main.html', form=form)


@app.route('/result')
def resultPage():
    return 'Result'

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()