from bs4 import BeautifulSoup
from urllib.request import urlopen

read=urlopen("http://www.maism.org")
so=BeautifulSoup(read)

links = so.findAll("a")
print(links)