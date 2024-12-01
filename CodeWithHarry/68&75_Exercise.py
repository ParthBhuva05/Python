# Exercise_7: Clear The Clutter


# Write a program to cler the clutter inside a folder on your computer. you shoulduse os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for another file formats.



# import os

# files = os.listdir("CodeWithHarry\Images_74-video")
# i = 1
# for file in files:
#     if file.endswith(".png"):
#         print(file)
#         os.rename(f"CodeWithHarry\Images_74-video/{file}", "CodeWithHarry\Images_74-video/{i}.png")
#         i=i+1



import os 

files = os.listdir("CodeWithHarry\Images_74-video")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"CodeWithHarry\Images_74-video/{file}", f"CodeWithHarry\Images_74-video/{i}.png")
        i = i + 1
