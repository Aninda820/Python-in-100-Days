                            # Finally keyword





# try:
#     i = [2, 5, 8, 12, 33, 9]
#     l = int(input("Enter the input: "))
#     print(i[l])
# except:
#     print("Some error occurred!!")
# finally:
#     print("I'm always executed")





def func1():
    try:
        i = [2, 5, 8, 12, 33, 9]
        l = int(input("Enter the input: "))
        print(i[l])
        return 1
    except:
        print("Some error occurred!!")
        return 0
    finally:
        print("I'm always executed")

x = func1()
print(x)