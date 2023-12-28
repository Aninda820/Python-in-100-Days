#            While loops



i = 0
while(i<10):
    print("Hello World")
    print(i+1)
    # i += 1
    i = i + 1


x = int(input("Enter a number: "))
while(x < 30):
    x = int(input("Enter the number again: "))
    print(x)
print("Done with the loop!")



count = 5
while count > 0:
    print(count)
    # count = count -1
    count -= 1
else:
    print("Inside the else!")