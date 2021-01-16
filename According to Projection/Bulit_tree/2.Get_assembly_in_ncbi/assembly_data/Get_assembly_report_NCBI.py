#制作列表
import pandas as pd
from pandas import read_excel
# species_assembly_id_ftp_382=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\species_assembly_id_ftp_382.xlsx")
# melted=species_assembly_id_ftp_382.melt("species")
# # melted=pd.unique(melted)
# melted.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\species_assembly_id_ftp_382_melt.xlsx")

#get ftp list
# species_assembly_id_ftp_382=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\species_assembly_id_ftp_382_melt.xlsx")
# all_ge=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_summary_genbank.xlsx")
# assembly_id_list=species_assembly_id_ftp_382["assembly_id"].to_list()
# ftp_path=all_ge["ftp_path"].to_list()
# assembly_accession=all_ge["assembly_accession"].to_list()
#
# ftp_list=[]
# for i in range(len(assembly_id_list)):
# 	if assembly_id_list[i] in assembly_accession:
# 		for j in range(len(assembly_accession)):
# 			if assembly_id_list[i]==assembly_accession[j]:
# 				ftp_list.append(ftp_path[j])
# 	else:
# 		ftp_list.append("XXXXX")
#
# ftp_list=pd.DataFrame(ftp_list)
# ftp_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\ftp_list.xlsx")

#get assembly stastc
import requests


# def getassembly_data(ftp_path):
# 	try:
# 		url=str(ftp_path)
# 		re=requests.get(url)
# 		with open(path, "wb") as f:
# 			f.write(re.content)
# 	except:
# 		return "xxxxxx"


# ftp_path=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\species_assembly_id_ftp_382_melt.xlsx")
# ftp_path_stastc=ftp_path["ftp_path_stastc"].to_list()
# file_name=ftp_path["file_name"].to_list()
#
# #批量下载txt
# import requests
# str=r"D:\\Study\\Z_Work\\LX\\Data\\Get_assembly\\assembly_data\\"
# for i in range(len(ftp_path_stastc)):
# 	url = ftp_path_stastc[i]
# 	re=requests.get(url, stream=True)
# 	path=str+file_name[i]
# 	with open(path, "wb") as f:
# 		f.write(re.content)
