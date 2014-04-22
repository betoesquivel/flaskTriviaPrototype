# -*- coding: utf-8 -*-
q1 = {
    "question" : "Cristobal Colón descubrió las Islas Caimán.",
    "questionType" : "VF",
    "category" : "historia",
    "options" : [
        "True",
        "False"
    ],
    "answer" : 1,
    "explanation" : "Cristobal Colón descubrió América el 12 de Octubre de 1492. Pensó que había llegado a la India.",
    "difficulty" : 0
}
q2 = {
    "question" : "Santa Anna fue el presidente mexicano que vendio territorio nacional a EUA",
    "questionType" : "VF",
    "category": "historia",
    "options" : [
        "True",
        "False"
    ],
    "answer" : 0,
    "explanation" : "Santa Anna vendió mucho de lo que ahora es conocido como Texas a EUA.",
    "difficulty" : 0
}
q3 = {
    "question" : "La revolución mexicana se inicio en Queretaro",
    "questionType" : "VF",
    "category": "historia",
    "options" : [
        "True",
        "False"
    ],
    "answer" : 1,
    "explanation" : "La revolución mexicana se inició en Puebla.",
    "difficulty" : 0
}
# this result is updated after a user takes a quiz
# each quiz has one per user that has taken the quiz
quizUserResult = {
    "user_id":1,
    "quiz_id":1,
    "scores":[
        60, 70, 75, 60, 70, 90
    ],
    "bestScore":90
}
# all the data pertaining a quiz
quiz_data = {
    "id" : "1",
    "title" : "Historia",
    "category" : "historia",
    "difficulty": 0,
    "questions" : [
        q1,
        q2,
        q3
    ],
    "results" : [
        quizUserResult
    ]
}
quiz_data2 = {
    "id" : "2",
    "title" : "Historia 2",
    "category" : "historia",
    "questions" : [
        q2,
        q3,
        q1
    ],
    "results" : [
    ]
}

# array of all the quizzes in the app
quizzes = [
    quiz_data,
    quiz_data2
]

# contains the quizzes the user has taken
testUser = {
    "user_id": 1,
    "quizzes":[
        {
            "quizNo": 1,
            "bestResult": 90
        }
    ]
}




