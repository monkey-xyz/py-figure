import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Sample URL for testing
url_to = 'https://myfigurecollection.net/browse.v4.php?mode=search&rootId=0&status=-1&categoryId=-1&orEntries[]=1590&domainId=-1&noReleaseDate=0&releaseTypeId=0&ratingId=0&isCastoff=0&hasBootleg=0&tagId=0&noBarcode=0&clubId=0&isDraft=0&year=2023&month=2&acc=0&separator=0&sort=insert&output=2&current=categoryId&order=desc&page='

response = requests.get(url_to)

soup = BeautifulSoup(response.content, 'html.parser')

end_page = soup.find('a', class_='nav-last').get('href')

"""
TO DO

Format the data.
"""
names = []
icons = []
urls = []

# Maybe add an extra method to get the official images from the figure entry as well sometime.

def get_last(page):
  q = urlparse(page)
  return int(q.query.rsplit('=', 1)[1])

for pages in range(1, get_last(end_page)):
  response = requests.get(url_to + str(pages))
  soup = BeautifulSoup(response.content, 'html.parser')

  print(soup.find_all('span',_class='item-icon'))

  for entries in soup.find_all('span', _class='item-icon'):
    print(entries)
  
