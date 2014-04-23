# -*- coding: utf-8 -*-
import json
import bson
from bson.json_util import dumps
from flask import Flask, render_template, url_for, redirect, request, session, make_response
from rapid import getQuiz, submitResults, getQuizzes, getAnsweredQuizzesResults, getUnansweredQuizzesResults, connectMongoHQ, getUserResults, getQuizzesResults
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic

from config import CONFIG

DEBUG = True
SECRET_KEY = "my secret"

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    # if user isnt logged in
    # connectMongoHQ()
    return redirect(url_for('home'))


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session['user_id'] = int(request.form['user_id'])
    elif not session.get('user_id'):
        return redirect(url_for('login'))
    quizzes = getQuizzesResults(session['user_id'])
    #results = getUserResults(session['user_id'])
    whichActive = "all"
    return render_template('index.jinja2.html', quizzes=quizzes,
                           whichActive=whichActive)
    # have to make a redirect checking

@app.route('/answered', methods=["GET", "POST"])
def answered():
    if request.method == "POST":
        session['user_id'] = int(request.form['user_id'])
    elif not session.get('user_id'):
        return redirect(url_for('login'))
    quizzes = getAnsweredQuizzesResults(session['user_id'])
    #results = getUserResults(session['user_id'])
    whichActive = "answered"
    return render_template('index.jinja2.html', quizzes=quizzes,
                           whichActive=whichActive)
    # have to make a redirect checking

@app.route('/unanswered', methods=["GET", "POST"])
def unanswered():
    if request.method == "POST":
        session['user_id'] = int(request.form['user_id'])
    elif not session.get('user_id'):
        return redirect(url_for('login'))
    quizzes = getUnansweredQuizzesResults(session['user_id'])
    whichActive = "unanswered"
    return render_template('index.jinja2.html', quizzes=quizzes, whichActive=whichActive)
    # have to make a redirect checking

@app.route('/instructions', methods=["GET", "POST"])
def instructions():
    if request.method == "POST":
        session['user_id'] = int(request.form['user_id'])
    elif not session.get('user_id'):
        return redirect(url_for('login'))
    instructions = "JUEGA"
    whichActive = "instructions"
    return render_template('index.jinja2.html', instructions=instructions, whichActive=whichActive)
    # have to make a redirect checking

@app.route('/login')
def login():
    return render_template('login.jinja2.html')

@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def loginAuth(provider_name):
    authomatic = Authomatic(CONFIG, 'secret')
    response = make_response()
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)
    if result:
        if result.user:
            result.user.update()
            usr = result.user.to_dict()
            session['user_id'] = usr['id']
            print "This is the fb id: ", usr['id']
            return redirect(url_for('home'))
        return redirect(url_for('login'))
    return response

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
