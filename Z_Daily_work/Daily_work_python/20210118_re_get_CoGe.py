import re
import pandas as pd
from pandas import read_excel

pattern = re.compile(r'(?<=gid=)\d+\.?\d*')
path="D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/All_species/"

species_doi=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\6.Literature mining\species_paper_url.xlsx")
species=species_doi["species"].to_list()

#读取文件
def getPRJAN(url):

	with open(url, "r", encoding="utf-8") as f: # 设置文件对象
		str = f.read()  # 将txt文件的所有内容读入到字符串str中
		f.close()
	x=pattern.findall(str)
	return x


for i in range(len(species)):
	url = path + str(i) + "_" + species[i] + ".txt"
	ee=getPRJAN(url)
	ee=pd.unique(ee)
	print(i,"xx",ee)