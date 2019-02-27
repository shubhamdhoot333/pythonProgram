from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
read=urlopen("http://www.maism.org")
so=BeautifulSoup(read)

links = so.findAll("a")
q=np.array(links)
print(q)