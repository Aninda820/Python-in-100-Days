                                        # Enumerate Function




marks = [4, 54, 32, 98, 44, 23, 92]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Very Good!!")
#     index += 1




for index, mark in enumerate(marks, start=1):
    print(mark)
    if (index == 3):
        print("Very Good!!")