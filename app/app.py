# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, url_for, redirect, request, session
from flask.ext.script import Manager
from rapid import getQuiz, submitResults, getQuizzes

DEBUG = True
SECRET_KEY = 'top secret'

app = Flask(__name__, static_folder="../static", static_url_path="/static")
app.config.from_object(__name__)


@app.route('/')
def index():
    # if user isnt logged in
    return redirect(url_for('home'))


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session['user_id'] = int(request.form['user_id'])
    elif not session.get('user_id'):
        return redirect(url_for('login'))
    quizzes = getQuizzes(session['user_id'])
    return render_template('index.jinja2.html', quizzes=quizzes)
    # have to make a redirect checking


@app.route('/login')
def login():
    return render_template('login.jinja2.html')


@app.route('/quiz/<id>')
def quiz(id):
    qdata = getQuiz(id)
    return render_template('quiz.jinja2.html',
                           qdata=qdata)


@app.route('/submitQuiz/<id>', methods=["GET", "POST"])
def submitQuiz(id):
    if request.method == "POST":
        print "Just being posted..."
        print request.json
        score = request.json['score']
        submitResults(id, session['user_id'], score)
    return redirect(url_for('home'))

manager = Manager(app)
if __name__ == '__main__':
    manager.run()
