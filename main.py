# School: Launch Code
# Class: LC101 Ft. Meade F18
# Student: Alberto Morales
# Instructor: Patrick Kozub
# TA: Jesse Shaw
# Assignment: user_signedup
# Due date: December 17, 2018 @ 21:00

# import modules for ther project
from flask import Flask
import os
import jinja2

# add absolute path in the filesystem on which the program is running.
template_dir = os.path.join(os.path.dirname(__file__),
                            'templates')
# initialize jinja templating engine
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')


@app.route('/')
def index():
    return ""


app.run()


   
