# Map, Filter and Reduce in python 


# Map, Filter and Reduce

# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.




# map

# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

# SYNTAX---------------------------
# map(function, iterable)

# The function argument is a function that is applied to each element in the Iterable argument. The iterable argument can be a list, tuple, or any other iterable object.




# filter

# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

# SYNTAX---------------------------
# filter(predicate, (terable)

# The predicate argument is a function that retums a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.




# reduce

# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

# SYNTAX---------------------------
# reduce(function, (terable)

# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.





# MAP function part
def cube(x):
    return x * x * x
print(cube(2))



print("Map() function is start")
list1 = [1, 2, 4, 6, 4, 3]
# list2 = []
# for item in list1:
#     list2.append(cube(item))

list2 = list(map(lambda x: x*x*x, list1))
print(list2)






# FILTER function part
print("Filter() function is start")

def filter_function(a):
    return a>3
newlist3 = list(filter(filter_function, list1))
print("Filter list is: ", newlist3)






# REDUCE function part
print("Reduceṇ() function is start")

from functools import reduce
numbers = [1, 2, 3, 4, 5]
def mysum(x, y):
    return x + y
sum1 = reduce(mysum, numbers)
print(sum1)

sum2 = reduce(lambda x, y: x + y, numbers)
print(sum2)








