from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired


class HelpForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])


class DeleteForm(FlaskForm):
    id = IntegerField(validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_repeat = PasswordField(validators=[DataRequired()])


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])