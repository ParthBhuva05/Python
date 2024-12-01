# Dir, __dict__ and help Method in python 

# dir(), diet and help() methods in python

# We must look into dir(), dict() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help(), Let's take a look at each of them:

# The dir() method

# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. Example:

print("The dir method is a start.----------------------------------------")
x = [1, 2, 3]
print(dir(x))

print(x.__add__)




# The __dict__ attribute

# __dict__: The __dict__ attribute returns a dictionary representation of an object's attribute. It is useful tool for introspection.


print("The dict attribut is a start.----------------------------------------")
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = person("Parth", 18)
print(person1.__dict__)



# The help() method 

# help(): The help() function is used to get help documentation an object, including a description of its attributes and methods.

print("The help functio is a start.----------------------------------------")
print(help(person))



# Conclusion

# dir(), dict() and help() are useful built-in functions in python that can be used th get information about objects. they are valuable tools for introspection and discovery.



