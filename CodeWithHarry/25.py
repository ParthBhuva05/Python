# Operators on tuple in python


# Tuple Method	Description

# count()---->	Returns the number of times a specified value      occurs in a tuple

# index()----> 	Searches the tuple for a specified value and returns the position of where it was found
# syntax---> tuple.index(element, start, end)




contries = ("Spain", "Italy", "India", "England", "Germany")
a = list(contries)
a.append("Russia") 
# a.pop[3]
# a[2] = "Finland"
contries = tuple(a)
print(contries)


tuple1 = ("apple", "banana", "oramge", "mango")
tuple2 = ("watermelon", "kiwi","graps")
tuple3 = tuple1 + tuple2
print(tuple3)


# Tuple ma aek ne aek item ketli vakhat ripit thy chhe te jova mate count vapray
tuple4 = (0, 1, 2, 3, 2, 3, 6, 3, 7, 8,3)
x = tuple4.count(3)
print("Count of 3 is in tuple is :", x)


# tuple na element no kram jova mate index no use thay chhe
tuple5  = (0, 1, 2, 7, 2, 9, 6, 3, 7, 8,3)
y = tuple5.index(3)
print("Index of 3 is :", y)
y = len(tuple5)
print("Lenght of tuple is :", y)


