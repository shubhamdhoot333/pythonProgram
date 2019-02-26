from bs4 import BeautifulSoup
from urllib.request import urlopen
read=urlopen("http://www.maism.org")
soup=BeautifulSoup(read)

links = soup.find_all("img")
print(links)