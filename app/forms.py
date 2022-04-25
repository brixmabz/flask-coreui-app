from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, EmailField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length, Email, email_validator


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(min=6, max=40, message=None)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=8, max=40, message=None)])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign In')
