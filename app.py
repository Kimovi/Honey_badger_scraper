#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    soup = BeautifulSoup(response, 'html.parser')
f = open("Readme.md", 'w')
for anchor in soup.find_all('a'):
    data = anchor.get('href', '/') + "\n"
    f.write(data)
f.close()
