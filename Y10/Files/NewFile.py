newfile = open("CreatedQuiz.txt", "w")
for i in range(4):
    q = ""
    question = input("Input your question: ")
    q += question
    optionA = input("Input your first option: ")
    q += "A.)" + optionA + "#"
    optionB = input("Input your second option: ")
    q += "B.)" + optionB + "#"
    corrAns = input("Input your correct answer: ")
    q += corrAns + "#"
    newfile.write(q+"\n")

file = open("CreatedQuiz.txt", "r")
print(file.read())
