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
from forms import SignupForm
import cgi
import os
import jinja2



app = Flask(__name__)


# Map index.html to main.py 
@app.route("/")
def index():
    return render_template("index.html")

# Map feedback to main.py


@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


@app.route("/signup", methods=['GET','POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        return "Success!"

    elif request.method == 'GET':
        return render_template("signup.html", form=form)








# statement app.run runs the app on local server
#thr debug=True flag any error message along the way

if __name__ == "__main__":
    app.run(debug=True)



   
