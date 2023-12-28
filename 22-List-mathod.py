#                                          List mathod


marks = [9, 4, 15, 33, "harry", "Aninda", 2, 20]
print(marks[0])
print(marks)
print(len(marks))
print(marks[2])
print(marks[4])
print(marks[len(marks)-2])
if "arr" in "harry":
    print("Yes")
else:
    print("No")

if "nin" in "Aninda":
    print("yes")
else:
    print("no")

if 7 in marks:
    print("Yes")
else:
    print("No")

# if 15 in marks:
#     print("yes")
# else:
#     print("no")

# if 6 in marks:
#     print("yes")
# else:
#     print("no")

# if "6" in marks:
#     print("yes")
# else:
#     print("no")










numbers =  [30, 9, 6, 44, 29, 50, 55]
print(len(numbers))
print(numbers[-4])
print(numbers[-3])
print(numbers[len(numbers)-3])
print(numbers[5-3])
print(numbers[1:-5])
# print(numbers[1:6])
print("\n")
print(numbers[1:6:2])
# print(numbers[0:len(numbers)])


lst = [i for i in range(5)]
print(lst)
Snd = [i*i for i in range(5)]
print(Snd)


lst = [i*i for i in range(20) if i%2==0]
print(lst)