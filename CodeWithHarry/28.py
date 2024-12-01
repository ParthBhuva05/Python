# F-String  in python

letter = "Hey my name is {1} and I am from {0}."
country = "India"
name = "parth"
print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")


price = 49.099878
text = f"For only {price:.3f} dollars!"
print(text)

print(type(f"{2*30}"))

