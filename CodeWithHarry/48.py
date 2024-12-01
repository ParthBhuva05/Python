# Local and Globle variable in python

x = 4
print(x)

def hello():
    x = 5 
    print(f"The Local x is {x}")
    print("Hello parth")

print(f"The Globle Variable x is {x}")
hello()
x = 6           
print(f"The Globle x is {x}")



a = 10 

def my_function():
    z = 5
    print(z)

my_function()
print(a)
# print(z) # this is through the erroe when the run a code.


print("------------------------------")

p = 100
print("Outside function variable is:", p)

def my_function():
    global p
    p = 200
    h = 50 
    print(h)

my_function()
print(p)

