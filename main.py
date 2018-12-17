#!/usr/bin/python

# School: Launch Code
# Class: LC101 Ft. Meade F18
# Student: Alberto Morales
# Instructor: Patrick Kozub
# TA: Jesse Shaw
# Assignment: user_signedup
# Due date: December 17, 2018 @ 21:00

# import modules need it for the project
from flask import Flask, render_template, request, redirect

from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, PasswordField, SubmitField
import cgi
import os
import jinja2

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'development-key'


class SignupForm(FlaskForm):
    #pending check
    username = StringField('username', validators=[
                       InputRequired("A username is require!")])

    password = PasswordField('password', validators=[InputRequired(
        "Password is require!"), validators.EqualTo('confirm', message='Passwords must match')])

    confirm = PasswordField('Repeat Password')

    email = StringField('E-mail', validators=[InputRequired(
        "Please enter your E-mail address."), Email("Please enter your email address.")])

    submit = SubmitField('Sign up')



@app.route("/index", methods=['GET','POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():
        return 'Sumitted!'

    return render_template('signup.html', form=form)





###
   







# statement app.run runs the app on local server
#thr debug=True flag any error message along the way

if __name__ == "__main__":
    app.run(debug=True)



   
