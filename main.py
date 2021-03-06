#!/usr/bin/python

# School: Launch Code
# Class: LC101 Ft. Meade F18
# Student: Alberto Morales
# Instructor: Patrick Kozub
# TA: Jesse Shaw
# Assignment: user_signedup
# Due date: December 17, 2018 @ 21:00

# import modules need it for the project
from flask import Flask, render_template
from wtforms.validators import InputRequired, DataRequired, Length,  Email, EqualTo, Optional, AnyOf
from wtforms import StringField, PasswordField, SubmitField, Form, validators
from flask_wtf import FlaskForm
import sys
import jinja2







app = Flask(__name__)
app.config['SECRET_KEY'] = 'development-key'


class SignupForm(FlaskForm):
    
    username = StringField('username', validators=[InputRequired
    (message='A username is required!'), 
    Length(min=3, max=20, message='Username must be between 3 to 20 characters long!')])

    password = PasswordField('password', validators=[InputRequired
    (message="Password is require!"), Length(
        min=3, max=20, message=
        'Password must be between 3 to 20 characters long, do not use space!'), 
        validators.EqualTo(
        'confirm', message='Passwords must match')])

    confirm = PasswordField('Repeat Password')

    email = StringField(
        'Email', [validators.Optional(strip_whitespace=True), AnyOf('@', message=None, values_formatter=None)])

    submit = SubmitField('Sign up')




@app.route("/index", methods=['GET','POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():
        return ' <h1> Welcome {}! ' . format(form.username.data, form.password.data)

    return render_template('index.html', form=form)


# statement app.run runs the app on local server
#thr debug=True flag any error message along the way

if __name__ == "__main__":
    app.run(debug=True)



   
