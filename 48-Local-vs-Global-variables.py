# x = 4
# print(x)


# def Local_var():
#     x = 5

#     print(x)
#     print(f"The local x is {x}")
#     print("Hello harry!")


# print(f"The global x is {x}")
# Local_var()
# print(f"The global x is {x}")








x = 5
print(x)


def my_function():
    global x, y
    x = 10
    y = 20 # local variable
    print(x)

my_function()
print(x)
print(y)