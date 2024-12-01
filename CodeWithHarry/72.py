# Super Keyword in Python


# Super keyword in Python

# The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

# When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.




class parentClass:
    def parent_metnod(self):
        print("This is a parent method.")


class childClass(parentClass):

    def parent_metnod(self):
        print("Parht")
        super().parent_metnod()

    def child_method(self):
        print("This is a child method.")

        super().parent_metnod()


child_object = childClass()
child_object.child_method()
child_object.parent_metnod()



print("--------------------SECOND EXAMPLE--------------------")

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self,name, id, language):
        super().__init__(name, id)
        self.language = language

Parth = Employee("Parth", 302)
Harry = Programmer("Harry", 304, "Python")

print(Harry.name)
print(Harry.id)
print(Harry.language)


