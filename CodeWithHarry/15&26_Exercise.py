# Exercise_2: Good Morning Sir



import time

# Some Information

# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)


num = int(input("Enter your value is : "))
if (num >= 6 and num <= 10):
    print("Good Morning Sir.")
elif (num >= 11 and num <=17):
    print("Good Afternoon Sir.")
elif (num >= 18 and num <= 22):
    print("Good Evening Sir.")
else:
    print("No Set,Default.")




t = time.strftime('%H:%M:%S')
hour = int (time.strftime('%H'))
hour = int (input("Enter hour :"))
print(hour)


if (hour>=0 and hour<12):
    print("Good Morning Sir !")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir !")
elif(hour>=17 and hour<0):
    print("Good Night Sir !")
    