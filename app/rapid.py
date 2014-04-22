# -*- coding: utf-8 -*-
import os
from pymongo import MongoClient

DB = "rapid-quiz"
cQuestions = "collQuestions"
cQuizzes = "collQuizzes"
cResults = "collResults"

MONGO_URL = os.environ.get('MONGOHQ_URL')
client = MongoClient(MONGO_URL)
db = client['rapid-quiz']
print "Connected to: ", db.collection_names()

def connectMongoHQ():
    MONGO_URL = os.environ.get('MONGOHQ_URL')
    client = MongoClient(MONGO_URL)
    db = client['rapid-quiz']
    print "Connected to: ", db.collection_names()

def getQuiz(id):
    coll = db[cQuizzes]
    print "This is the id", id
    q = coll.find_one({'_id':id})
    print "Got quiz", q['title']
    return q

def getResults(quiz_id, user_id):
    coll = db[cResults]
    r = coll.find_one({'quiz_id':quiz_id, 'user_id':user_id})
    return r

def getUserResults(user_id):
    coll = db[cResults]
    r = list( coll.find({'user_id':user_id}) )
    return r

def getQuizID(quizNo):
    coll = db[cQuizzes]
    q = coll.find_one({'id':quizNo})
    return q['_id']

def submitResults(quizNo, user_id, score):
    r = getResults(quizNo, user_id)
    if r != None:
        print "Found existing results..."
        if r['bestScore'] < score:
            r['bestScore'] = score
        r['scores'].append(score)
    else:
        print "New results..."
        newR = {}
        newR['quiz_id'] = quizNo
        newR['user_id'] = user_id
        newR['bestScore'] = score
        newR['scores'] = []
        newR['scores'].append(score)
        r = newR
    coll = db[cResults]
    print "Modified results: ", r
    coll.update({'quiz_id':quizNo, 'user_id':user_id}, r, upsert=True)


def getQuizzesResults(user_id):
    qrs = []
    qs = getQuizzes()
    for q in qs:
        qr = {}
        qr['_id'] = q['_id']
        qr['title'] = q['title']
        r = getResults(q['_id'], user_id)
        qr['result'] = None
        if r != None:
            qr['result'] = r['bestScore']
        qrs.append(qr)
    return qrs


def getUnansweredQuizzesResults(user_id):
    qrs = []
    qs = getQuizzes()
    for q in qs:
        qr = {}
        r = getResults(q['_id'], user_id)
        if r == None:
            qr['_id'] = q['_id']
            qr['title'] = q['title']
            qr['result'] = None
            qrs.append(qr)
    return qrs

def getAnsweredQuizzesResults(user_id):
    qrs = []
    qs = getQuizzes()
    for q in qs:
        qr = {}
        r = getResults(q['_id'], user_id)
        if r != None:
            qr['_id'] = q['_id']
            qr['title'] = q['title']
            qr['result'] = r['bestScore']
            qrs.append(qr)
    return qrs


def getQuizzes():
    coll = db[cQuizzes]
    q = list(coll.find())
    return q

