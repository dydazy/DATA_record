library(readr)
Assembly=read.csv("D:\\Study\\Z_Work\\LX\\Data\\Get_assembly\\assembly_summary_genbank.csv",header = T,encoding = 'UTF-8')
#Assembly=read.csv("D:\\Study\\Z_Work\\LX\\Data\\Get_assembly\\assembly_summary_genbank_WG.csv",header = T,encoding = 'UTF-8')
data=read.csv("D:\\Study\\Z_Work\\LX\\Data\\Get_assembly\\Angiospermae.csv",header = T,encoding = 'UTF-8')

#flag=data.frame(matrix(length(data[,9]),100))
#x=0

for(i in 1:length(data[,9]))
  {
  if (data[i,9] %in% Assembly$organism_name)
    {
     #e=length(which(Assembly$organism_name==data[i,9]))  
     #flag[i,1:e]=which(Assembly$organism_name==data[i,9])
     assembly_1=Assembly[which(Assembly$organism_name==data[i,9]),]
     write_csv(assembly_1, "D:\\Study\\Z_Work\\LX\\Data\\Get_assembly\\assembly_summary_genbank_flowers.csv",append = T)
     #x=x+e
  }
}

#write.csv(flag,"D:\\Study\\Z_Work\\LX\\Data\\Get_assembly\\Assembly_in_data.csv")

#获取assembly id

























