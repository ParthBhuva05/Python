# os Module in Python

# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

# Here are some common tasks you can perform with the os module:

# Reading and writing files The os module provides functions for opening, reading, and writing files. For example, to open a file for reading, you can use the open function:




import os 

if (not os.path.exists("CodeWithHarry/data_46-Video")):
    #  "mkdir" method folder create kare chhe.
    os.mkdir("CodeWithHarry/data_46-Video")


for i in range(0, 100):
    # os.mkdir(f"CodeWithHarry/data_46-Video/Day{i+1}")

    # # "rename" method name ne change kare chhe.
    # os.rename(f"CodeWithHarry/data_46-Video/Tutorial{i+1}", f"CodeWithHarry/data_46-Video/Tutorial_{i+1}")

    folders = os.listdir("CodeWithHarry/data_46-Video")
# print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"CodeWithHarry/data_46-Video/{folder}"))


# print(os.getcwd())
# os.chdir("CodeWithHarry/data_46-Video")





