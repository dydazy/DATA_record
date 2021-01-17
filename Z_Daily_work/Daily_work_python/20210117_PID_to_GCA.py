import pandas as pd
from pandas import read_excel
species_PRJNA=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\5.PRJNA_to_GCA\species_PRJNA.xlsx",sheet_name="Sheet1")
data_base=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\Z_data_base\assembly_summary_genbank_project.xlsx")
id_list=[]
PRJNA_list=species_PRJNA["PRJNA"].tolist()
data_base_PRJNA=data_base["bioproject"].tolist()
for i in range(len(data_base_PRJNA)):
	if data_base_PRJNA[i] in PRJNA_list:
		id_list.append(1)
	else:
		id_list.append(0)
id_list=pd.DataFrame(id_list)
id_list.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\Z_data_base\id_list_big.xlsx")
