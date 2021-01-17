import pandas as pd
from  pandas import read_excel
annotation_list=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\anoation_list.xlsx")
annotation_list=annotation_list["ana"].tolist()
all_statistic=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\statistic.xlsx")
species=all_statistic["species"].tolist()
list=[]
for i in range(len(species)):
	if species[i] in annotation_list:
		list.append(1)
	else:
		list.append(0)

list=pd.DataFrame(list)
list.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\GCA_information\binary_anation.xlsx")