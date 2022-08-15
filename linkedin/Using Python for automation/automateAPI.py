from email.mime import base
import json
import requests

# Create API requests
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc':'0885909950805'}
response = requests.get(baseUrl, params=parameters)

# Parsing through JSON
content = response.content
info = json.loads(content)
itemInfo = info['items']
item = itemInfo[0]
title = item['title']
brand = item['brand']
print(title, brand)

# Using API keys
baseUrl = 'http://api.openweathermap.org/geo/1.0/direct'
parameters = {'appid':'32066a7b4550d8a6dd6ca785d5a3c80b', 'q':'London'}
response = requests.get(baseUrl, params=parameters)
print(response.text)