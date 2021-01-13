import pandas as pd
from pandas import read_excel
ftp_path=read_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\species_assembly_id_ftp_382_melt.xlsx")
file_name=ftp_path["file_name"].to_list()


#读取str
#读取文件名

#正则抓取数据
import re
pattern = re.compile(r'(?<=all	all	all	all	component-count	)\d+\.?\d*')
pattern1 = re.compile(r'(?<=all	all	all	all	contig-L50	)\d+\.?\d*')
pattern2 = re.compile(r'(?<=all	all	all	all	contig-N50	)\d+\.?\d*')
pattern3 = re.compile(r'(?<=all	all	all	all	contig-count	)\d+\.?\d*')
pattern4 = re.compile(r'(?<=all	all	all	all	molecule-count	)\d+\.?\d*')
pattern5 = re.compile(r'(?<=all	all	all	all	region-count	)\d+\.?\d*')
pattern6 = re.compile(r'(?<=all	all	all	all	scaffold-L50	)\d+\.?\d*')
pattern7 = re.compile(r'(?<=all	all	all	all	scaffold-N50	)\d+\.?\d*')
pattern8 = re.compile(r'(?<=all	all	all	all	scaffold-N75	)\d+\.?\d*')
pattern9= re.compile(r'(?<=all	all	all	all	scaffold-N90	)\d+\.?\d*')
pattern10 = re.compile(r'(?<=all	all	all	all	scaffold-count	)\d+\.?\d*')
pattern11 = re.compile(r'(?<=all	all	all	all	top-level-count	)\d+\.?\d*')
pattern12 = re.compile(r'(?<=all	all	all	all	total-gap-length	)\d+\.?\d*')
pattern13 = re.compile(r'(?<=all	all	all	all	total-length	)\d+\.?\d*')
pattern14 = re.compile(r'(?<=all	all	all	all	ungapped-length	)\d+\.?\d*')
pattern15 = re.compile(r'(?<=all	all	all	all	unspanned-gaps	)\d+\.?\d*')
pattern16 = re.compile(r'(?<=# Organism name:).*')
pattern17 = re.compile(r'(?<=# Infraspecific name:).*')
pattern18 = re.compile(r'(?<=# Taxid:).*')
pattern19 = re.compile(r'(?<=# BioSample:).*')
pattern20 = re.compile(r'(?<=# BioProject:).*')
pattern21 = re.compile(r'(?<=# Submitter:).*')
pattern22 = re.compile(r'(?<=# Date:).*')
pattern23 = re.compile(r'(?<=# Release type:).*')
pattern24 = re.compile(r'(?<=# Assembly level:).*')
pattern25 = re.compile(r'(?<=# Genome representation).*')
pattern26 = re.compile(r'(?<=# WGS project:).*')
pattern27 = re.compile(r'(?<=# Genome coverage:).*')
pattern28 = re.compile(r'(?<=# GenBank assembly accession:).*')
pattern29 = re.compile(r'(?<=# Assembly name:).*')
pattern30 = re.compile(r'(?<=all	all	all	all	spanned-gaps	)\d+\.?\d')

contig_L50_list=[]
contig_N50_list=[]
contig_count_list=[]
molecule_count_list=[]
region_count_list=[]
scaffold_L50_list=[]
scaffold_N50_list=[]
scaffold_N75_list=[]
scaffold_N90_list=[]
scaffold_count_list=[]
top_level_count_list=[]
total_gap_length_list=[]
total_length_list=[]
ungapped_length_list=[]
unspanned_gaps_list=[]
component_count_list=[]
Organism_name_list=[]
Infraspecific_name_list=[]
Taxid_list=[]
BioSample_list=[]
BioProject_list=[]
Submitter_list=[]
Date_list=[]
Release_type_list=[]
Assembly_level_list=[]
Genome_representation_list=[]
WGS_project_list=[]
Genome_coverage_list=[]
GenBank_assembly_accession_list=[]
Assembly_name_list=[]
spanned_gaps_list=[]
ee="D:\Study\\Z_Work\\LX\\Data\Get_assembly\\assembly_data\\"


for i in range(len(file_name)):
	url = ee + file_name[i]
	f = open(url, "r")  # 设置文件对象
	str = f.read()  # 将txt文件的所有内容读入到字符串str中
	f.close()
	component_count = "XXXXX"
	contig_L50 = "XXXXX"
	contig_N50 = "XXXXX"
	contig_count = "XXXXX"
	molecule_count = "XXXXX"
	region_count = "XXXXX"
	scaffold_L50 = "XXXXX"
	scaffold_N50 = "XXXXX"
	scaffold_N75 = "XXXXX"
	scaffold_N90 = "XXXXX"
	scaffold_count = "XXXXX"
	top_level_count = "XXXXX"
	total_gap_length = "XXXXX"
	total_length = "XXXXX"
	ungapped_length = "XXXXX"
	unspanned_gaps = "XXXXX"
	Organism_name = "XXXXX"
	Infraspecific_name = "XXXXX"
	Taxid = "XXXXX"
	BioSample = "XXXXX"
	BioProject = "XXXXX"
	Submitter = "XXXXX"
	Date = "XXXXX"
	Release_type = "XXXXX"
	Assembly_level = "XXXXX"
	Genome_representation = "XXXXX"
	WGS_project = "XXXXX"
	Genome_coverage = "XXXXX"
	GenBank_assembly_accession = "XXXXX"
	Assembly_name="XXXXX"
	spanned_gaps="XXXXX"
	component_count=pattern.findall(str)
	contig_L50=pattern1.findall(str)
	contig_N50=pattern2.findall(str)
	contig_count=pattern3.findall(str)
	molecule_count=pattern4.findall(str)
	region_count=pattern5.findall(str)
	scaffold_L50=pattern6.findall(str)
	scaffold_N50=pattern7.findall(str)
	scaffold_N75=pattern8.findall(str)
	scaffold_N90=pattern9.findall(str)
	scaffold_count=pattern10.findall(str)
	top_level_count=pattern11.findall(str)
	total_gap_length=pattern12.findall(str)
	total_length=pattern13.findall(str)
	ungapped_length=pattern14.findall(str)
	unspanned_gaps=pattern15.findall(str)
	Organism_name = pattern16.findall(str)
	Infraspecific_name = pattern17.findall(str)
	Taxid = pattern18.findall(str)
	BioSample = pattern19.findall(str)
	BioProject = pattern20.findall(str)
	Submitter = pattern21.findall(str)
	Date = pattern22.findall(str)
	Release_type = pattern23.findall(str)
	Assembly_level = pattern24.findall(str)
	Genome_representation = pattern25.findall(str)
	WGS_project = pattern26.findall(str)
	Genome_coverage = pattern27.findall(str)
	GenBank_assembly_accession = pattern28.findall(str)
	Assembly_name=pattern29.findall(str)
	spanned_gaps=pattern30.findall(str)
	contig_L50_list.append(contig_L50)
	contig_N50_list.append(contig_N50)
	contig_count_list.append(contig_count)
	molecule_count_list.append(molecule_count)
	region_count_list.append(region_count)
	scaffold_L50_list.append(scaffold_L50)
	scaffold_N50_list.append(scaffold_N50)
	scaffold_N75_list.append(scaffold_N75)
	scaffold_N90_list.append(scaffold_N90)
	scaffold_count_list.append(scaffold_count)
	top_level_count_list.append(top_level_count)
	total_gap_length_list.append(total_gap_length)
	total_length_list.append(total_length)
	ungapped_length_list.append(ungapped_length)
	unspanned_gaps_list.append(unspanned_gaps)
	component_count_list.append(component_count)
	Organism_name_list.append(Organism_name)
	Infraspecific_name_list.append(Infraspecific_name)
	Taxid_list.append(Taxid)
	BioSample_list.append(BioSample)
	BioProject_list.append(BioProject)
	Submitter_list.append(Submitter)
	Date_list.append(Date)
	Release_type_list.append(Release_type)
	Assembly_level_list.append(Assembly_level)
	Genome_representation_list.append(Genome_representation)
	WGS_project_list.append(WGS_project)
	Genome_coverage_list.append(Genome_coverage)
	GenBank_assembly_accession_list.append(GenBank_assembly_accession)
	Assembly_name_list.append(Assembly_name)
	spanned_gaps_list.append(spanned_gaps)
	component_count = "XXXXX"
	contig_L50 = "XXXXX"
	contig_N50 = "XXXXX"
	contig_count = "XXXXX"
	molecule_count = "XXXXX"
	region_count = "XXXXX"
	scaffold_L50 = "XXXXX"
	scaffold_N50 = "XXXXX"
	scaffold_N75 = "XXXXX"
	scaffold_N90 = "XXXXX"
	scaffold_count = "XXXXX"
	top_level_count = "XXXXX"
	total_gap_length = "XXXXX"
	total_length = "XXXXX"
	ungapped_length = "XXXXX"
	unspanned_gaps = "XXXXX"
	Organism_name = "XXXXX"
	Infraspecific_name = "XXXXX"
	Taxid = "XXXXX"
	BioSample = "XXXXX"
	BioProject = "XXXXX"
	Submitter = "XXXXX"
	Date = "XXXXX"
	Release_type = "XXXXX"
	Assembly_level = "XXXXX"
	Genome_representation = "XXXXX"
	WGS_project = "XXXXX"
	Genome_coverage = "XXXXX"
	GenBank_assembly_accession = "XXXXX"
	Assembly_name = "XXXXX"
	spanned_gaps = "XXXXX"
component_count_list=pd.DataFrame(component_count_list)
contig_L50_list=pd.DataFrame(contig_L50_list)
contig_N50_list=pd.DataFrame(contig_N50_list)
contig_count_list=pd.DataFrame(contig_count_list)
molecule_count_list=pd.DataFrame(molecule_count_list)
region_count_list=pd.DataFrame(region_count_list)
scaffold_L50_list=pd.DataFrame(scaffold_L50_list)
scaffold_N50_list=pd.DataFrame(scaffold_N50_list)
scaffold_N75_list=pd.DataFrame(scaffold_N75_list)
scaffold_N90_list=pd.DataFrame(scaffold_N90_list)
scaffold_count_list=pd.DataFrame(scaffold_count_list)
top_level_count_list=pd.DataFrame(top_level_count_list)
total_gap_length_list=pd.DataFrame(total_gap_length_list)
total_length_list=pd.DataFrame(total_length_list)
ungapped_length_list=pd.DataFrame(ungapped_length_list)
unspanned_gaps_list=pd.DataFrame(unspanned_gaps_list)
component_count_list=pd.DataFrame(component_count_list)
Organism_name_list=pd.DataFrame(Organism_name_list)
Infraspecific_name_list=pd.DataFrame(Infraspecific_name_list)
Taxid_list=pd.DataFrame(Taxid_list)
BioSample_list=pd.DataFrame(BioSample_list)
BioProject_list=pd.DataFrame(BioProject_list)
Submitter_list=pd.DataFrame(Submitter_list)
Date_list=pd.DataFrame(Date_list)
Release_type_list=pd.DataFrame(Release_type_list)
Assembly_level_list=pd.DataFrame(Assembly_level_list)
Genome_representation_list=pd.DataFrame(Genome_representation_list)
WGS_project_list=pd.DataFrame(WGS_project_list)
Genome_coverage_list=pd.DataFrame(Genome_coverage_list)
GenBank_assembly_accession_list=pd.DataFrame(GenBank_assembly_accession_list)
Assembly_name_list=pd.DataFrame(Assembly_name_list)
spanned_gaps_list=pd.DataFrame(spanned_gaps_list)
contig_L50_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\contig_L50_list.xlsx")
contig_N50_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\contig_N50_list.xlsx")
contig_count_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\contig_count_list.xlsx")
molecule_count_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\molecule_count_list.xlsx")
region_count_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\region_count_list.xlsx")
scaffold_L50_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\scaffold_L50_list.xlsx")
scaffold_N50_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\scaffold_N50_list.xlsx")
scaffold_N75_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\scaffold_N75_list.xlsx")
scaffold_N90_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\scaffold_N90_list.xlsx")
scaffold_count_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\scaffold_count_list.xlsx")
top_level_count_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\top_level_count_list.xlsx")
total_gap_length_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\total_gap_length_list.xlsx")
total_length_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\total_length_list.xlsx")
ungapped_length_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\ungapped_length_list.xlsx")
unspanned_gaps_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\unspanned_gaps_list.xlsx")
component_count_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\component_count_list.xlsx")
Organism_name_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Organism_name_list.xlsx")
Infraspecific_name_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Infraspecific_name_list.xlsx")
Taxid_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Taxid_list.xlsx")
BioSample_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\BioSample_list.xlsx")
BioProject_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\BioProject_list.xlsx")
Submitter_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Submitter_list.xlsx")
Date_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Date_list.xlsx")
Release_type_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Release_type_list.xlsx")
Assembly_level_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Assembly_level_list.xlsx")
Genome_representation_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Genome_representation_list.xlsx")
WGS_project_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\WGS_project_list.xlsx")
Genome_coverage_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Genome_coverage_list.xlsx")
GenBank_assembly_accession_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\GenBank_assembly_accession_list.xlsx")
Assembly_name_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\Assembly_name_list.xlsx")
spanned_gaps_list.to_excel(r"D:\Study\Z_Work\LX\Data\Get_assembly\assembly_data_2_list\spanned_gaps_list.xlsx")





