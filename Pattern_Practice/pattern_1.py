# Square Pattern

num1  = int(input("Enter The Number :"))
for i in range(num1):
    for j in range(num1):
        print("*", end=" ")
    print()




# Square print

size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()





