from classQuestion import Question
from classQuiz import Quiz

from questionList import question_data
#learnt this concept with difficulty but now it's clear "List Comprehension"
questions = [Question(data["text"], data["answer"]) for data in question_data]
#passing questions array of instance of Question {text,answer,user_answer & method check_answer in Quiz class}
quiz = Quiz(questions)  
quiz.play()
