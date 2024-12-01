# is vs == in python



a = 3
b = 3
print(a is b) #exact location of objecit in memory
print(a == b)  # value
print("----------------------------------------Frist Complete")

a = None
b = None
print(a is b) # Compare to the exact location of objecit in memory
print(a == b)  # Compare to the value
print("----------------------------------------Second Complete")


a = 4
b = "4"
print(a is b) # Compare to the exact location of objecit in memory
print(a == b)  # Compare to the value
print("----------------------------------------Thired Complete")


a = [1, 2, 43]
b = [1, 2, 43]
print(a is b) # Compare to the exact location of objecit in memory
print(a == b)  # Compare to the value
print("----------------------------------------Fourth Complete")










