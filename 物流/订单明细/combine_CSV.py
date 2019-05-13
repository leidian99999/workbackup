import os
import pandas as pd
import glob

date = "1904"
xls2csvPath = "/root/lnglat_gaode/temp/xls2csv/"  #输出目录
xlsPath  = "/root/lnglat_gaode/temp/yuan/"  #读取目录
csvPath = "/root/lnglat_gaode/temp/csv/"



#建立单个文件的excel转换成csv函数,file 是excel文件名，to_file 是csv文件名。
def excel_to_csv(file,to_file):
    data_xls=pd.read_excel(file,sheet_name=0)
    data_xls.to_csv(to_file,encoding='utf_8_sig')


#读取一个目录里面的所有文件：
def read_path(path):
    dirs=os.listdir(path)
    return dirs

 #将源文件路径里面的文件转换成列表file_list
file_list=[xlsPath+i for i in read_path(xlsPath)]
j=1
#建立循环对于每个文件调用excel_to_csv()
for it in file_list:
    #给目标文件新建一些名字列表
    j_mid=str(j)
    j_csv=xls2csvPath+j_mid+".csv"
    excel_to_csv(it,j_csv)
    print(it)
    j=j+1



csv_list = glob.glob(xls2csvPath + '*.csv') #查看同文件夹下的csv文件数
print(u'共发现%s个CSV文件'% len(csv_list))
print(u'正在处理............')
for i in csv_list: #循环读取同文件夹下的csv文件
    fr = open(i,'rb').read()
    with open(csvPath + date + 'info.csv','ab') as f: #将结果保存为csv
        f.write(fr)
print(u'合并完毕！')
