# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__, static_folder="../static", static_url_path="/static")
app.debug = True

q1 = {
    "question" : "Cristobal Colón descubrió las Islas Caimán.",
    "questionType" : "VF",
    "options" : [
        "True",
        "False"
    ],
    "answer" : 1,
    "explanation" : "Cristobal Colón descubrió América el 12 de Octubre de 1492. Pensó que había llegado a la India.",
    "dificulty" : 0
}
q2 = {
    "question" : "Santa Anna fue el presidente mexicano que vendio territorio nacional a EUA",
    "questionType" : "VF",
    "options" : [
        "True",
        "False"
    ],
    "answer" : 0,
    "explanation" : "Santa Anna vendió mucho de lo que ahora es conocido como Texas a EUA.",
    "dificulty" : 0
}
q3 = {
    "question" : "La revolución mexicana se inicio en Queretaro",
    "questionType" : "VF",
    "options" : [
        "True",
        "False"
    ],
    "answer" : 1,
    "explanation" : "La revolución mexicana se inició en Puebla.",
    "dificulty" : 1
}
quiz_data = {
    "title" : "Historia",
    "category" : "historia",
    "questions" : [
        q1,
        q2,
        q3
    ],
    "results" : [

    ]
};

def getQuiz():
    return quiz_data

@app.route('/')
def index():
    return render_template('index.jinja2.html')

@app.route('/quiz')
def quiz():
    qdata = getQuiz()
    return render_template('quiz.jinja2.html',
                           qdata=qdata)

manager = Manager(app)
if __name__ == '__main__':
    manager.run()
