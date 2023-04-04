quiz= {
     "question 1":{
    "question": "Cual es la capital de Francia?",
    "answer": "Paris"
     },
     "question 2":{
    "question": "Cual es la capital de Alemania?",
    "answer": "Berlin"
     },
     "question 3":{
    "question": "Cual es la capital de Italia?",
    "answer": "Roma"
     },
     "question 4":{
    "question": "Cual es la capital de España?",
    "answer": "Madrid"
     },
     "question 5":{
    "question": "Cual es la capital de Portugal?",
    "answer": "Lisboa"
     },
     "question 6":{
    "question": "Cual es la capital de Suiza?",
    "answer": "Berna"
     },
}

score = 0
for key, value in quiz.items():
    print (value['question'])
    answer = input ("Answer? ")

    if answer.lower()==value ['answer'].lower():
        print('correct')
        score =score + 1
        print("your score is:"+ str(score))

    else:
        print ("Wrong")
        print("The answer is: " +value['answer'])
        print("your score is:" +str(score))
