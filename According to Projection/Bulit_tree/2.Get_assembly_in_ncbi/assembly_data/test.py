import pandas as pd
from pandas import read_excel
ftp_path=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\species_assembly_id_ftp_382_melt.xlsx")
file_name=ftp_path["file_name"].to_list()
ee="D:\Study\\Z_Work\\LX\\Data\Get_assembly\\assembly_data\\"
url = ee + file_name[3]
f = open(url, "r")  # 设置文件对象
str = f.read()  # 将txt文件的所有内容读入到字符串str中
f.close()
import re
pattern16 = re.compile(r'(?<=all	all	all	all	ungapped-length	)\d+\.?\d*')
Organism_name = pattern16.findall(str)
print(Organism_name)
# print(str)