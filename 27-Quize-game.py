                # Quize game



dic = {
    1: "DOS",
    2: "Linux",
    3: "Mac",
    4: "Windows",
    5: "Android"
}
dic1 = {
    1: "Brown",
    2: "Black",
    3: "White"
}

def qLoop():
    for i in dic1:
        print(i,". ", dic1[i])
        
print("Who is the mother of OS?")

try:
    x = input("Enter your answer: ")
    match int(x):
            case 1:
                print("DOS")
                print("You pick the wrong answer!!")
            case 2:
                print("Linux")
                print("Amazing!!")
            case 3:
                print("Mac")
                print("You pick the wrong answer!!")
            case 4:
                print("Windows")
                print("You pick the wrong answer!!")
            case 5:
                print("Android")
                print("You pick the wrong answer!!")
            case _:
                print("Invalid input!!!\n try again")
except ValueError:
    print("Enter the Integer !!")
qLoop()
print("Which hacker work for Government?")

try:
    x = input("Enter your answer: ")
    match int(x):
            case 1:
                print("Brown")
                print("You pick the wrong answer!!")
            case 2:
                print("Black")
                print("Amazing!!")
            case 3:
                print("White")
                print("You pick the wrong answer!!")
            case _:
                print("Invalid input!!!\n try again")
except ValueError:
    print("Enter the Integer !!")
    