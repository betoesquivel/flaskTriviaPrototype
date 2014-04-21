# -*- coding: utf-8 -*-
import json
import bson
from bson.json_util import dumps
from flask import Flask, render_template, url_for, redirect, request, session
from flask.ext.script import Manager
from rapid import getQuiz, submitResults, getQuizzes, getAnsweredQuizzes, getUnansweredQuizzes

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
    quizzes = getQuizzes()
    whichActive = "all"
    return render_template('index.jinja2.html', quizzes=quizzes, whichActive=whichActive)
    # have to make a redirect checking

@app.route('/answered', methods=["GET", "POST"])
def answered():
    if request.method == "POST":
        session['user_id'] = int(request.form['user_id'])
    elif not session.get('user_id'):
        return redirect(url_for('login'))
    quizzes = getAnsweredQuizzes(session['user_id'])
    whichActive = "answered"
    return render_template('index.jinja2.html', quizzes=quizzes, whichActive=whichActive)
    # have to make a redirect checking

@app.route('/unanswered', methods=["GET", "POST"])
def unanswered():
    if request.method == "POST":
        session['user_id'] = int(request.form['user_id'])
    elif not session.get('user_id'):
        return redirect(url_for('login'))
    quizzes = getUnansweredQuizzes(session['user_id'])
    whichActive = "unsanswered"
    return render_template('index.jinja2.html', quizzes=quizzes, whichActive=whichActive)
    # have to make a redirect checking


@app.route('/login')
def login():
    return render_template('login.jinja2.html')


@app.route('/quiz/<id>')
def quiz(id):
    quiz_oid = bson.ObjectId(oid=str(id))
    qdata = getQuiz(quiz_oid)
    q = json.loads(dumps(qdata))
    print q
    return render_template('quiz.jinja2.html',
                           q=q)


@app.route('/submitQuiz/<id>', methods=["GET", "POST"])
def submitQuiz(id):
    if request.method == "POST":
        print "Just being posted..."
        print request.json
        score = request.json['score']
        quiz_oid = bson.ObjectId(oid=str(id))
        submitResults(quiz_oid, session['user_id'], score)
    return redirect(url_for('home'))

manager = Manager(app)
if __name__ == '__main__':
    manager.run()
