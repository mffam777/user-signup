# Import Flask-WTF functions
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    #pending check
    user_name = StringField('User Name', validators=[DataRequired("Please enter your User Name.")])
    user_password = PasswordField('Password', validators=[DataRequired(
        "Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])   

    user_vpwd = PasswordField('Password', validators=[DataRequired(
        "Password verification doesn't match.")])

    user_email = StringField('E-mail', validators=[DataRequired("Please enter your E-mail address."), Email("Please enter your email address.")])
    
    submit = SubmitField('Sign up')

