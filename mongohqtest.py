import os
import pymongo
from pymongo import MongoClient


cQuestions = "collQuestions"
cQuizzes = "collQuizzes"
cResults = "collResults"

MONGO_URL = os.environ.get('MONGOHQ_URL')
client = MongoClient(MONGO_URL)

db = client['rapid-quiz']
print "Connected to the database..."
print db.collection_names()

print "Getting quizzes collection..."
print list ( db[cQuizzes].find() )
