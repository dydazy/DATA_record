#get latest id
import pandas
from pandas import read_excel

all_ge=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\eukaryotes_geome.xlsx")
data=all_ge["seq_rel_data"].to_list()
species=all_ge["organism_name"].to_list()
species_row={}
for i in (range(len(data))):
	if species[i] in species_row:
		if species_row[species[i]]<data[i]:
			species_row[species[i]]=data[i]
		else:
			pass
	else:
		species_row[species[i]]=data[i]
