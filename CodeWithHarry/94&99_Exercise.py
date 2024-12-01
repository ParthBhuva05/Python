# Exercise_10: Drink Water Reminder in Python

# Drink Water Reminder

# Write a python program which reminds you of drinking water every hour or two. you program can either beep or send desktop notifications for a specific operating system. 



# pip install win10toast
# from win10toast import ToastNotifier
# toast = ToastNotifier()
# toast.show_toast("Notification", "Hay Parth You Drink a Water", duration = 5, icon_path = "icon.ico", threaded = True,)



import time
import os
from win10toast import ToastNotifier

Repeat_Interval = 10

while True:
    toast = ToastNotifier()
    toast.show_toast("Notification", "Hay Parth You Drink a Water")

    os.system(toast)
    time.sleep(Repeat_Interval)
    











