from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from flask_codemirror.fields import CodeMirrorField
from wtforms.validators import DataRequired


class CheckerForm(FlaskForm):
    codeField = TextAreaField("Ваш код", render_kw={"rows": 15, "cols": 10}, validators=[DataRequired()])
    # inputField = TextAreaField("Input data")
    # outputField = TextAreaField("Output data")
    selectLang = SelectField('', choices=[('gcc', 'C'), ('g++', 'C++'), ('py', 'Python'),\
                                          ('java', 'Java'), ('js', 'JavaScript')])
    submit = SubmitField('Перевірити')
