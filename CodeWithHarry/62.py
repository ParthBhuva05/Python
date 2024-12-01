# Access Specifiers/Modifiers

# access specifiers and access modofiers in python programming are used to limit the access of the class variables and class methods outside of class while implementing the concept of inheritance.

# let us see the each of access specifiers in details:

# Type of access Modifiers

# 1 --- Public access Modifier
# 2 --- Private access Modifier
# 3 --- Protected access Modifier


# Public access Modifiers ----------
# All the variables and methods (member functio) in python are by default public. any instance variables in a class followed by the 'self' keyword 

print("Public access Modifiers ----------")
class Employee:
    def __init__(self):
        self.name = "Parht"

a = Employee()
print(a.name)



# Private access Modifiers ----------

# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.


# Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.

# Name mangling

# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.


print("Private access Modifiers ----------")
class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()
# print(a.__name)  # can not be accessed directly 
print(a._Employee__name)  ## can be accessed indirectly


print(a.__dir__())




# Protected Access Modifier ----------

# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore. For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (ie. varName.




print("Protected access Modifiers ----------")
class student:
    def __init__(self):
        self._name = "lalji master"
    
    def _funName(self):
        return "CodeWithHarry"

class subject(student):
    pass

obj1 = student()
obj2 = subject()



print(obj1._name)
print(obj1._funName())

print(obj2._name)
print(obj2._funName())

print(dir(obj1))



