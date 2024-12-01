# Exercise_9: Shoutouts to Everyone


# Write a program to pronounce list of names using Win32 API. If you are given a list L as follows.

L = ["Rahul", "Nishant", "Harry"]

# your program should pronounce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

# Note: ---> If you are not using windows, try to figure out how to do the same thing using some other package.  




import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = ["Parth Bhuva", "Code with harry", "Renish Buva", "Ramesh smju", "Elvish bhai"]
for name in names:
    speaker.speak(f"{name} Welcome to the millionaire life")






    