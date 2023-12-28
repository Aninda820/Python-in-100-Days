#          (if- else statements)

a=int(input("enter your age\n"))
print("your age is:",a)

# conditional operators
# >,<, <=, >=, ==
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
    print("you can drive")
    print("but chalan too katega tera")
else:
    print("you can't drive")
    print("no, go for a cycle bitch")
  


    
a=int(input("enter the apple prise\n"))
budget= 200
if(budget- a>50):
    print("allexa, add 1kg apples to the cart.")
elif(budget- a>70):
    print("it ok you can buy.")
else:
    print("Alexa don't add any apples to the cart.")



num= int(input("enter the value of num\n"))
if(num<0):
    print("number is nagative.")
elif(num==0):
    print("the number is zero.")
elif(num==999):
    print("the number is spacial.")
else:
    print("the number is posative")
print("i'm happy now")




# (nested if- else)

num=int(input("enter the value of num\n"))
if(num<0):
    print("number is negative")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("the number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")

    
a= int(input("enter your age\n"))
print("your age is: ",a)
if(a>=20):
    print("you can drive")
elif(a<=10):
    print("you can't drive")
else:
    print("go for licence")
