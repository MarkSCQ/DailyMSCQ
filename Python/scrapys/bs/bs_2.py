import requests
import os
import time
import numpy as np
from bs4 import BeautifulSoup
import re
import urllib

# https://www.airbnb.com/s/Seattle--WA--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=november&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Seattle%2C%20WA%2C%20United%20States&place_id=ChIJVTPokywQkFQRmtVEaUZlJRA&source=structured_search_input_header&search_type=autocomplete_click

def purning(text):

    pass

url = r"http://www.hair43.com/y/k/k4/201012/298494.html"


r = requests.get(url)
r.encoding = "gb2312"
soup = BeautifulSoup(r.text, 'html.parser')

linkpool = []
imglinkpool = []

urlhead = r""
urltail = ""

index = 0

titles = soup.find_all('option',selected=True)

for i in titles:
    print((i.text).split("：")[1])
    # print(titles)
# content = soup.find('div',attrs={"id":"artcNt"}).find_all('p')[0]
# print(content)
# content = soup.find('div',attrs={"id":"artcNt"}).find_all('p')[1]
# print(content)
content = soup.find('div',attrs={"id":"artcNt"}).find_all('p')[2]
print(content)
test = re.sub('<.*?>',"",str(content))
print(content)
print(test)
# print(content)

# print(content)
# for i in content:
#     print(i)
# with open("test.txt",'w') as f:
#     f.write(str(content))
