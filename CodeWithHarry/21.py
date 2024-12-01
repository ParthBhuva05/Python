# Function Argument in python


def average(a, b):
    print("The average is ",(a + b)/2)
average(9, 8)


# Default Argument
print("The Default Argument Start:")

def name( fname, mname = "parht",lname = "bhuva" ):
    print("Hello, good morning",fname, mname, lname)
name("Mr")
name("Mr", "ram", "narayan")


# Keyword Argument
print("The Keyword Argument Start:")

average(b=9, a=21)


# Required Argumen
print("The Required Argument Start:")

def average(x, y, z = 8):
    print("The average is ",(x + y +z)/3)
average(5, 6)



# Variable length Argument
print("The variable length Argument Start:")
def average (*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is:",sum/len(numbers))
    return sum/len(numbers)

c = average(5, 6, 7, 1)
print(c)
