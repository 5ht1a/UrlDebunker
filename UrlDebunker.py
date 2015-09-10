# ___________________________________________________________________________________
# ++++++++++++++++++++++++++++++-URLDEBUNKER-++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++-+-Coded by NULLBOT, the grey hat hacker.-+-++++++++++++++++++++++
# This script will prompt a user for a site to crawl, and it will ask the user if he/she wants to
# see the source code of a site of your choosing.
# For more info on webcrawling go to https://en.wikipedia.org/wiki/Web_crawler

import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

print '\033[1;33m-----------------------------------------------------------------------------------\033[1;m'
print '\033[1;41m-------------------------------+-+-+URLDEBUNKER+-+-+-------------------------------\033[1;m'
print '\033[1;31m----------------------------------MADE BY NULLBOT----------------------------------\033[1;m'
print '\033[1;33m-----------------------------------------------------------------------------------\033[1;m'
print '\033[1;36m---------------------------Search engines cannot be crawled------------------------\033[1;m'
print '\033[1;36m-------------------------------Any Url can be analyzed-----------------------------\033[1;m'

# THIS IS WHERE THE URLREADER STARTS
urlsread = []
html_text = urllib.urlopen(raw_input("Type a url for analysis: "))
urlsread.append(html_text)
print html_text.read()

print '\033[1;33m---------------------------------------------------------------------\033[1;m'
again = (raw_input("Would you like to analyze another url? Y or N?: "))
if again == 'Y':
    while len(urlsread) < 5:
        another_url = urllib.urlopen(raw_input("Type another url: "))
        urlsread.append(another_url)
        print another_url.read()
        print '\033[1;44m---------------------------------------------------------------------\033[1;m'
        print ("Urls entered: " + str(len(urlsread)))
else:
    print '\033[1;34m---------------------------------------------------------------------\033[1;m'
    print '\033[1;36m--------------------ALL URLS HAVE BEEN ANALYZED----------------------\033[1;m'
    print '\033[1;36m---------------------PROCEEDING TO WEB-CRAWLER-----------------------\033[1;m'
    print '\033[1;34m---------------------------------------------------------------------\033[1;m'

if len(urlsread) == 5:
    print '\033[1;36mALL URLS HAVE BEEN ANALYZED\033[1;m'

# THIS IS WHERE THE WEB-CRAWLER STARTS
url = raw_input("Type a url to be scraped/crawled: ")
br = mechanize.Browser()
urls = [url]
visited = [url]
while len(urls) > 0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url, link.url)
            b1 = urlparse.urlparse(newurl).hostname
            b2 = urlparse.urlparse(newurl).path
            newurl = "http://"+b1+b2
            if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
                urls.append(newurl)
                visited.append(newurl)
                print newurl
                print len(urls)
    except:
        print '\033[1;34m---------------------------------------------------------------------------\033[1;m'
        found = ("URLS FOUND: " + str(len(visited)))
        print found
        urls.pop(0)

if len(visited) == 1:
    print '\033[1;31mAn Error Occurred: Invalid url or the website is blocking connection \033[1;m'
else:
    print '\033[1;32mSUCCESS: ALL URLS HAVE BEEN FOUND \033[1;m'
    print '\033[1;32mNOTE: Some links may not have been found if \033[1;m'
