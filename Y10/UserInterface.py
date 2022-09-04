def openquiz(filename):
    file = open(filename, "r")
    text = file.readlines()
    for i in range(4):
        question = text[i].split("#")
        print(question[0])
        answer = input("Answer (A/B): ")
        if answer == question[3]:
            print("Correct")
        else:
            print("Incorrect")


view = tk.Tk()
view.geometry("500x500")

welcomemessage = tk.Label(view, text = "Welcome to My revision quiz!")
welcomemessage.pack()

questionLabel = tk.StringVar()
quiz = input("What would you like to be quizzed on? (PM for primary memory and C for compression): ")
while quiz != "PM" and quiz != "C":
    quiz = input("What would you like to be quizzed on? (PM for primary memory and C for compression): ")

if quiz == "PM":
    openquiz("PrimaryMemory.txt")
elif quiz == "C":
    openquiz("Compression.txt")
