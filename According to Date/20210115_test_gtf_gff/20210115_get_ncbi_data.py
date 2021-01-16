#get ncbi data ( 382 species )
#species is or not have anoation
import requests
import re
import pandas as pd
from pandas import read_excel
species_382=read_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\species_assembly_id_ftp_382_melt.xlsx")
ftp_path=species_382["ftp_path"].to_list()
assembly_id=species_382["assembly_id"].to_list()
species=species_382["species"].to_list()
infromation=pd.DataFrame(index=range(939),columns=["species","assembly_id","assembly_structure",'assembly_report', 'assembly_stats', 'cds_from_genomic', 'feature_count',"feature_table","genomic.fna"
	,"genomic.gbff","genomic.gff","genomic.gtf","genomic_gaps","protein.faa","protein.gpff","rna_from_genomic.fna","translated_cds.faa","wgsmaster.gbff"])
infromation.loc[:,'assembly_id']=assembly_id
infromation.loc[:,'species']=species
for i in range(939):
	ftp_html = requests.get(ftp_path[i])
	text = ftp_html.text
	# infromation.loc[i,'assembly_structure']= (r"_assembly_structure" in text)
	# infromation.loc[i,'assembly_report']=(r"_assembly_report.txt" in text)
	# infromation.loc[i,'assembly_stats']=(r"_assembly_stats.txt" in text)
	# infromation.loc[i,'cds_from_genomic']=(r"_cds_from_genomic.fna.gz" in text)
	# infromation.loc[i,'feature_count']=(r"_feature_count.txt.gz" in text)
	# infromation.loc[i,'feature_table']=(r"_feature_table.txt.gz" in text)
	# infromation.loc[i,'genomic.fna']=(r"_genomic.fna.gz" in text)
	# infromation.loc[i,'genomic.gbff']=(r"_genomic.gbff.gz" in text)
	# infromation.loc[i,'genomic.gff']=(r"_genomic.gff.gz" in text)
	# infromation.loc[i,'genomic.gtf']=(r"genomic.gtf.gz" in text)
	# infromation.loc[i,'genomic_gaps']=(r"_genomic_gaps.txt.gz" in text)
	# infromation.loc[i,'protein.faa']=(r"_protein.faa.gz" in text)
	# infromation.loc[i,'protein.gpff']=(r"_protein.gpff.gz" in text)
	# infromation.loc[i,'rna_from_genomic.fna']=(r"_rna_from_genomic.fna.gz" in text)
	# infromation.loc[i,'translated_cds.faa']=(r"_translated_cds.faa.gz" in text)
	# infromation.loc[i,'wgsmaster.gbff']=(r"_wgsmaster.gbff.gz" in text)
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
infromation.to_excel(r"D:\Study\Z_Work\LX\Data\Bulit_tree\3.Get_species_in_ncbi\information_GCF.xlsx")


# print(ftp_html.content)

