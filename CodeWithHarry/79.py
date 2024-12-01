# Multiple Inheritance in Python

# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

# Syntax

# In Python, multiple Inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.

# -------------------------------------------------------------

# class ChildClass(ParentClass1, ParentClass2, ParentClass3): 
#     class body

# -------------------------------------------------------------

# In this example, the ChildClass Inherits attributes and methods from all three parent classes: ParentClass1, ParentClass2, and ParentClass3.

# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.




class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Dancer, Employee):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name 


o = DancerEmployee("kathak", "shivani")
print(o.name)
print(o.dance)


o.show()
print(DancerEmployee.mro())





