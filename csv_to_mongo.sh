# mongodb://<user>:<password>@oceanic.mongohq.com:10019/app24410107
mongoimport -h oceanic.mongohq.com --port 10019 -d app24410107 -c collQuestions -u ppesq -p28282828 --type csv --file ~/workspace/rapid-quiz/aid/preguntasCSV.csv --headerline
