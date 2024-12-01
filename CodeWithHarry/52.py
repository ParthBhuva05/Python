# Lambda function in python


#   In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:


# SYNTAX---------------------------
#   lambda arguments: expression


#   Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

#   The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.


# Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with multiple arguments:

# Lambda functions can also include multiple statements, but they are limited to a single expression.

# In the above example, the lambda function includes a print statement, but it is still limited to a single expression.

# Lambda functions are often used in conjunction with higher-order functions, such as map, filter,



print("Simple Functio")
def double(x):
    return x*2 
print(double(5))


print("Lambda Functio")

double = lambda x: x*2
print(double(5))

cube = lambda x: x*x*x
print(cube(5))


ave = lambda x, y, z: (x + y + z)/3
print("Average is: ", ave(3, 5, 10))


def apple(fx, value):
    return 6 + fx(value)
print(apple(cube, 2))
print(apple( lambda x: x*x*x, 2))


