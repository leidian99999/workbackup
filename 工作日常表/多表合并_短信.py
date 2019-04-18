# -*- coding: utf-8 -*-

#将多个Excel文件合并成一个
import xlrd
import xlsxwriter
import os
from datetime import datetime
import time

starttime = datetime.now()


#打开一个excel文件
def open_xls(file):
    fh=xlrd.open_workbook(file)
    return fh

#获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()

#获取sheet表的行数
def getnrows(fh,sheet):
    table=fh.sheets()[sheet]
    return table.nrows

#读取文件内容并返回行内容
def getFilect(file,shnum):
    fh=open_xls(file)
    table=fh.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue

#获取sheet表的个数
def getshnum(fh):
    x=0
    sh=getsheet(fh)
    for sheet in sh:
        x+=1
    return x




def all_path(dirname):
    result = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        #os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
        print("当前目录:",maindir) #当前主目录
        print("当前目录下所有目录:",subdir) #当前主目录下的所有目录
        print("当前主目录下的所有文件:",file_name_list)  #当前主目录下的所有文件
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)

    return result



if __name__=='__main__':
    # fold = ""
    disk = "G"
    #定义要合并的excel文件列表
    fold_zong = disk + ":\\work\\basic\\carriers\\1901\\output\\"  #输出文件目录
    allxls = all_path( disk + ":\\work\\basic\\carriers\\1901\\output\\gaode\\")  #读取文件目录
    #存储所有读取的结果
    datavalue=[]
    for fl in allxls: 
        fh=open_xls(fl)
        x=getshnum(fh)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=getFilect(fl,shnum)
    #定义最终合并后生成的新文件

        endfile =  fold_zong  + "1901info_lnglat_gaode.xlsx"
    wb1=xlsxwriter.Workbook(endfile)
    #创建一个sheet工作对象
    print("开始合表中。。。。。")
    ws=wb1.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            ws.write(a,b,c)
    wb1.close()
    print("文件合并完成")

    # data_new = open_xls(endfile)
    # table_new = data_new.sheet_by_index(0)
    # print(table_new.nrows)
endtime = datetime.now()
print("耗时（秒）")
print((endtime - starttime).seconds)