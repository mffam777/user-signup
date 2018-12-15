# Import Flask-WTF functions
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
# Pending Delete
from wtforms import TextField
from wtforms import Form, BooleanField, TextField, validators

class SignupForm(Form):

    first_name = StringField('First Name', validators=[DataRequired("Please enter your First Name.")])
    last_name = StringField('Last Name', validators=[DataRequired("Please enter your Last Name.")])
    email = StringField('E-mail', validators=[DataRequired("Please enter your E-mail address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
    submit = SubmitField('Sign up')

