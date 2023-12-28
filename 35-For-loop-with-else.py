                    # For loop with else




# for i in range(5):
#     print(i)
# else:
#     print("This is the else block")



# for i in []:
#     print(i)
# else:
#     print("This is the else block")



for i in range(5):
    print(i)
    if i==4:
        break

else:
    print("this is else block !!")





x = 0
while(x < 5):
    print(x)
    x = x+1
    if x == 4:
        break
else:
    print("End of program !!")






for y in range(5):
    print("itration no {} in for loop".format(y+1))
else:
    print("else block in loop")
print("End of loop!!")