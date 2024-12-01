# num1 = int(input("ENter The Start Number :"))
# num2 = int(input("ENter The End Number :"))
# for j in range(num1, num2):
#     for i in range(1, 11):
#         print(num1, "X", i, "=", num1 * i)
#     print(j)



for i in range(1, 11):
    print("\nMultiplication table of %d" %(i))
    for j in range(1, 11):
        # print(num1, "X", i, "=", num1 * i, i*j)
        print("%-5dX%5d =%5d" % (i, j, i*j))