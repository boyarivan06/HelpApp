from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, \
    TextAreaField, FileField, EmailField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class HelpForm(FlaskForm):
    pass