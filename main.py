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
import cgi
import os
import jinja2



app = Flask(__name__)



# Map url to index.html.html

@app.route('/')
def index():
    return render_template("index.html")


# statement app.run runs the app on local server
#thr debug=True flag any error message along the way

if __name__ == "__main__":
    app.run(debug=True)



   
