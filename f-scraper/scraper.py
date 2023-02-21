import requests
from bs4 import BeautifulSoup
import json

# Sample URL for testing
url_to = 'https://myfigurecollection.net/browse.v4.php?mode=search&rootId=0&status=-1&categoryId=-1&orEntries[]=1590&domainId=-1&noReleaseDate=0&releaseTypeId=0&ratingId=0&isCastoff=0&hasBootleg=0&tagId=0&noBarcode=0&clubId=0&isDraft=0&year=2023&month=2&acc=0&separator=0&sort=insert&output=2&current=categoryId&order=desc&page='

"""
TO DO

Format the data.
"""

figure_entries = []

# Maybe add an extra method to get the official images from the figure entry as well sometime.

for pages in range(1, 20):
  resp = requests.get(url_to + str(pages))
  soup = BeautifulSoup(resp.content, 'html.parser')
  entry = soup.find_all('span', class_='item-icon')

  for i in range(len(entry)):
    f_name = entry[i].find('img').get('alt')
    f_link = 'https://myfigurecollection.net/item/' + str(entry[i].find('a').get('href'))
    
    fr = requests.get(f_link)
    fs = BeautifulSoup(fr.content, 'html.parser')
    #f_img = fs.find_all('a', class_='main')

    #print(fs)

    print(f_name)

    figure_entries.append({"name": f_name, "link": f_link})
  
    # print(entry[i].find('a').get('href'))
  
#print(figure_entries)
