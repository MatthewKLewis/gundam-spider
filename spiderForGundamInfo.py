#import
import urllib
import re
import json
from bs4 import BeautifulSoup
import time

#
separator = ','

#open the urls file as a string
with open('urls.txt', 'r') as file:
    urlData = file.read().split(separator)

class Gundam:
    def __init__(self):
        pass


f = open('data.txt', 'a')

arrayOfObjects = []

i = 0
while i < 400:
    i += 1
    print(urlData[i])
    tempPage = urllib.request.urlopen(urlData[i])
    tempSoup = BeautifulSoup(tempPage, features='lxml')
    tagLabels = tempSoup.find_all("h3", class_="pi-data-label")
    tagValues = tempSoup.find_all("div", class_="pi-data-value")
    
    lengthOfValues = (len(tagValues))
    lengthOfLabels = (len(tagLabels))
    if lengthOfLabels == lengthOfValues:
        tempGundam = Gundam() 
        if lengthOfLabels == lengthOfValues:
            j = 0
            while j < lengthOfLabels:
                setattr(tempGundam, tagLabels[j].text, tagValues[j].text)
                j += 1
            arrayOfObjects.append(json.dumps(tempGundam.__dict__, indent=4))


f = open('data.txt', 'w')
f.write('[')

for item in arrayOfObjects:
    f.write(item)

f.write(']')
f.close()
print('end')


# #Sample page to test data extraction

# f = open('data.txt', 'w')
# j = 200
# while j < 205:

#     print(urlList2[j])

#     newPage = urllib.request.urlopen(urlList2[j])

#     newSoup = BeautifulSoup(newPage, features='lxml')

#     infoIwant = newSoup.find_all("div", class_="pi-data-value", recursive=True)
    
#     for item in infoIWant:
#         f.write(str(item) + '\r\n\r\n\r\n')

#     print(j)
#     j += 1
#     time.sleep(5)


# f.close()
# print('write complete')