# Match case statement in python

# To implement switch-caes like characteristics very similar to if-else functionality, we use a match case in python.

# A match statement will compare a given variable's value to different shapes, also referred to as the pattern. the man idea is to keep on comparing the variable with the present patterns unitl it fits inti one.

# The match case consists of three main entities:
# 1) The match keyword
# 2) One or more case clauses
# 3) Expression for each case

# The caes clause consists of a pattern to be matched to the variable,acondition to be evluated if the pattern matches, and a set of statements to be executed if the pattern matches.


x = int (input("Enter the value of x : "))
match x :
    case 0:
        print("x is zero")
    case 4:
        print("caes is 4")
    case _ if x!=90:
        print("x, is not 90")
    case _ if x!=80:
        print("x, is not 80")
    case _ :
        print(x) 