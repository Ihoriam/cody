from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CheckerForm(FlaskForm):
    codeField = TextAreaField("Input your code", validators=[DataRequired()])
    inputField = TextAreaField("Input data", validators=[DataRequired()])
    outputField = TextAreaField("Output data", validators=[DataRequired()])
    submit = SubmitField('Sign In')