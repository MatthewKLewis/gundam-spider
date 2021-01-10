#import
import urllib
import re
import json
from bs4 import BeautifulSoup
import time

class Gundam:
    def __init__(self):
        pass


separator = ','

#open the urls file as a string
with open('urls.txt', 'r') as file:
    urlData = file.read().split(separator)

arrayOfObjects = []

f = open('gundamData.txt', 'w')
f.write('[')

i = 0
finalIndex = 1
while i < len(urlData):
    print(urlData[i])
    tempPage = urllib.request.urlopen(urlData[i])
    tempSoup = BeautifulSoup(tempPage, features='lxml')
    tagImage = tempSoup.find("img", class_="pi-image-thumbnail")
    tagLabels = tempSoup.find_all("h3", class_="pi-data-label")
    tagValues = tempSoup.find_all("div", class_="pi-data-value")
    lengthOfLabels = (len(tagLabels))
    lengthOfValues = (len(tagValues))
    if lengthOfLabels == lengthOfValues and lengthOfLabels != 0:
        try:
            tempGundam = Gundam()
            setattr(tempGundam, "Final Array Index", finalIndex)
            setattr(tempGundam, "Image", tagImage.attrs['src'])
            finalIndex += 1        

            j = 0
            while j < lengthOfLabels:

                setattr(tempGundam, tagLabels[j].text, tagValues[j].text)
                j += 1

            f.write(json.dumps(tempGundam.__dict__, indent=4))
            f.write(',')

            # arrayOfObjects.append(json.dumps(tempGundam.__dict__, indent=4))
        except:
            print("Couldn't add Gundam to JSON File")

    i += 1

f.write(']')
f.close()
print('--end--')