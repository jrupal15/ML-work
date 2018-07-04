#!/usr/bin/python

from bs4 import BeautifulSoup

import urllib

web=urllib.urlopen('https://stackoverflow.com/')

print (web.read())

