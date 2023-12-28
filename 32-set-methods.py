                            # set methods



s1 = {1, 2, 5, 6}
s2 = {3, 6, 7, 1}
print(s1.union(s2))
s1.update(s2)
print(s1)



print("\n")



s4 = {1, 2, 5, 6}
s5 = {3, 6, 7, 1}
print(s4.intersection(s5))
s4.intersection_update(s5)
print(s4)



print("\n")



city = {"Haldia", "Tamluk", "Barlin", "Tokio"}
city2 = {"Madla", "Radhamoni", "Tamluk", "Haldia", "Durgachak"}
city3 = city.symmetric_difference(city2)
print(city3)




print("\n")




city4 = {"Haldia", "Tamluk", "Barlin", "Tokio"}
city5 = {"Madla", "Radhamoni", "Tamluk", "Haldia", "Durgachak"}
city6 = city4.difference(city5)
city7 = city5.difference(city4)
print(city6)
print(city7)





print("\n")




city8 = {"Haldia", "Tamluk", "Barlin", "Tokio"}
city9 = {"Madla", "Radhamoni", "Tamluk", "Haldia", "Durgachak"}
city10 = city8.isdisjoint(city9)
print(city10)
city11 = {"Haldia1", "Tamluk1", "Barlin", "Tokio"}
city12 = {"Madla", "Radhamoni", "Tamluk", "Haldia", "Durgachak"}
print(city11.isdisjoint(city12))




print("\n")





city13 = {"Haldia", "Tamluk", "Barlin", "Tokio"}
city14 = {"Madla", "Durgachak"}
print(city13.issuperset(city14))
city15 = {"Haldia", "Tamluk", "Barlin", "Tokio"}
city16 = {"Tamluk", "Haldia"}
print(city15.issuperset(city16))
print(city16.issubset(city15))





print("\n")





cityName = {"Tokio", "Haldia", "Durgachak", "Barlin", "Dilhi"}
cityName.add("Toll_Plaza")
print(cityName)


print("\n")


cityName = {"Tokio", "Haldia", "Durgachak", "Barlin", "Dilhi"}
cityName.remove("Barlin")
print(cityName)


print("\n")


cityName = {"Tokio", "Haldia", "Durgachak", "Barlin", "Dilhi"}
cityName.discard("tokiyo")
print(cityName)



print("\n")



item = cityName.pop()
print(item)