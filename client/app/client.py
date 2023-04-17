import requests

response = requests.get('http://server:5000/')
print(response.text)
