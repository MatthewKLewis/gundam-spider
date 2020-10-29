# imports
import urllib
import re
import json
from bs4 import BeautifulSoup

#initial Beautiful Soup data
url = 'https://gundam.fandom.com/wiki/List_of_Mobile_Weapons'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, features="lxml")
soupList = soup.findAll('a', attrs={'href': re.compile("^/wiki/")})

#Arrays with progressively more human-readable data
urlList = []
urlList2 = []
infoIWant = []
infoIWant2 = []

#Take elements from soupList and append them to urlList if they will form a proper url
i = 0
while i < len(soupList):
    soupList[i] = str(soupList[i])[9:] + '   '
    if soupList[i][0] == '/':
        urlList.append('https://gundam.fandom.com' + soupList[i])
    i += 1

#Take elements from urlList and append them to urlList2 after removing extraneous letters
for item in urlList:
    item = item.partition('"')
    urlList2.append(item[0])

#Sample page to test data extraction
newPage = urllib.request.urlopen(urlList2[200])
newSoup = BeautifulSoup(newPage, features='lxml')

#extract all divs with the class pi-data-value
print(urlList2[200])
infoIwant = newSoup.find_all("div", class_="pi-data-value")

#Take elements from infoIWant and strip the HTML, add to infoIWant2
for item in infoIwant:
    infoIWant2.append(item.get_text())

#Write the readable data into a text file
f = open('data.txt', 'w')
for item in infoIWant2:
    f.write(item)

f.close()
print('write complete')
