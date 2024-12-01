# Set Method in Python



# Set Method	                Description

# add()---------------------->  Adds an element to the set 


# clear()-------------------->  Removes all the elements from the set

# copy()--------------------->  Returns a copy of the set

# difference()--------------->  Returns a set containing the difference between two or more sets

# difference_update()-------->  Removes the items in this set that are also included in another, specified set

# discard()------------------>  Remove the specified item

# intersection()------------->  Returns a set, that is the intersection of two other sets

# intersection_update()------>  Removes the items in this set that are not present in other, specified set(s)

# isdisjoint()--------------->  Returns whether two sets have a intersection or not

# issubset()----------------->  Returns whether another set contains this set or not

# issuperset()--------------->  Returns whether this set contains another set or not

# pop()---------------------->  Removes an element from the set

# remove()------------------->  Removes the specified element

# symmetric_difference()----->  Returns a set with the symmetric differences of two sets

# symmetric_difference_update()-------->  inserts the symmetric differences from this set and another

# union()-------------------->  Return a set containing the union of sets

# update()------------------->  Update the set with the union of this set and others



set1 = {1, 2, 5, 6}
set2 = {3, 6, 7}
print(set1.union(set2))
set1.update(set2)
print(set1, set2)

print("------------------------------")

# Union
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3= cities1.union(cities2)
print("Union is :", cities3)

# Union Update
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.update(cities2)
print("updater is :", cities1)

print("------------------------------")

# Intersection 
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities4 = cities1.intersection(cities2)
print("Intersection is :", cities4)

# Intersection Update
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.intersection_update(cities2)
print("Intersection_update is :",cities1)

print("------------------------------")

# symmetric_difference and symmetric_difference_update
# symmetric_difference
cities6 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities7 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities5 = cities6.symmetric_difference(cities7)
print("symmetric_difference is :", cities5)

# symmetric_difference_update
cities6.symmetric_difference_update(cities7)
print("symmetric_difference_update is :", cities6)

print("------------------------------")

# Difference
cities6 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities7 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities8 = cities6.difference(cities7)
print("Difference is :",cities8)

# Difference_update
cities6.difference_update(cities7)
print("Difference_update is :", cities6)

print("------------------------------")

# Disjoint set
x = {"apple", "banana", "cherry"}
y = {"orange", "watermelon", "mango"}
z = x.isdisjoint(y) 
print("Disjoint set is :", z)

print("------------------------------")

# Super set
parth1 = {"apple", "banana", "mango", "watermelon", "orange", "graps"}
parht2 = {"banana", "graps", "watermelon"}
print("super set is :", parth1.issuperset(parht2))

parth3 = {"mango", "graps", "orange", "kiwi"}
print("super set is :", parth1.issuperset(parth3))

print("------------------------------")

# Sub set
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print("sub set is :", z)

a = {"x", "y", "z"}
b = {"f", "g", "p", "x", "z", "c", "q"}
c = a.issubset(b)
print("sub set is :", c)

print("------------------------------")

# Add Method
parth4 = {"ahmedabad", "mumbai", "surat", "junagadha"}
parth4.add("rajkot")
print("Add Method is :", parth4)

print("------------------------------")

# Remove & Discard Method
parth5 = {"ahmedabad", "mumbai", "surat", "junagadha"}
# Error throw karse
parth5.remove("mumbai")
print("Remove Method is :", parth5)

parth5 = {"ahmedabad", "mumbai", "surat", "junagadha"}
# Error throw nathi kartu
parth5 .discard("surat")
print("discard Method is :", parth5)

print("------------------------------")

# Pop Method 
parth6 = {"ahmedabad", "mumbai", "surat", "junagadha"}
x = parth6.pop()
print("Pop Item is :", x)
print("Pop Method is :", parth6)

print("------------------------------")

# Del - Keyword Method
parth7 = {"ahmedabad", "mumbai", "surat", "junagadha"}
del parth7
# print(parth7)
# when run a del method is show an error because set is deleted.

print("------------------------------")

# Clear Method
parth8 = {"ahmedabad", "mumbai", "surat", "junagadha"}
parth8.clear()
print("Clear Method is :", parth8)

print("------------------------------")

# Check if item exists
info = {"ram", 19 ,"ravan", 45.50, 4534, "ramesh"}
if "ram" in info:
    print("ram is present.")
else:
    print("ram is not present.")

