import requests
from bs4 import BeautifulSoup

# Sample URL for testing
response = requests.get('https://myfigurecollection.net/browse.v4.php?mode=search&rootId=0&status=-1&categoryId=-1&orEntries[]=1590&domainId=-1&noReleaseDate=0&releaseTypeId=0&ratingId=0&isCastoff=0&hasBootleg=0&tagId=0&noBarcode=0&clubId=0&isDraft=0&year=2023&month=2&acc=0&separator=0&sort=insert&output=2&current=categoryId&order=desc&page=1')
soup = BeautifulSoup(response.content, 'html.parser')

d = soup.find_all('span', class_='item-icon')

"""
TO DO

Update page iterator to automatically take the URL from the Last nav link.
Split the string and take the last digits of the link use for the second parameter.

Format the data.
"""
for pages in range(1, 20):
  pass

print(d)
