# -*- coding: utf-8 -*-
from flask import session
from rapidData import quizzes
from pymongo import MongoClient

DB = "rapid-quiz"
cQuestions = "collQuestions"
cQuizzes = "collQuizzes"
cResults = "collResults"



def getQuiz(id):
    coll = MongoClient()[DB][cQuizzes]
    print "This is the id", id
    q = coll.find_one({'_id':id})
    print "Got quiz", q['title']
    return q

def getResults(quiz_id, user_id):
    coll = MongoClient()[DB][cResults]
    r = coll.find_one({'quiz_id':quiz_id, 'user_id':user_id})
    return r

def getQuizID(quizNo):
    coll = MongoClient()[DB][cQuizzes]
    q = coll.find_one({'id':quizNo})
    return q['_id']

def submitResults(quizNo, user_id, score):
    # agrego los resultados a mi json con info del quiz
    # agrego los resultados al json del usuario
    # hago algo
    q = getQuiz(quizNo)
    if q != None:
        r = getResults(quizNo, user_id)
        if r != None:
            print "Found existing results..."
            rtemp= r
            if r['bestScore'] < score:
                r['bestScore'] = score
            r['scores'].append(score)

            # update the user result in the quiz var
            for index, item in enumerate(q['results']):
                if item['user_id'] == user_id :
                    q['results'][index] = r
        else:
            newResult = {
                "user_id":user_id,
                "scores":[score],
                "bestScore":score
            }
            r = newResult
            q['results'].append(r)
        print "Loaded results to quiz: ", q['results'][len(q['results']) - 1]
        #update in db
        coll = MongoClient()[DB][cResults]
        coll.update({'quiz_id':quizNo, 'user_id':user_id}, r, upsert=True)
        print "Updated this doc: ", list(coll.find({'quiz_id':quizNo, 'user_id':user_id}))
        coll = MongoClient()[DB][cQuizzes]
        coll.update({'_id':quizNo}, q, upsert=True)
        print "Updated this doc: ", list(coll.find({'_id':quizNo}))


def getUnansweredQuizzes(user_id):
    coll = MongoClient()[DB][cQuizzes]
    qs = list(coll.find())
    uaqs = []
    for q in qs:
        for r in q['results']:
            if r['user_id'] != user_id:
                uaqs.append(q)

    return uaqs

def getAnsweredQuizzes(user_id):
    coll = MongoClient()[DB][cQuizzes]
    qs = list(coll.find())
    aqs = []
    for q in qs:
        for r in q['results']:
            if r['user_id'] == user_id:
                aqs.append(q)
    return aqs

def getQuizzes():
    coll = MongoClient()[DB][cQuizzes]
    q = list(coll.find())
    for e in q:
        print e['title']
        for r in e['results']:
            if r['user_id'] == session['user_id']:
                print "From this user: ", e['results']
            else:
                print "Not from this user: ", e['results']
    return q

