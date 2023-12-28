#           Operation on Tuples



# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")
# print(temp.pop(3))                 #remove item
# countries = tuple(temp)
# print(countries)





# country1 = ("india", "landon", "Kasmir", "Japan")
# country2 = ("Vutan", "koria", "Taiwan")
# marge = country1 + country2
# print(marge)




# tuple1 = (3, 5, 1, 0, 4, 3, 9, 7, 7, 3, 3)
# # res = tuple1.count(3)
# res = tuple1.index(3, 4, 9)
# print("The index of 3 is: ", res)



marks = (2, 5, 44, 77, 3, 8, 90, 3, 33, 44, 3, 4, 3, 44)
print(type(marks))
print(len(marks))
mark = list(marks)
print(type(mark))

print(marks.count(44))
mark.remove(2)
print(mark)
mark.insert(0, 999)
print(mark)
print(mark.index(44))


marks = tuple(mark)
print(marks)
