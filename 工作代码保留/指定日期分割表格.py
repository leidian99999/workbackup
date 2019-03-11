import pandas as pd
import datetime 
import os
import openpyxl
import re

# 输出指定sheet到新表
def putout_sheets(datapath1,outpath1):
    sheet1 = pd.read_excel(datapath1,sheet_name="昨日省份激活率",header=1)
    sheet2 = pd.read_excel(datapath1,sheet_name="昨日产品激活率",header=1)
    writer = pd.ExcelWriter(outpath1)
    sheet1.to_excel(writer,sheet_name="昨日省份激活率",index=False)
    sheet2.to_excel(writer,sheet_name="昨日产品激活率",index=False)
    writer.save()
    return sheet1,sheet2

# 删除指定sheet名称

def putout_rest_sheet(datapath3,outpath2,delsheet):
	workbook = openpyxl.load_workbook(datapath3)
	for i in delsheet:
		workbook.remove_sheet(workbook.get_sheet_by_name(i))
		workbook._active_sheet_index = 0
		workbook.save(outpath2)

# 读取文件夹下所有文件名
def all_path(datapath2):
    filepaths = []#所有的文件
    filenames = []
    for maindir, subdir, file_name_list in os.walk(datapath2):
        #os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
        print("当前目录:",maindir) #当前主目录
        print("当前目录下所有目录:",subdir) #当前主目录下的所有目录
        print("当前主目录下的所有文件:",file_name_list)  #当前主目录下的所有文件
        print("*"*50)
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            filepaths.append(apath)
            filenames.append(filename)
    return filenames,filepaths


if __name__=='__main__':
    datapath2 = "F:/temp/190214/yuan/"
    delsheet = ["昨日省份激活率", "昨日产品激活率"]

    allfilenames,allfilepaths = all_path(datapath2)
    # 读取所有文件
    for filepath in allfilepaths:

        filename = ''.join(re.findall("F:/temp/190214/yuan/(.*)",filepath))# 输出前2个sheet并保存
        outpath1 = "F:/temp/190214/output_qian/" + "前2个sheet" + filename
        putout_sheets(filepath,outpath1)

        # 删除钱两个sheet并输出其余sheet
        outpath2 = "F:/temp/190214/output_hou/" + "其余sheet" + filename
        putout_rest_sheet(filepath,outpath2,delsheet)
