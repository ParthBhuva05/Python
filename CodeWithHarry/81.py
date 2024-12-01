# Hybrid and Hierarchical Inheritance in Python



# Hybrid Inheritance in Python

# Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

# In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

# Hybrid Inheritance Example
class Baseclass:
    pass

class Derivedclass1(Baseclass):
    pass

class Derivedclass2(Baseclass):
    pass

class Derivedclass3(Derivedclass1, Derivedclass2):
    pass





# Hierarchical Inheritance

# Hierarchical Inheritance is a type of inheritance in Object- Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner.

# Hierarchical Inheritance Example


class Baseclass:
    pass

class DerivedClass1(Baseclass):
    pass

class DerivedClass2(Baseclass):
    pass

class Derivedclass3(DerivedClass1):
    pass

class Derivedclass4(Derivedclass1):
    pass

class Derivedclass5(Derivedclass2):
    pass

class Derivedclass6(Derivedclass2):
    pass





