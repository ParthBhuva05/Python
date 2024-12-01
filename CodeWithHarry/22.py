# Introduction to Lists in python

list = ["apple", "banana", "orange"]
print(list)

list1 = [3, 5, 7]
print(list1)
print(len(list1))
print(type(list1))
print(list1[0])
print(list1[1])
print(list1[2])

if 7 in list1:
    print("Yes")
else:
    print("No")


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
print(list2)
print(len(list2))
print(list2[0:10:2])
print(list2[0:10:3])

# List comprehension

print("List Comprehension is a Start :")
list3 = [i*i for i in range(10)]
print(list3)
list3 = [i*i for i in range(10) if i%2==0]
print(list3)

fruit = ["apple", "banana", "kiwi", "mango", "cherry",]
newlist = [x for x in fruit if "a" in x]
print(newlist)



