# Constructors in python

# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Syntax of Python Constructor

# def_init__(self):
# #initializations

# init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor. We can also create constructor by defining the function name with same class name.

# init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.


# Types of Constructors in Python
# 1. Parameterized Constructor
# 2. Default Constructor



# Parameterized Constructor in Python

# When the constructor accepts arguments along with self, it is known as parameterized constructor.



# Default Constructor in Python

# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.




class person:
    
    def __init__(self, name, occupation):
        print("Hey i am a person")
        self.name = name
        self.occ = occupation
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Parht", "Developer")
b = person("Divya", "Human Resource")
a.info()
b.info()
        









