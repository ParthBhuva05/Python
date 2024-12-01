print("----------1----------")
# Row Number Print
# num1 = int(input("Enter The Number :"))
num1 = 5
for i in range(1, num1 + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()



print("----------2----------")
# Row Number Print
# num3 = int(input("Enter The Number :"))
num3 = 5
for i in range(num3, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()



print("----------3----------")
# Row Number Print
# num4 = int(input("Enter The Number :"))
num4 = 5
p = 0
for i in range(num4, 0, -1):
    p += 1
    for j in range(1, i + 1):
        print(p, end=" ")
    print()



print("----------4----------")
# Column Number Print
# num5 = int(input("Enter The Number :"))
num5 = 5
for i in range(1, num5 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()