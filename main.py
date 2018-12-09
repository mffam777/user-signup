#!/usr/bin/python

# School: Launch Code
# Class: LC101 Ft. Meade F18
# Student: Alberto Morales
# Instructor: Patrick Kozub
# TA: Jesse Shaw
# Assignment: user_signedup
# Due date: December 17, 2018 @ 21:00

# import modules for ther project
from flask import Flask, request, redirect
import os
import jinja2

#DELETE
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
# from app.models import User

# add absolute path in the filesystem on which the program is running.
template_dir = os.path.join(os.path.dirname(__file__),
                            'templates')
# initialize jinja templating engine
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
# In the index function, create a template variable that holds the template 
# returned from Jinja's get_template function and then return the string that 
# template.render()
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

# add function, but this time pass an argument to template.render that matches a 
# placeholder called name
# @app.route('/form', method='POST')
# def form():
    #first_name = request.form['first_name']
    #template = jinja_env.get_template('feedback.html')
    #return template.render(name=first_name)

app.run()


   
