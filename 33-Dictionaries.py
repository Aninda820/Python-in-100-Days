                # Dictionaries



dic = {
    "Harry": "Human being",
    "Spoon": "Object",
    1: "Aninda",
    2: "Nila",
    3: "Bibek",
    4: "Dulal",
    5: "Asis"
}
print(dic)
print(dic["Harry"])
print(dic[1])
print(dic[2])
print(dic[3])
print(dic[4])
print(dic[5])
# print(dic["Harry2"])      # error line
print(dic.get("Harry"))
print(dic.get("Harry2"))


print(dic.keys())
print(dic.values())

for i in dic.keys():
    # print(dic[i])
    print(f"The value corresponding to the key {i} is {dic[i]}")



print(dic.items())


for k, value in dic.items():
    print(f"The value corresponding to the key {k} is {value}")
    print(f"The value corresponding to the key {k} is {dic[k]}")