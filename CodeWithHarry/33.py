# Dictionaries in python

dic = {
    "name": "parth",
    "Surname": "bhuva",
    "age" : 19
}
print(dic)
print(type(dic))
print(len(dic))

print("------------------------------")

print(dic["name"])
# print(dic["name2"])  # Error throw karse
print(dic.get("name2"))
print(dic["Surname"])
print(dic["age"])

print("------------------------------")

dic1 = {
    101: "parth",
    102: "kevin",
    103: "hevin",
    104: "mayur",
    105: "shubham"
}
print(dic1)
print(dic1[103])
print(dic1[105])

print("------------------------------")

dic2 = {
    "name": "parth",
    "Surname": "bhuva",
    "age" : 19
}
print("Dic2 keys is :", dic2.keys())

print("Dic2 values is :", dic2.values())

print(dic2.items()) 

print("------------------------------")

# Access the keys
for key in dic2.keys():
    print(key)

print("------------------------------")

# Access the values
for value in dic2.values():
    print(value)

print("------------------------------")

# Access the keys and values
for key, value in dic2.items():
    print(key,value)

