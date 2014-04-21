# -*- coding: utf-8 -*-
from rapidData import quizzes

def getQuiz(id):
    for q in quizzes:
        if q['id'] == id:
            return q
def getResults(quizNo, user_id):
    q = getQuiz(quizNo)
    if q!= None:
        for r in q['results']:
            if r['user_id'] == user_id:
                return r

def submitResults(quizNo, user_id, score):
    # agrego los resultados a mi json con info del quiz
    # agrego los resultados al json del usuario
    # hago algo
    q = getQuiz(quizNo)
    if q != None:
        r = getResults(quizNo, user_id)
        if r != None:
            print "Found existing results..."
            if r['bestScore'] < score:
                r['bestScore'] = score
            r['scores'].append(score)
        else:
            newResult = {
                "user_id":user_id,
                "scores":[score],
                "bestScore":score
            }
            q['results'].append(newResult)
        print "Loaded results to quiz."



def getQuizzes(usr_id):
    return quizzes

