#!/usr/bin/env python

from lxml import html
import requests
from bs4 import BeautifulSoup
import pickle

text_file = open("Output.txt", "w")
#r= requests.get('http://www.imdb.com/search/keyword?keywords=based-on-novel&sort=moviemeter,asc&mode=detail&page=1&ref_=kw_ref_key')
for i in range(200):	
	url="http://www.imdb.com/search/keyword?keywords=based-on-novel&mode=detail&page={}&ref_=kw_nxt&sort=moviemeter,asc".format(i)
	r= requests.get(url)
	bs = BeautifulSoup(r.text, "lxml")
	for movie in bs.findAll('div','lister-item-content'):
		title = movie.find('a').contents[0]
 #   	genres = movie.find('span','genre').findAll('a')
  #  	genres = [g.contents[0] for g in genres]
   # 	runtime = movie.find('span','runtime').contents[0]
    		rating = movie.find('strong').contents[0]
    #	year = movie.find('span','year_type').contents[0]
    #	imdbID = movie.find('span','rating-cancel').a['href'].split('/')[2]
	#title=str(title)
	#print(title) 
#	seq= "\t".join([str(title.encode('utf8')), str(rating), str(year), str(runtime), str(map(str, genres))])  	
	seq= "\t".join([str(title.encode('utf8')), str(rating)])
	text_file.write(seq + '\n')
	#	text_file.write(str(title.encode('utf8'))+'\n')
text_file.close()

