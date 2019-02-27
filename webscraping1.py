from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import pandas as pd
read=urlopen("http://www.maism.org")
so=BeautifulSoup(read)

links = so.findAll("a")
q=np.array(links)
df=pd.DataFrame(q)
writer=pd.ExcelWriter('pandas2.xlsx',engine="xlsxwriter")
df.to_excel(writer , sheet_name='sheet1')
writer.save()

file=open("pandas2.xlsx",'rb')
dataF=pd.read_excel(file)
print(dataF)
