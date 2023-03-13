#this is where the questions and their answers are stored
questions = ["What is the main subject studied in B-block?", "What is the main subject studied in E-block?", "What is the main subject studied in H-block?", "What is the main subject studied in G-block?", "What is the main subject studied in C-block?", "What is the main subject studied in F-block?", "What is the main subject studied in A-block?", "What is the main subject studied in K-block?", "What is the main subject studied in the RHS gyms?", "What is the main subject studied in P-block?", ]
answers = ["Tech", "Tech", "Food", "English", "Math", "Science", "Art", "Language", "P.E", "Science"]

score = 0

for i in range(len(questions)):
    print("Question", i+1, ":", questions[i])
    user_answer = input("Your answer: ")
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", answers[i])

print("Your final score is:", score, "out of", len(questions))

