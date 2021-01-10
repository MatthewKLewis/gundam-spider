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

f = open('urls.txt', 'w')

#Take elements from urlList and append them to urlList2 after removing extraneous letters
for item in urlList:
    item = item.partition('"')
    urlList2.append(item[0])
    f.write(item[0])
    f.write(',')

f.close()
print('write complete')