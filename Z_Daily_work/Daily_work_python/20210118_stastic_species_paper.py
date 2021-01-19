import pandas
from pandas import read_excel
already_url=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\6.Literature mining\already_url.xlsx")
species_paper_url=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\6.Literature mining\species_paper_url.xlsx")
already_species=already_url["species"].tolist()
species_paper_species=species_paper_url["species"].tolist()

list=[]

for i in range(len(species_paper_species)):
	if species_paper_species[i] in already_species:
		list.append(1)
	else:
		list.append(0)

list=pandas.DataFrame(list)
list.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\6.Literature mining\list.xlsx")