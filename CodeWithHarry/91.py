# Generator in Python

# Generators in Python are special type of functions that allow you to create an iterable sequence of values. A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets, as they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.

# Creating a Generator

# In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested. Here's an example:

# def my_generator(): 
#     for i in range(5):
#         yield i

# As you can see, the generator function my_generator() returns a generator object, which can be used to generate the values in the range 0 to 4. The next() function is used to request the next value from the generator, and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.


# Using a Generator

# Once you have created a generator, you can use it in a variety of ways, such as in a for loop, a list comprehension or a generator expression.


# gen = my_generator()
# for i in gen:
#     print(i)


# As you can see, the generator can be used in a for loop, just like any other iterable sequence. the generator is used to generat the values one-by-one as the loop iterates over it.


# Conclusions

# Generators in Python are a powerful tool for working with large or complex data sets, allowing you to generate the values on-the-fly and store only what you need in memory. Whether you are working with a large dataset, performing complex calculations, or generating a sequence of values, generators are a must-have tool in your programming toolkit. So, if you haven't already, be sure to check out generators in Python and see how they can help you write better, more efficient code.



def my_generator():
    for i in range(500):
        yield i 

gen = my_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)







