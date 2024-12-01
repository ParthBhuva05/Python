# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# # Example usage:
# number = 5
# print("Factorial of", number, "is", factorial(number))


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


number = 4 
print(factorial(number))


square = lambda x: x**2
result = square(5)
print("square of 5 is:", result)




try:
    num = int(input("Enter a number: "))
    result = 10/num
    print("result: ", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("cannot divide by zero.")