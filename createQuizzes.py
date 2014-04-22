# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pprint

pp = pprint.PrettyPrinter(indent=4)

#[
#	"historia",
#	"arte",
#	"entretenimiento",
#	"atre",
#	"ciencia",
#	"agilidad mental",
#	"geografia"
#]

MONGO_URL = "mongodb://<user>:<pass>@oceanic.mongohq.com:10019/<databasename>"
client = MongoClient(MONGO_URL)
db = client['app24410107']
print "Connected to: ", db.collection_names()

coll = db['collQuestions']
questions = list( coll.find({'category':'historia'}) )

print "Preguntas del quiz: "
pp.pprint(questions)


quiz = {
}
quiz['category'] = "historia"
quiz['title'] = "Historia"
quiz['difficulty'] = 2
quiz['questions'] = questions


print "Quiz a subir: "
pp.pprint(quiz)


coll = db['collQuizzes']
#coll.insert(quiz)
