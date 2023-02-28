import requests
from bs4 import BeautifulSoup
import json

# Change URL to desired Search URL. Remove the page number at the end.
url_to = 'https://myfigurecollection.net/browse.v4.php?mode=search&rootId=0&status=-1&categoryId=-1&orEntries[]=1590&domainId=-1&noReleaseDate=0&releaseTypeId=0&ratingId=0&isCastoff=0&hasBootleg=0&tagId=0&noBarcode=0&clubId=0&isDraft=0&year=2023&month=2&acc=0&separator=0&sort=insert&output=2&current=categoryId&order=desc&page='

figure_entries = []


"""
Change the second parameter to the maximum or minimum pages you wish to go over.

In case of a single page, you can delete the for loop and all cases of [i].
"""
for pages in range(1, 20):
  resp = requests.get(url_to + str(pages))
  soup = BeautifulSoup(resp.content, 'html.parser')
  entry = soup.find_all('span', class_='item-icon')

  for i in range(len(entry)):
    f_name = entry[i].find('img').get('alt')
    f_link = 'https://myfigurecollection.net' + str(entry[i].find('a').get('href'))
    
    fr = requests.get(f_link)
    fs = BeautifulSoup(fr.content, 'html.parser')
    f_img = fs.find(class_='main').find_all(recursive=False)[0].get('src')

    figure_entries.append({"name": f_name, "link": f_link, "image": f_img})
  
print(figure_entries)

with open("selection.json", "w") as outfile:
  json.dump((figure_entries), outfile)
