questions = [
    ["What is my favarite language?: ", "Python", "Java", "PHP", "HTML, CSS", "PHP", 1],
    ["What is my aim?: ", "Hacker", "Programmer", "Teacher", "Gammer", 2]
]
def Group():
    for i in range(0, len(questions)):
        question = questions [i]
        print(f"a. {question[1]}       b. {question[2]}")
        print(f"c. {question[3]}       d. {question[4]}")
        reply = int(input("Enter your answer(1-4): "))
        if(reply==questions[-1]):
        # if(reply==1):
            print(f"Correct answer, you won in this challange!!")
        else:
            print("Wrong answer, you loose!!")
            break

Group()
