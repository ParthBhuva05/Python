# Find The Fibonacci Sequence


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