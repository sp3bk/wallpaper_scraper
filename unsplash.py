# for everyday automation:
# crontab -e
# 1 2 3 4 5 /path/to/script
# 1: Minutes(0-59)
# 2: Hours(0-23)
# 3: Days(1-31)
# 4: Month(1-12)
# 5: Day of the week(1-7)
# /path/to/script - your own shell script
# :q!

from bs4 import BeautifulSoup
import requests
import urllib
import os

try:
    list1 = []
    list2 = []
    # source 1
    source = requests.get("https://unsplash.com/@ripato").text
    soup = BeautifulSoup(source, 'lxml')
    for article in soup.find_all('img'):
        if 'profile' not in article['src'] and 'secure.insightexpressai.com' not in article['src']:
            list1.append(article['src'])

    # source 2
    source = requests.get(
        "https://unsplash.com/collections/1922729/beautiful-shots-from-above").text
    soup = BeautifulSoup(source, 'lxml')
    for article in soup.find_all('img'):
        if 'profile' not in article['src'] and 'secure.insightexpressai.com' not in article['src']:
            list2.append(article['src'])

    # saving them to a folder
    path = os.path.dirname(os.path.realpath("unsplash.py"))

    os.chdir(path+"/ricardo")
    count = 1
    for link in list1:
        urllib.urlretrieve(
            link, "ricardo"+"_"+str(count)+".jpg")
        count = count + 1

    os.chdir(path+"/above")
    count = 1
    for link in list2:
        urllib.urlretrieve(
            link, "above"+"_"+str(count)+".jpg")
        count = count + 1

except (requests.ConnectionError):
    print ("ERROR. Invalid URL for unspash!")
