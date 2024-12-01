# Class and Oblect in python


# CLASS -----

# Aclass is a blueprint or a template for creating objects, providing initial value for state (member variabels or attributes), and implementations or behavior (member function or method). the user defind objects are created using class keyword.  



# OBJECT -----

# A object is a instance of the class used to access the properties of the class now lets create an object of the class.



# SELF PARAMETER -----

# The self parameter is a reference to the current instance of the class,and is used to access variables that belongs to the class.

# It must be provided as the extra parameter inside the method definition.



class person:
    name = "Parht"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()

a.name = "Harry"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "Human Resource"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()






