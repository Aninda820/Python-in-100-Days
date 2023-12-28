                        # Exception Handiling



a = input("Enter the number: ")
print(f"Multiplicatin table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a)*i}")
except ValueError:
    print("Invalid input!!")


print("some lines of code!")
print("End of program")




try:
    num = int(input("Enter a number: "))
    y = [6, 3]
    print(y[num])
except ValueError:
    print("This is not an inreger!!")
except IndexError:
    print("Index error!!")