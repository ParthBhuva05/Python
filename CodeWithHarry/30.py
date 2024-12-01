# Recursion in python

# Recursion is the process of defining something in terms of itself.

# A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

# In python, We known that a function can call other functions. It is even possible for the function to call itself. these types of construct are termed as recursive functions.


def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
print(factorial(4))
print(factorial(3))



# Quick Quiz : Fibonacci sequence
# F(0) = 0 
# F(1) = 1
# F(2) = f(1) + f(0)
# F(n) = f(n-1) + f(n-2)


# def fibonacci_sequence(x):
x = 20
f0 = 0
f1 = 1
next_number = f1
count = 0
while count <= x:
    print(next_number, end="  ")
    count += 1
    f0, f1 = f1, next_number
    next_number = f0 + f1 
# print()