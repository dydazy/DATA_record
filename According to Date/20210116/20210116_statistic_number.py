#整理数据
import pandas as pd
from pandas	import read_excel
all_statistic=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\statistic.xlsx")
binary=all_statistic["binary"].tolist()
species=all_statistic["species"].tolist()
GCA=all_statistic["GCA"].tolist()
#获取可以利用的数据
#至少存在一种注释的物种及其GCA编号
useful_data_binary_1=all_statistic[all_statistic.binary==1]
# useful_data_binary_1.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\useful_data_binary_1.xlsx")

#优先寻找GCF的下载链接
#寻找到78个总共79个重复
useful_data_binary_GCF=useful_data_binary_1[(useful_data_binary_1.GCF_gff==1) | (useful_data_binary_1.GCF_gtf==1) | (useful_data_binary_1.GCF_cds==1) | (useful_data_binary_1.GCF_protein==1) | (useful_data_binary_1.GCF_translate_cds==1)]
# print(useful_data_binary_GCF)
# useful_data_binary_GCF.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\useful_data_binary_GCF.xlsx")

#寻找GCA中的下载链接

species_GCF=useful_data_binary_GCF["species"]
species_GCF=pd.unique(species_GCF)
# x=0
# for i in range(len(species)):
# 	if not(species[i] in species_GCF): #排除有GCF的物种
# 		x=x+1

# useful_data=pd.DataFrame(index=range(695),columns=['species', 'GCA', 'N50', 'GCA_gff', 'GCA_gtf', 'GCA_cds', 'GCA_protein',
#        'GCA_translate_cds', 'GCF_gff', 'GCF_gtf', 'GCF_cds', 'GCF_protein',
#        'GCF_translate_cds', 'total', 'binary', 'ftp_path_GCA', 'ftp_path_GCF'])
#排除有GCF的物种
# x=0
# list=[]
# for i in range(len(species)):
# 	if not(species[i] in species_GCF):
# 		list.append(1)
# 	else:
# 		list.append(0)
# list=pd.DataFrame(list)
# list.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\list_GCA.xlsx")
useful_data_binary_2=all_statistic[all_statistic.nothave_GCF==1]
# useful_data_binary_2.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\no_GCF.xlsx")








# useful_data["binary"]=binary
# useful_data["species"]=species
# useful_data["GCA"]=GCA
# ufd=useful_data.drop_duplicates()
# ufd_species=ufd["species"].tolist()
# useful_binary=ufd["binary"].tolist()
# useful_data_1=pd.DataFrame(columns=["GCA","binary","species"])
# for i in range(len(ufd_species)):
# 	if useful_binary[i] == 1:
# print(all_statistic.columns)
# for i in range(len(species)):
# 	if binary[i]==1:
# 		useful_data



# print(ufd)
# ufd.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\usefuldata.xlsx")
