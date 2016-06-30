#!/usr/bin/env python

from lxml import html
import requests
from bs4 import BeautifulSoup


text_file = open("books.txt", "w")
r= requests.get('https://www.librarything.com/search.php?search=film&searchtype=media&searchtype=media&sortchoice=0')
bs = BeautifulSoup(r.text, "lxml")
for book in bs.findAll('td','title'):
        title = movie.find('a').contents[0]
        genres = movie.find('span','genre').findAll('a')
        genres = [g.contents[0] for g in genres]
        runtime = movie.find('span','runtime').contents[0]
        rating = movie.find('span','value').contents[0]
        year = movie.find('span','year_type').contents[0]
        imdbID = movie.find('span','rating-cancel').a['href'].split('/')[2]
        #title=str(title)
        #print(title) 
        seq= "\t".join([str(title.encode('utf8')), str(rating), str(year), str(runtime), str(map(str, genres))])
        text_file.write(seq + '\n')

text_file.close()

