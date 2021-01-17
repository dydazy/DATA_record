#获取GCA中的下载地址
import pandas as pd
from pandas import read_excel
all_GCA_file=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\no_GCF.xlsx")
all_statistic=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\statistic.xlsx")
##存在protein序列的基因组的下载地址
protein	= all_GCA_file[all_GCA_file.GCA_protein==1]
species_protein_GCA=protein["species"].tolist()
species_N50_GCA=protein["N50"].tolist()
# protein.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\2_GCA_protein.xlsx")
species_use=[]

# for i in range(len(species_protein_GCA)):
# 	if species_protein_GCA.count(species_protein_GCA[i]) == 1:
# 		species_use.append(1)
# 	if species_protein_GCA.count(species_protein_GCA[i]) > 1:
# 		if species_N50_GCA