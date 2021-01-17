import requests
import re
import pandas
from pandas import read_excel


species=read_excel(r"D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi.xlsx")

url=species["doi"].tolist()
species=species["species"].tolist()
# html=requests.get(url[1])
# x=html.content
# str="D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/"
# path=str + species[1] + ".txt"
# with open(path, "wb") as f:
# 	f.write(x)

#59
#66

def gethtml(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.content
	except:
		return bytes("异常",encoding="UTF-8")

for i in range(66,67):
	# html = requests.get(url[i])
	x=gethtml(url[i])
	str1 = "D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/"
	path = str1 + str(i)+"_" + species[i] + ".txt"
	with open(path, "wb") as f:
		f.write(x)


