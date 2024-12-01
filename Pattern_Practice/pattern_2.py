# Right Triangle Pattern

num2 = int(input("Enter The Number :"))

for i in range(0, num2):
    for j in range(0, i + 1):
        print("*",end=" ")
    print("")


# Inverted Right Triangle Pattern

num3 = int(input("Enter The Number :"))
for i in range(num3, 0, -1):
    for j in range(1, i + 1):
        print("*",end=" ")
    print("")






# Left Triangle Pattern

num1 = int(input("Enter The Number :"))
for i in range(0, num1):
    for j in range(0, num1-i):
        print(" ", end=" ")
    for k in range(0, i+1):
        print("*", end=" ")
    print("")


# Inverted Left Triangle Pattern

num2 = int(input("Enter The Number :"))
for i in range(num2, 0, -1):
    for j in range(0, num2 - i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print("*", end=" ")
    print("")
