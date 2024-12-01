# String method in python 

a = "!!!Harry!!!! !!!!! !!parth"
print(len(a))
print(a.upper())
print(a.lower())

# removes any trailing character & string ni pachhad na vadharana character ne kadhi nakhe chhe 
print(a.rstrip("!"))

# string ne replace kare chhe
print(a.replace("Harry","parth"))

# split string ne list ma convert kare chhe
print(a.split(" "))

# string no frist character upper case tay jay chhe
blogheading = "introduction to javascript"
print(blogheading.capitalize())

# string ne center kare chhe 
str1 = "Welcome to the console!!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))

# string ma aek no aek sabd ketli vakhat aave chhe te count kare chhe 
print(a.count("Harry"))

# string na end ma koi character aave chhe ke nay te chakasi sako chho.  
str2 = "Welcome to the console!!!"
print("endswith is :",str2.endswith("!!!"))

# string na start ma koi character aave chhe ke nay te chakasi sako chho.  
str2 = "!!Welcome to the console!!!"
print("startswith is :",str2.startswith("!!"))

# string na character no index print kare chhe
str3 = "He's name is Dan. He is an honest man."
print(str3.find("is"))

# string no index print kare chhe
print(str3.index("honest"))

# aa string alphabets and number hoy to j true return karse nahi to false
str4 = "WelcomeToTheConsole"
print(str4.isalnum())

# aa string alphabets hase to j true return karse nahi to false 
str5 = "Welcome"
print(str5.isalpha())

# aakhi string lower case ma hase to j true return karse nahi to false 
str6 = "hello world"
print("lower case is :",str6.islower())

# aakhi string upper case ma hase to j true return karse nahi to false 
str6 =  "HELLO WORLD"
print("upper case is :",str6.isupper())

# printable character hoy to j true return karse nahi to false
str7 = "We Wish you a merry christmas"
print(str7.isprintable())

# whitespace hase to j true return karse nahi to false
str8 = "            "
print("whitespace is :",str8.isspace())

# string na sabda na frist character ne upper case hase to j true return karse nahi to false
str9 = "World Health Organization"
print(str9.istitle())

# string na upper case ne lower case ma and lower case ne upper case ma ferve chhe
str10 = " Python is a Interpreted Language"
print(str10.swapcase())

# string na words na frist character ne upper case ma convert kare chhe  
str11 = "His name is Dan. Dan is an honest man."
print(str11.title())

