import requests
import os
import time
import numpy as np
from bs4 import BeautifulSoup


# _6tbg2q

# https://www.airbnb.com/s/Seattle--WA--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=november&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Seattle%2C%20WA%2C%20United%20States&place_id=ChIJVTPokywQkFQRmtVEaUZlJRA&source=structured_search_input_header&search_type=autocomplete_click


url = ""


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

linkpool = []
imglinkpool = []
# print(soup.title.text)
urlhead = r""
urltail = ""
# imgs = soup.find('div', attrs={'id': 'aRtcNt'})
# imglink = imgs.findAll('img')[0].attrs['src']
# targetlink = imgs.findAll("a")[-2].attrs['href']
index = 0
while url not in linkpool:
    r = requests.get(url)
    linkpool.append(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    imgs = soup.find('div', attrs={'id': 'aRTcNt'})
    imglink = imgs.findAll('img')[0].attrs['src']
    # imagefulllink = url+imglink
    # print(imagefulllink)
    with open(str(index)+'.jpg', 'wb') as f:
        im = requests.get(imglink)
        f.write(im.content)

    # Download
    imglinkpool.append(imglink)
    #
    urltail = imgs.findAll("a")[-1].attrs['href']
    url = urlhead+urltail
    index += 1
    print(url)
    print("SLEEP START")
    time.sleep(1)
    print("SLEEP END")
    # update urltail
print(linkpool)
print(imglinkpool)

# imglinkpool
# print(imglink)
# print(urlhead+targetlink)
# for link in imgs.findAll("a"):
#     print(link)


# print(imgs) aRtcNt

# index = 0
# for index, item in enumerate(imgs):
#     print(item)

#     link = item['src']
#     print(link)
#     with open(str(index)+'.jpg', 'wb') as f:
#         im = requests.get(link)
#         f.write(im.content)
