# Inheritance in python


# When a class derived from another class. the child class will inherit all the public and protected properties and methods from the partnt class. it can have its own properties and metods, this is called as inheritance.

# Inheritance Syntax -----

# class BassClass:
#     body of base class
# class derivedClass(BassClass):
#     body of derived class

# Derived class inherits features from the base class where new features can be added ti it. this results in re-usability of code

# Types of Inheritance

# 1-- Single Inheritance
# 2-- Multiple Inheritance
# 3-- multilevel Inheritance
# 4-- Hierarchical Inheritance
# 5-- Hybrid Inheritance



class Employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("The dedfault language is python")

e1 = Employee("parth", 400)
e1.showDetails()
e2 = programmer("Harry", 401)
e2.showDetails()
e2.showLanguage()


