#get ncbi data ( 382 species )
#species is or not have anoation
import requests
import re
import pandas as pd
from pandas import read_excel
species_PRJNA=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\5.PRJNA_to_GCA\species_PRJNA.xlsx",sheet_name="Sheet2")
ftp_path=species_PRJNA["ftp_path"].to_list()
assembly_id=species_PRJNA["assembly_accession"].to_list()
species=species_PRJNA["organism_name"].to_list()
infromation=pd.DataFrame(index=range(len(species)),columns=["species","assembly_id","assembly_structure",'assembly_report', 'assembly_stats', 'cds_from_genomic', 'feature_count',"feature_table","genomic.fna"
	,"genomic.gbff","genomic.gff","genomic.gtf","genomic_gaps","protein.faa","protein.gpff","rna_from_genomic.fna","translated_cds.faa","wgsmaster.gbff"])
infromation.loc[range(len(species)),'assembly_id']=assembly_id
infromation.loc[range(len(species)),'species']=species
for i in range(len(species)):
	ftp_html = requests.get(ftp_path[i])
	text = ftp_html.text
	infromation.loc[i,'assembly_structure']= (r"_assembly_structure" in text)
	infromation.loc[i,'assembly_report']=(r"assembly_report.txt" in text)
	infromation.loc[i,'assembly_stats']=(r"assembly_stats.txt" in text)
	infromation.loc[i,'cds_from_genomic']=(r"cds_from_genomic.fna" in text)
	infromation.loc[i,'feature_count']=(r"feature_count.txt" in text)
	infromation.loc[i,'feature_table']=(r"feature_table.txt" in text)
	infromation.loc[i,'genomic.fna']=(r"genomic.fna" in text)
	infromation.loc[i,'genomic.gbff']=(r"genomic.gbff" in text)
	infromation.loc[i,'genomic.gff']=(r"genomic.gff" in text)
	infromation.loc[i,'genomic.gtf']=(r"genomic.gtf" in text)
	infromation.loc[i,'genomic_gaps']=(r"genomic_gaps" in text)
	infromation.loc[i,'protein.faa']=(r"protein.faa" in text)
	infromation.loc[i,'protein.gpff']=(r"protein.gpff.gz" in text)
	infromation.loc[i,'rna_from_genomic.fna']=(r"rna_from_genomic.fna" in text)
	infromation.loc[i,'translated_cds.faa']=(r"translated_cds.faa" in text)
	infromation.loc[i,'wgsmaster.gbff']=(r"wgsmaster.gbf" in text)
	text=""

print(infromation)
infromation.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\5.PRJNA_to_GCA\information_GCA.xlsx")


# print(ftp_html.content)

