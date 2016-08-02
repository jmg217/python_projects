#!/usr/bin/env python

from lxml import html
import requests
from bs4 import BeautifulSoup
#import pickle

#text_file = open("books.txt", "w")
#r= requests.get('https://www.goodreads.com/list/show/252.Books_Made_into_Movies?page=')
#r= requests.get('http://www.imdb.com/search/keyword?keywords=based-on-novel&sort=moviemeter,asc&mode=detail&page=1&ref_=kw_ref_key')
#print('here')
for i in range(1):	
	url="https://www.goodreads.com/list/show/252.Books_Made_into_Movies?page={}".format(i)
	r= requests.get(url)
	bs = BeautifulSoup(r.texti, , "lxml")
	print('here')
	for book in bs.findAll('tr','http://schema.org/Book'):
	#	title = book.find('a').contents[0]
		title = book.find('span', 'name').contents[0]
 #   	genres = movie.find('span','genre').findAll('a')
  #  	genres = [g.contents[0] for g in genres]
   # 	runtime = movie.find('span','runtime').contents[0]
    #	rating = movie.find('span','value').contents[0]
    #	year = movie.find('span','year_type').contents[0]
    #	imdbID = movie.find('span','rating-cancel').a['href'].split('/')[2]
	#title=str(title)
		print(title) 
		print('here')
#	seq= "\t".join([str(title.encode('utf8')), str(rating), str(year), str(runtime), str(map(str, genres))])  	
#	text_file.write(seq + '\n')
	#	text_file.write(str(title.encode('utf8'))+'\n')
#text_file.close()

