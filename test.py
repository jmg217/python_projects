import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.librarything.com/search.php?search=film&searchtype=media&searchtype=media&sortchoice=0', preload_content=False)
#for chunk in r.stream(32):
 #    print(chunk)
