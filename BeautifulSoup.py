#!/usr/bin/python

from bs4 import BeautifulSoup

import urllib

web=urllib.urlopen('https://stackoverflow.com/')

#print (web.read())

#applying soup

souped=BeautifulSoup(web,'html5lib')

#print(souped)


#only text extraction

text_data=souped.get_text()
#print (text_data)

#tokenize process on behalf of words

token=[ i for i in text_data.split()] 
print(token)

print(len(token))
