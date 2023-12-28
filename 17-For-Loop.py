#          For loops



name = "Aninda"
for i in name:
    print(i)
    if(i=="d"):
        print("This is somthing spacial!")


color = ["Red", "Green", "Yellow", "Blue"]
for x in color:
    print(x)
    for i in x:
        print(i)




for number in range(100):  #(0, 100)  (start, stop)
    print(number+1)


for k in range(1,201):    #(start, stop)
    print(k)


for y in range(1, 20, 3):  #(start, stop, steps)
    print(y)