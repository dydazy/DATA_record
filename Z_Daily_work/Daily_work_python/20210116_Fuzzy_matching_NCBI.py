#在NCBI中再次爬取种名
#尝试
import requests
import re
import pandas
from pandas import read_excel

# species=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\4.other_data_base\species.xlsx")
# species=species["species"].tolist()
# species=species["species"].tolist()
# url=r"https://www.ncbi.nlm.nih.gov/genome/?term="
#
#
#
species=read_excel(r"D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi.xlsx")

url=species["doi"].tolist()
species=species["species"].tolist()
# html=requests.get(url[1])
# x=html.content
# str="D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/"
# path=str + species[1] + ".txt"
# with open(path, "wb") as f:
# 	f.write(x)

for i in range(67,len(species)):
	html = requests.get(url[i])
	x = html.content
	str1 = "D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/"
	path = str1 + str(i)+"_" + species[i] + ".txt"
	with open(path, "wb") as f:
		f.write(x)


# from scihub import SciHub
# sh = SciHub()
# result = sh.fetch(identifier=url[1])
# print(result)
# result = sh.download(identifier=url[1], destination='D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/',path=species[1]+".pdf")
