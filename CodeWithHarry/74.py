# Method Overriding in Python


# Method Overriding in Python

# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

# In Python, method overriding is a way to customize the behavior of a class based on its specific needs. For example, consider the following base class:

# class Shape: 
#     def area(self): 
#         pass

# In this base class, the area method is defined, but does not have any implementation. If you want to create a derived class that represents a circle, you can override the area method and provide an implementation that calculates the area of a circle:



class Shape: 

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self): 
        return self.x * self.y

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()



rec = Shape(3, 5)
print(rec.area())

c = circle(5)
print(c.area())



