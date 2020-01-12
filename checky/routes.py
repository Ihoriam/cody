from checky import app
from flask import render_template, request
from checky.forms import CheckerForm
import subprocess
import os


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/main', methods=['GET', 'POST'])
def mainPage():
    form = CheckerForm()
    if request.method == 'POST':

        with open("temp_sub.py", "w") as sub:
            sub.write(form.codeField.data)

        process = subprocess.run(['python3', 'temp_sub.py', *form.inputField.data.split()],
                                 check=True,
                                 stdout=subprocess.PIPE,
                                 universal_newlines=True)
        output = process.stdout
        flag_valid = 1 if output.strip() == form.outputField.data.strip() else 0

        return render_template('result.html',
                               code=form.codeField.data,
                               inData=form.inputField.data,
                               validOutData=form.outputField.data,
                               reallyOutData=output,
                               flag=flag_valid
                               )
    else:
        return render_template('main.html', form=form)
