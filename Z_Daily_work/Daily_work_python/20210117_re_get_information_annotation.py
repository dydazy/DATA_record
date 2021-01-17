#正则抓取文章中的内容
import re
import pandas as pd
from pandas import read_excel

pattern = re.compile(r'(?<=all	all	all	all	component-count	)\d+\.?\d*')
path="D:/Study/Z_Work/LX/Data/Bulit_tree/4.other_data_base/species_doi/no_annotation_in_NCBI/"

species_doi=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\4.other_data_base\In_NCBI_no_annotation.xlsx")
species=species_doi["species"].to_list()

#读取文件
def getPRJAN(url):

	with open(url, "r", encoding="utf-8") as f: # 设置文件对象
		str = f.read()  # 将txt文件的所有内容读入到字符串str中
		f.close()
	pattern1 = re.compile(r'(?<=PRJNA)\d+\.?\d*')
	x=pattern1.findall(str)
	return x

# dict={}
for i in range(len(species)):
	url = path + str(i) + "_" + species[i] + ".txt"
	ee=getPRJAN(url)
	ee=pd.unique(ee)
	print("xx",ee)
	# url=""
	# aa = {i: getPRJAN(i)}
	# dict.update(aa)
	# aa={}

# df = pd.DataFrame.from_dict(dict)
# df.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\4.other_data_base\Not_in_ncbi_dict.xlsx")

# url = path + str(1) + "_" + species[1] + ".txt"
# with open(url, "r", encoding="utf-8") as f: # 设置文件对象
# 	str = f.read()  # 将txt文件的所有内容读入到字符串str中
# 	f.close()
# # print(str)
# pattern1 = re.compile(r'(?<=PRJNA)\d+\.?\d*')
# # pattern2 = re.compile(r'(?<=BioProject ).*')
# x=pattern1.findall(str)
# print(x)
