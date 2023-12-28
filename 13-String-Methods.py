#           String methods




a = "Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))





txt = " Hello World "
x = txt.strip()         # Return the string without any whitespace at the beginning or the end.
print(x)


caption = "this is my first python blog"
print(caption.capitalize())

words = "welcome to the python tutorial"
print(len(words))
print(len(words.center(50)))

print(a.count("Harry"))


words = "welcome to the python tutorial"
print(words.endswith("tutorial"))
print(words.endswith("al"))
print(words.endswith("tu"))
print(words.endswith("to", 3, 10))



words = "welcome to the python tutorial"
print(words.startswith("wel"))
print(words.startswith("welcome"))
print(words.startswith("come"))



findWord = "He's name is Jon. He is a rich man."
print(findWord.find("is"))   #index and find mathod both are same
print(findWord.index("is"))  
print(findWord.find("ishh"))   #when it become flase it's return -1
# print(findWord.index("ishh"))   #it's return Error


words = "welcomeToThePythonTutorial"
print(words.isalnum())


latter = "Welcome"
print(latter.isalpha())
latter = "Welcome00"
print(latter.isalpha())



hi = "hello sir!"
print(hi.islower())
hello = "HELLO WORLD"
print(hello.isupper())



printOrNot = "I love my wife"
print(printOrNot.isprintable())
printOrNot = "I love my wife \n"  # \n is not a printable carrecter 
print(printOrNot.isprintable())



str1 = "        "
print(str1.isspace()) #space using Tab
str2 = "         "
print(str2.isspace()) #space using space



str3 = "To Kill A Mocking Bird"
print(str3.istitle())
str3 = "To kill a mocking bird"
print(str3.istitle())



change = "I love python coding Most"
print(change.swapcase())
print(change.title())

