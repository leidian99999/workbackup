# coding=utf-8
import xlrd
import pandas as pd
from  pandas import DataFrame
from openpyxl import load_workbook
import os





def combine_sheets(inputPath,inputName):
    wb = xlrd.open_workbook(inputPath + inputName)
    # 获取workbook中所有的表格
    sheets = wb.sheet_names()
    # 循环遍历所有sheet
    allSheets = DataFrame()
    for i in range(len(sheets)):
        df = pd.read_excel(inputPath + inputName, sheet_name=i, index=False, encoding='utf8')
        allSheets = allSheets.append(df)
    #输出
    # writer = pd.ExcelWriter(inputPath+"allData.xlsx",engine='openpyxl')
    # allData.to_excel(excel_writer=writer,sheet_name="ALLDATA",index=False)
    # writer.save()
    # writer.close()
    return allSheets

def combin_excels(inputPath,outputPath,outFileName):
    for maindir, subdir, file_name_list in os.walk(inputPath):
        print("当前主目录下的所有文件:", file_name_list)
        allData = DataFrame()
        for file in file_name_list:
            allData = allData.append(combine_sheets(inputPath,file))

        allData.to_csv(outputPath + outFileName,index=False)
        # allData.to_excel(outputPath + outFileName,index=False)

        # writer = pd.ExcelWriter(outputPath+outFileName+".xlsx",engine='openpyxl')
        # allData.to_excel(excel_writer=writer,sheet_name="ALLDATA",index=False)
        # writer.save()

# for root,dirs,files in walk(inputPath + "3日 7日前Ctrl189导出/",topdown=False):
#     print(files)
# num = len(files)
# df1 = pd.DataFrame()
# for i in range(num):
#     newdata = pd.read_excel(inputPath + '3日 7日前Ctrl189导出/%s'%files[i])
#     df1 = df1.append(newdata) # 189

if __name__=='__main__':
    # inputName = 'test1.xlsx'  #表格地址+表格名
    # inputPath = "G:/work/daily/DataShow/190613/"
    # outputPath = "G:/work/daily/DataShow/test/"
    # outFileName = "大傻逼.csv"
    inputPath2 = "D:/work/daily/DataShow/"
    combin_excels(inputPath2 + "6.8-6.13CHZH_Info/",inputPath2,"CHZHInfo"+".csv")
