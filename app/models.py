from app import db
from app import admin
from flask_admin.contrib.sqla import ModelView


class Task (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    about = db.Column(db.Text(), nullable=False)

    codes = db.relationship('Code', backref='task', lazy=True)


class Language(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    codes = db.relationship('Code', backref='language', lazy=True)


class Code (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_task = db.Column(db.Integer(), db.ForeignKey('task.id'))
    id_lang = db.Column(db.Integer(), db.ForeignKey('language.id'))
    pre_code = db.Column(db.Text())
    main_code = db.Column(db.Text(), nullable=False)
    post_code = db.Column(db.Text())

    tests = db.relationship('Test', backref='code', lazy=True)


class Test (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_code = db.Column(db.Integer(), db.ForeignKey('code.id'))
    input_data = db.Column(db.Text(), nullable=False)
    output_data = db.Column(db.Text(), nullable=False)

class MyModelView(ModelView):
    column_display_pk = True
    column_hide_backrefs = True

admin.add_view(MyModelView(Task, db.session))
admin.add_view(MyModelView(Code, db.session))
admin.add_view(MyModelView(Language, db.session))
admin.add_view(MyModelView(Test, db.session))

