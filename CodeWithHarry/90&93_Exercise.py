# Exercise_10: News App in Python

# Use the newsAPI and the requests module to fetch the daily news related to different topics. 

# Go To : http://newsapi.org/

# And explor the various options to build your application.



import requests
import json
query = input("What type of news are you interested in ?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-29&sortBy=publishedAt&apiKey=87182320b0994296be8cc7d400feee73"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------------------")







