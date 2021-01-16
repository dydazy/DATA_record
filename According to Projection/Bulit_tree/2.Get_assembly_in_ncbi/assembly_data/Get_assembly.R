Assembly=read.csv("D:\\Study\\Z_Work\\LX\\Data\\assembly_summary_genbank.csv",header = T,encoding = 'UTF-8')
data=read.csv("D:\\Study\\Z_Work\\LX\\Data\\Angiospermae.csv",header = T,encoding = 'UTF-8')

flag=data.frame(matrix(NA,length(data[,9]),100))
x=0
for(i in 1:length(data[,9]))
  {
  if (data[i,9] %in% Assembly[,8])
    {
    e=length(which(Assembly$organism_name==data[i,9]))  
    flag[i,1:e]=which(Assembly$organism_name==data[i,9])
  }
}
write.csv(flag,"D:\\Study\\Z_Work\\LX\\Data\\Assembly_in_data.csv")

#获取assembly id








