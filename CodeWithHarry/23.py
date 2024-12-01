# List Method in python

# list Method	  Description

# append()----->  Adds an element at the end of the list
# clear()------>  Removes all the elements from the list
# copy()------->  Returns a copy of the list
# count()------>  Returns the number of elements with the specified value
# extend()----->  Add the elements of a list (or any iterable), to the end of the current list
# index()------>  Returns the index of the first element with the specified value
# insert()----->  Adds an element at the specified position
# pop()-------->  Removes the element at the specified position
# remove()----->  Removes the item with the specified value
# reverse()---->  Reverses the order of the list
# sort()------->  Sorts the list


# List ni end ma element add karva mate
list = [1, 2, 4, 6]
print(list)
list.append(7)
print("Append list is :", list)


# List na element ne lainma & kram ma print karva mate
list1 = [11, 45, 1, 2, 4, 6]
print(list1)
list1.sort()
print("Sort list is :",list1)

# list ne reverse karva mate
list2 = [11, 45, 1, 2, 4, 6]
list2.reverse()
print("Reverse list is :", list2)

# list ma element no index kyo chhe jova mate
list3 = [11, 45, 1, 2, 4, 6]
print(list3.index(1))

# list ma aek no aek element ketli vakhat aave chhe te count karva mate 
list4 = [11, 45, 1, 2, 1, 4, 1, 6, 1]
print(list4.count(1))

# List ne copy karva mate
list5 = [11, 45, 1, 2, 1, 4, 1, 6, 1]
print(list5)
mylist = list5.copy()
print("Mylist is :", mylist)

# list ma index mujab element add karva mate
list6 = ["apple", "banana", "mango", "kiwi"]
list6.insert(2, "watermelon")
print("Insert list is :", list6)

# aek list ne bija list ma add karva mate
list6 = ["apple", "banana", "mango", "kiwi"]
list7 = [900, 1000, 10000, 100000]
# Extend method one :
# list6.extend(list7)
# print(list6)

# Extend method two :
list8 = list6 + list7
print("Extend list is :", list8)


# List ne clear karva mate
list9 = ["parth", "kevin", "hevin", "jay"]
list9.clear()
print("Clear list is :", list9)


# List ne remove karva mate
list10 = ["parth", "kevin", "hevin", "jay"]
# Frist method :
# list10.remove("jay")
# print("remove list is :", list10)

# Second method :
list10.pop(1)
print(list10)