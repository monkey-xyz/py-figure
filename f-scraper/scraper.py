import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Sample URL for testing
url_to = 'https://myfigurecollection.net/browse.v4.php?mode=search&rootId=0&status=-1&categoryId=-1&orEntries[]=1590&domainId=-1&noReleaseDate=0&releaseTypeId=0&ratingId=0&isCastoff=0&hasBootleg=0&tagId=0&noBarcode=0&clubId=0&isDraft=0&year=2023&month=2&acc=0&separator=0&sort=insert&output=2&current=categoryId&order=desc&page='

"""
TO DO

Format the data.
"""

figure_entries = []

# Maybe add an extra method to get the official images from the figure entry as well sometime.

def get_last(page):
  q = urlparse(page)
  return int(q.query.rsplit('=', 1)[1])

for pages in range(1, 20):
  resp = requests.get(url_to + str(pages))
  soup = BeautifulSoup(resp.content, 'html.parser')
  entry = soup.find_all('span', class_='item-icon')

  for i in range(len(entry)):
    f_name = entry.find('img').get('alt')
    f_link = entry.find('a').get('href')
    
    fr = requests.get(f_link)
    fs = BeautifulSoup(fr.content, 'html.parser')
    f_img = soup.find_all('img')
  
    # print(entry[i].find('a').get('href'))
  
