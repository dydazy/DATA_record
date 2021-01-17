import pandas as pd
from pandas import read_excel
# #找到ncbi中没有注释的物种的doi号
# no_annotation_NCBI=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\4.other_data_base\species_in_NCBI_no_annotation.xlsx")
# all_species=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\4.other_data_base\all_species_doi.xlsx")
# all_species_list=all_species["species"].tolist()
# no_annotation_list=no_annotation_NCBI["species"].tolist()
# id_list=[]
# for i in range(len(all_species_list)):
# 	if all_species_list[i] in no_annotation_list:
# 		id_list.append(0)
# 	else:
# 		id_list.append(1)
# id_list=pd.DataFrame(id_list)
# id_list.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\4.other_data_base\id_list.xlsx")

import requests
species_doi=read_excel(r"D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/In_NCBI_no_annotation.xlsx")
species=species_doi["species"].tolist()
url=species_doi["doi"].tolist()
def gethtml(url):
	try:
		r=requests.get(url,timeout=60)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.content
	except:
		return bytes("异常",encoding="UTF-8")

for i in range(len(species)):
	# html = requests.get(url[i])
	x=gethtml(url[i])
	str1 = "D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/no_annotation_in_NCBI/"
	path = str1 + str(i)+"_" + species[i] + ".txt"
	with open(path, "wb") as f:
		f.write(x)
		