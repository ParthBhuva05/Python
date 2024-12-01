# Walrus Operator in Python

# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

# The Walrus Operator is represented by the syntax and can be used in a variety of contexts including while loops and if statements.

# Here's an example of how you can use the Walrus Operator in a while loop:


# numbers = [1, 2, 3, 4, 5]

# while(n = len(numbers)) > 0: 
#     print(numbers.pop())

# In this example, the length of the numbers list is assigned to the variable n using the Walrus Operator. The value of n is then used in the condition of the while loop, so that the loop will continue to execute until the numbers list is empty.




a = True
print(a := False)


number = [1, 2, 3, 4, 5]
while (n := len(number)) >0 :
    print(number.pop())



# New to python 3.8.

# Assignment expression aka walrus operator.
    
# Assigns values to variables as part of a larger expression.  



happy = False
print(happy)

print(happy := True)


# foods = list()
# while True:
#     food = input("What Food Do You Like? : ")
#     if food == "quit":
#         break
#     foods.append(food)


foods = list()
while (food := input("What Food Do You Like? : ")) != "quit":
    foods.append(food)


# In this example, the user input is assigned to the variable name using the walrus operator. the value of name is then used in the if statement to determine whether it is in the names list. if it is, the corresponding message is printed, otherwise, a different message is printed.
    
# It is important to note that the walrus operator shiuld be used sparingly as it can make code less readable if overused.
    
# In conclusion, the walrus Operator is a useful tool for python developers to have in their tookit. it can helps streamline code and reduce duplication, but it should be used with care to ensure code readability and maintainability. 








