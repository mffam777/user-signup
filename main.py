# School: Launch Code
# Class: LC101 Ft. Meade F18
# Student: Alberto Morales
# Instructor: Patrick Kozub
# TA: Jesse Shaw
# Assignment: user_signedup
# Due date: December 17, 2018 @ 21:00


from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')


@app.route('/')
def index():
    return ""


app.run()


   