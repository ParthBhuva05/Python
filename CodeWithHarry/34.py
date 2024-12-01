# Dictionary Method in python

# Dictionary Method     Description

# clear()------------>  Removes all the elements from the dictionary
# copy()------------->  Returns a copy of the dictionary
# fromkeys()--------->  Returns a dictionary with the specified keys and value
# get()-------------->  Returns the value of the specified key
# items()------------>  Returns a list containing a tuple for each key value pair
# keys()------------->  Returns a list containing the dictionary's keys
# pop()-------------->  Removes the element with the specified key
# popitem()---------->  Removes the last inserted key-value pair
# update()----------->  Updates the dictionary with the specified key-value pairs
# values()----------->  Returns a list of all the values in the dictionary
# setdefault()------->  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value



# Empty Dictionary
empty = {}
print("Empty Dictionary is :", empty)

print("------------------------------")

# Update Method
employee1 = {101: "Parth", 102: "Kevin", 103:"Hevin", 104:"Mayur", 105:"Prince"}
employee2 = {106: "Vishal", 107:"Renish", 108:"Bharat"}
employee1.update(employee2)
print(employee1)

print("------------------------------")

# Clear Method
employee3 = {101: "Parth", 102: "Kevin", 103:"Hevin", 104:"Mayur", 105:"Prince"}
employee3.clear()
print("Clear Dictionary is :", employee3)

print("------------------------------")

# Pop Method
employee4 = {1001: "Parth", 1002: "Renish", 1003:"Vishal", 1004:"Bharat"}
employee4.pop(1003)
print("Pop Method is :", employee4)

# Popitem method dictionary ni chheli key:value delete kare chhe.
employee4 = {1001: "Parth", 1002: "Renish", 1003:"Vishal", 1004:"Bharat"}
employee4.popitem()
print("Popitem Method is :", employee4)

print("------------------------------")

# Del keyword Metho
employee5 = {1001: "Parth", 1002: "Renish", 1003:"Vishal", 1004:"Bharat"}
del employee5[1001]
print("Delete method is :", employee5)



