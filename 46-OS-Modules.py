            # os Module in python


import os
# if(not os.path.exists("Hack")):
#     os.mkdir("Hack")

# for i in range(0, 10):                        # Make unlimited files
#     os.mkdir(f"Hack/Day{i+1}")


# for i in range(0, 10):                             # Rename thoes files
#     os.rename(f"Hack/Tutorial{i+1}", f"Hack/Tut{i+1}")



# folders = os.listdir("Hack")
# print(folders)
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Hack/{folder}"))
    


print(os.getcwd())
# cmd = "date"
# os.system(cmd)


print(os.name)


folders = os.listdir("Hack")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"Hack/{folder}"))