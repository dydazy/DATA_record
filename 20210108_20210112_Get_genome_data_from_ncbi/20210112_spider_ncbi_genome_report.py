import requests
import pandas
from pandas import read_excel
import re

#抓取网页
list=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\Angiospermae.xlsx")
species_list=list['name8'].to_list()

def getspecies(species_name):
	try:
		url="https://www.ncbi.nlm.nih.gov/genome/?term="
		data=species_name
		r=requests.get(url+data)
		r.encoding=r.apparent_encoding
		r.raise_for_status()
		return r.text
	except:
		return "xxxxxx"

# def append_to_excel(filepath,dataframe)->None:
#     writer=pandas.ExcelWriter(filepath,mode='w')#这里的mode需要用w模式，a模式会产生新的sheet
#     data=pandas.read_excel(writer,index_col=None,header=None)
#     data.to_excel(writer,startrow=0,index=None,header=None,sheet_name='sheet1')
#     dataframe.to_excel(writer,startrow=data.shape[0],index=None,header=None,sheet_name='sheet1')
#     writer.save()


id_list=[]
for i in range(len(species_list)):
	flage=getspecies(species_list[i])
	# if flage=="xxxxxx":
	# 	id_list[i]="xxxxxx"
	id=re.findall(r'(?<=ASSEMBLY_NAME=GCA_)\d+\.?\d*',flage)
	id="GCA_"+str(id)
	id_list.append(id)
	print(id)

df=pandas.DataFrame(id_list)
df.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_id.xlsx")
# html=getspecies(species_list[10])
# print(html)
# print(re.findall(r'(?<=ASSEMBLY_NAME=GCA_)\d+\.?\d*',html))




#get GCA id


###希望直接爬取最新的基因组数据，失败，
#原因：
#不同物种搜索后的页面不同，爬取失败
#考虑先找到不同物种的的页面在进行测试