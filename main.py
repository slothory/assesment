#this is where the questions and their answers are stored
questions = ["What is the main subject studied in B-block?", "What is the main subject studied in E-block?", "What is the main subject studied in H-block?", "What is the main subject studied in G-block?", "What is the main subject studied in C-block?", "What is the main subject studied in F-block?", "What is the main subject studied in A-block?", "What is the main subject studied in K-block?", "What is the main subject studied in the RHS gyms?", "What is the main subject studied in P-block?", ]
answers = ["Tech", "Tech", "Food", "English", "Math", "Science", "Art", "Language", "P.E", "Science"]

#Main code
score = 0   

for i in range(len(questions)):
    print("Question", i+1, ":", questions[i])
    user_answer = input("Your answer: ")
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1   #adds one to the score
    else:
        print("Incorrect. The correct answer is", answers[i])    #doesn't add one to the score because you got it wrong

print("Your final score is:", score, "out of", len(questions))    #calculates the amount of questions you got right and how many you got wrong.

