from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CheckerForm(FlaskForm):
    codeField = TextAreaField("Input your code")
    inputField = TextAreaField("Input data")
    outputField = TextAreaField("Output data")
    submit = SubmitField('Check')