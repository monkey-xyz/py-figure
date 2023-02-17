import requests
from bs4 import BeautifulSoup

response = requests.get('https://myfigurecollection.net/')
soup = BeautifulSoup(response.content, 'html.parser')

print(response.text)
