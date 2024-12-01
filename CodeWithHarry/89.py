# Requests Module in Python

# The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.



# Installation

# pip install requests



# Get Request

# Once you have installed the Requests module, you can start using it to send HTTP requests. Here is a simple example that sends a GET request to the Google homepage:



import requests


# response = requests.get("https://www.google.com")
# print(response.text)

# print("-----------------------------------------------------------------------------------")
# import requests
# response = requests.get("https://codewithharry.com")
# print(response.text)



# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'Parht',
#     "body": 'Bhai',
#     "userId": 12,
#   }

# headers = {'Content-type': 'application/json; charset=UTF-8',}

# response = requests.post(url, headers=headers, json=data)

# print(response.text)



# bs4 module

# There is another module called beautifulsoup which is used for web scraping in python. I have personaliy used bs4 module to finish a lot of freelancing task.


from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
for heading in soup.find_all("h2"):
    print(heading.text)


