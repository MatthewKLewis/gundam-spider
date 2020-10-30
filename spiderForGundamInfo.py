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


arrayOfObjects = []

i = 1200
while i < (len(urlData)-10):
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
        if lengthOfLabels == lengthOfValues and lengthOfLabels != 0:
            j = 0
            while j < lengthOfLabels:
                setattr(tempGundam, tagLabels[j].text, tagValues[j].text)
                j += 1
            arrayOfObjects.append(json.dumps(tempGundam.__dict__, indent=4))


f = open('twelveToEnd.txt', 'w')
f.write('[')

for item in arrayOfObjects:
    f.write(item)
    f.write(',')

f.write(']')
f.close()
print('end')