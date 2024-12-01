# enumerate function in python

# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.


# marks = [12, 56, 32, 98, 12, 45, 1, 4]
# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Parth, Awesome !")
#     index +=1



marks = [12, 56, 32, 98, 12, 45, 1, 4]
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Parth, Awesome !")

print("--------------------Second Methom Start--------------------")

marks = [12, 56, 32, 98, 12, 45, 1, 4]
for index, mark in enumerate(marks, start = 1):
    print(mark)
    if (index == 3):
        print("Parth, Awesome !")


