# read(), readlines() and other method in python


# readlines() method

# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# The readlines() method reads all the lines of the file and returns them as a list of strings.




# writelines() method

# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.




f = open('CodeWithHarry\myfile_50_1.txt', 'r')
while True :
    line = f.readline()
    if not line:
        break 
    print(line)



f = open('CodeWithHarry\myfile_50_2.txt', 'r')
i = 0
while True :
    i = i + 1
    line = f.readline()
    if not line:
        break 
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"gujrati of student {i} in maths is: {m1*2}")
    print(f"hindi of student {i} in maths is: {m2*2}")
    print(f"english of student {i} in maths is: {m3*2}")

    print(line)


# Writeline()

# f = open('CodeWithHarry\myfile_50_3.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n']
# f.writelines(lines)
# f.close()


f = open('CodeWithHarry\myfile_50_3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n']
for line in lines:
    f.writelines(line + '\n')
f.close()