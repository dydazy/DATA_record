import pandas
from pandas import read_excel
import difflib



all_plan=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\all_plant.xlsx")
all_ge=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\eukaryotes_geome.xlsx")

#取出无重复的种名
# all_species_plan=pandas.unique(all_plan["name8"].to_list())
# all_species=pandas.unique(all_ge["Name"].to_list())

#取出重复的种名
all_species_plan=all_plan["species"].to_list()
all_species=all_ge["Name"].to_list()
tax_id=all_ge["TaxID"].to_list()
Assembly_id=all_ge["Assembly Accession"].to_list()
Scaffolds_id=all_ge["Scaffolds"].to_list()
Status_id=all_ge["Status"].to_list()

# id_list=[]
# all_species=set(all_species)
# for i in range(len(all_species_plan)):
# 	if all_species_plan[i] in all_species:
# 		id_list.append(i)
# 	else:
# 		id_list.append("xxxxx")
#
# df_id=pandas.DataFrame(id_list)
# df_plan=pandas.DataFrame(all_species_plan)
# df_id.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\genome_list.xlsx")
# df_plan.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\genome_plan.xlsx")
#
# ###使用模糊匹配
# list1 = ['qqaabb', 'wweerr', '121', 'qbcd', 'plqs']
# data = difflib.get_close_matches('xx', list1, 1, cutoff=0.5)
# print(data)     # 返回值为：['plqs']

# id_list=[]
#
# for i in range(len(all_species_plan)):
# 	if all_species_plan[i] in all_species:
# 		index=all_species.index[all_species_plan[i]]
# 		id_list.append(str(Assembly_id[]))
# 		#全基因组测序的次数
# 		#num=all_species_plan.count(all_species_plan[i])
# 		#id_list.append(num)
# 	else:
# 		# data = difflib.get_close_matches(all_species_plan[i], all_species)
# 		# id_list.append(data)
# 		id_list.append("0")

tax_id_list=[]
id_list=[]
Assembly_list=[]
Scaffolds_list=[]
num_count_list=[]
num_list=[]
Status_list=[]
ncbi_list=[]
xx=""
vv=""
ww=""
ee=""
uu=""
y=0
for i in range(len(all_species_plan)):
	if all_species_plan[i] in all_species:
		for j in range(len(all_species)):
			if all_species_plan[i] == all_species[j]:
				xx=str(Assembly_id[j])+","+xx
				vv=str(tax_id[j])+","+vv
				ww=str(Scaffolds_id[j])+","+ww
				uu=str(Status_id[j])+","+uu
				y=y+1
		Assembly_list.append(xx)
		id_list.append(vv)
		Scaffolds_list.append(ww)
		num_count_list.append(y)
		Status_list.append(uu)
		ncbi_list.append(1)
		xx = ""
		vv = ""
		ww = ""
		ee = ""
		uu = ""
		y = 0
	else:
		Assembly_list.append(0)
		id_list.append(0)
		Scaffolds_list.append(0)
		num_count_list.append(0)
		Status_list.append(0)
		ncbi_list.append(0)

Assembly_id=pandas.DataFrame(Assembly_list)
id_id=pandas.DataFrame(id_list)
Scaffolds_id=pandas.DataFrame(Scaffolds_list)
num_count_id=pandas.DataFrame(num_count_list)
Status_id=pandas.DataFrame(Status_list)
ncbi_id=pandas.DataFrame(ncbi_list)
Assembly_id.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\Assembly_list.xlsx")
id_id.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\id_list.xlsx")
Scaffolds_id.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\Scaffolds_list.xlsx")
num_count_id.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\num_list.xlsx")
Status_id.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\Status_list.xlsx")
ncbi_id.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\ncbi_list.xlsx")



