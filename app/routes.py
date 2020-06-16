from app import app
from flask import render_template, request
from app.forms import CheckerForm
from app.models import Task, Language, Code, Test
import subprocess
import pathlib
import os, shutil

PATH_LIST = ['temp/py', 'temp/js', 'temp/java', 'temp/gcc', 'temp/g++']

def clean_temp_folders(path_list):
    for path in path_list:
            folder = path
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

@app.route('/main')
def mainPage():
    tasks = Task.query.all()

    return render_template('main.html',
                            tasks=tasks)


@app.route('/task/<int:id_task>', methods=['GET', 'POST'])
def taskPage(id_task):
    form = CheckerForm()
    task = Task.query.filter_by(id = id_task).first()
    
    # print(task.name)
    if request.method == 'POST' and form.validate_on_submit():
        # print(form.selectLang.data)
        if form.selectLang.data == 'py':
            code = Code.query.filter_by(id_task=id_task, id_lang=3).first()
            tests = Test.query.filter_by(id_code=code.id).all()
            num_tests = len(tests)
            count = 0
            with open("temp/py/sub.py", "w") as sub:
                sub.writelines([code.pre_code, '\n', form.codeField.data, '\n', code.post_code])
            for test in tests:
                # print(test.input_data)
                process = subprocess.run(['python3', 'temp/py/sub.py', *test.input_data.split()],
                                        check=False,
                                        capture_output=True,  
                                        universal_newlines=True)
                
                if (process.stdout) and process.stdout.strip() == test.output_data.strip():
                    count += 1
                    # print(count)
                else:
                    break

            
            # flag_valid = 1 if output.strip() == form.outputField.data.strip() else 0
        if form.selectLang.data == 'js':
            with open("temp/js/sub.js", "w") as sub:
                sub.write(form.codeField.data)
            process = subprocess.run(['node', 'temp/js/sub.js'],
                                     check=False,
                                     capture_output=True,  
                                     universal_newlines=True)

        if form.selectLang.data == 'java':
            with open("temp/java/sub.java", "w") as sub:
                sub.write(form.codeField.data)
            process = subprocess.run(['javac', 'temp/java/sub.java'],
                                         check=False,
                                         capture_output=True,  
                                         universal_newlines=True)
            if not process.stderr:
                post_process = subprocess.run(['java', '-cp', 'temp/java/', 'sub'],
                                        check=False,
                                        capture_output=True,  
                                        universal_newlines=True)

        if form.selectLang.data == 'gcc':
            with open("temp/gcc/sub.c", "w") as sub:
                sub.write(form.codeField.data)
            process = subprocess.run(['gcc', '-o', 'temp/gcc/sub', 'temp/gcc/sub.c'],
                                         check=False,
                                         capture_output=True,  
                                         universal_newlines=True)
            if not process.stderr:
                post_process = subprocess.run(['./temp/gcc/sub'],
                                        check=False,
                                        capture_output=True,  
                                        universal_newlines=True)

        if form.selectLang.data == 'g++':
            with open("temp/g++/sub.c", "w") as sub:
                sub.write(form.codeField.data)
            process = subprocess.run(['g++', '-o', 'temp/g++/sub', 'temp/g++/sub.c'],
                                         check=False,
                                         capture_output=True,  
                                         universal_newlines=True)
            if not process.stderr:
                post_process = subprocess.run(['./temp/g++/sub'],
                                        check=False,
                                        capture_output=True,  
                                        universal_newlines=True)
        print(pathlib.Path().absolute())
        
        clean_temp_folders(PATH_LIST)

        if 'post_process' in locals():
            error = post_process.stderr
            output = post_process.stdout
        else:
            error = process.stderr
            output = process.stdout

        print(output)
        print(error) 
        # if error:
        #     flag_valid = False
        # else:
        #     flag_valid = True

        if count == num_tests:
            flag_valid=True
        else:
            flag_valid=False
        
        return render_template('result.html',
                               code=form.codeField.data,
                               propose_code = code.main_code,
                               error=error,
                               flag=flag_valid,
                               count=count,
                               num_tests=num_tests
                               )
    else:

        return render_template('task.html', form=form, task=task)
