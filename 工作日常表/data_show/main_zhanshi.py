import pandas as pd
import xlsxwriter
from os import walk
from def_zhanshi import *
from def_fiveTables import *
from def_fiveTables2 import *
from datetime import datetime
import time

starttime = datetime.now()
date = '19/06/06'  # 表中日期
filename = 'test190606.xlsx'  # 输出文件名
inputPath = "D:/work/dataShow/190606/"  # 输出路径

rows1  = 17  # 昨日产品行数
rows3  = 13  # 3日产品行数
rows7  = 14  # 7日产品行数
rows15 = 14  # 15日产品行数

date1 = '190606'  # 文件名日期



'''读取数据'''
# 产品标卡
biaoka = pd.read_excel(inputPath + "产品标卡.xlsx")
biaoka["销售品编号"] = biaoka["销售品编号"].map(lambda x: str(x))

# 数据集1
data1 = pd.read_excel(inputPath + "A1_sign_active_1.xlsx",
                      skiprows=3,
                      header=0,
                      sheet_name="8日前签收时效合计",
                      nrows=100)
data1 = data1.drop(columns=["Unnamed: 0"], axis=1)
data1 = data1.fillna(method="ffill")
data1 = data1.iloc[:-2]
data1 = data1[data1["承运商"].str.contains("京东线下") == False]

# 数据集2




# 数据集3
data3 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                      skiprows=41,
                      header=None,
                      sheet_name="生产流程分省情况",
                      nrows=32)

# 数据集4
data4 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                      skiprows=4,
                      header=None,
                      sheet_name="生产流程分产品情况",
                      nrows=rows1)

# 数据集5
data5 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                     skiprows=4,
                     header=None,
                     sheet_name="激活时效",
                     nrows=6)

data5 = data5.drop([0, 1], axis=1)

# 数据集6
data6 = pd.read_excel(inputPath + "激活展示总表.xlsx")
# data6 = data6.drop(columns=["总计"])
data6["日期"] = data6["日期"].dt.strftime('%y/%m/%d')
data6["日期"] = data6["日期"].map(lambda x : str(x))
new=pd.DataFrame({'日期':date,
                  '4日激活占比':data5.iloc[0,2],
                  '5-10天激活占比':data5.iloc[1,2],
                  '11-15天激活占比':data5.iloc[2,2],
                  '16-30天激活占比':data5.iloc[3,2],
                  '30天以上激活占比':data5.iloc[4,2]},
                 index=[1]
                 )
data6 = data6.append(new,ignore_index=True)


# 数据集7
data7 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng_3day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程分省情况",
                      nrows=32)
# 数据集8

data8 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng_3day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程产品情况",
                      nrows=rows3)

# 数据集：京东，盲投 (3日)
# for root,dirs,files_3ri in walk(inputPath + "3日",topdown=False):
#     print(files_3ri)
# num_3ri = len(files_3ri)
# df1_3ri = pd.DataFrame()
# for i in range(num_3ri):
#     newdata_3ri = pd.read_excel(inputPath + '3日\%s'%files_3ri[i])
#     df1_3ri = df1_3ri.append(newdata_3ri) # 189
# df1_3ri.to_excel(inputPath + "df1_3ri.xlsx",index=False)

df1_3ri = pd.read_excel(inputPath + "df1_3ri.xlsx")
df2_3ri = pd.read_excel(inputPath + "三日新生产"+ date1 + ".xlsx") # 新生产表
df3_3ri = pd.read_excel(inputPath + "首充明细.xlsx", sheet_name="Sheet1") # 首充历史表
df4_3ri = pd.read_excel(inputPath + "首充新增.xlsx") # 当日历史表
df5_3ri = pd.read_excel(inputPath + "京东3日" + date1 +".xlsx") # 京东表
data_JM3 = five_tables(df1_3ri, df2_3ri, df3_3ri, df4_3ri, df5_3ri)
data_JM3 = pd.merge(data_JM3, biaoka, how="left", on="销售品编号")

# data_JM3.to_excel(inputPath + "data_JM3.xlsx",index=False)


# 数据集：京东，盲投 (7日)
# for root,dirs,files_7ri in walk(inputPath + "7日",topdown=False):
#     print(files_7ri)
# num_7ri = len(files_7ri)
# df1_7ri = pd.DataFrame()
# for i in range(num_7ri):
#     newdata_7ri = pd.read_excel(inputPath + '7日\%s'%files_7ri[i])
#     df1_7ri = df1_7ri.append(newdata_7ri) # 189
# df1_7ri.to_excel(inputPath + "df1_7ri.xlsx",index=False)

df1_7ri = pd.read_excel(inputPath + "df1_7ri.xlsx")
df2_7ri = pd.read_excel(inputPath + "七日新生产"+ date1 + ".xlsx") # 新生产表
df3_7ri = pd.read_excel(inputPath + "首充明细.xlsx", sheet_name="Sheet1") # 首充历史表
df4_7ri = pd.read_excel(inputPath + "首充新增.xlsx") # 当日历史表
df5_7ri = pd.read_excel(inputPath + "京东7日" + date1 +".xlsx") # 京东表
data_JM7 = five_tables(df1_7ri, df2_7ri, df3_7ri, df4_7ri, df5_7ri)

data_JM7 = pd.merge(data_JM7, biaoka, how="left", on="销售品编号")
# data_JM7.to_excel(inputPath + "data_JM7.xlsx",index=False)

# 数据集11
data11 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程分省情况",
                      nrows=32)

# 数据集12
data12 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程产品情况",
                      nrows=rows7)

# 数据集17
data17 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng_15day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程分省情况",
                      nrows=32)

# 数据集18
data18 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng_15day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程产品情况",
                      nrows=rows15)



'''数据清洗'''
data3 = cleanquan(data3)
data4 = cleanquan(data4)
data7 = clean271525(data7)
data8 = clean271525(data8)
data9 = JD_mode_province(data_JM3)
data10 = JD_mode_product(data_JM3)
data11 = clean271525(data11)
data12 = clean271525(data12)
data13 = M_mode_province(data_JM7)
data14 = M_mode_product(data_JM7)
data15 = JD_mode_province(data_JM7)
data16 = JD_mode_product(data_JM7)
data17 = clean271525(data17)
data18 = clean271525(data18)





# 设置输出sheet
workbook = xlsxwriter.Workbook(inputPath + filename)
worksheet1 = workbook.add_worksheet("1、签收时效")
worksheet2 = workbook.add_worksheet("2、地址校验")
worksheet3 = workbook.add_worksheet("3、昨日省份激活率")
worksheet4 = workbook.add_worksheet("4、昨日产品激活率")
worksheet5 = workbook.add_worksheet("5、昨日激活时效")
worksheet6 = workbook.add_worksheet("6、激活展示")
worksheet7 = workbook.add_worksheet("7、3日省份激活率")
worksheet8 = workbook.add_worksheet("8、3日产品激活率")
worksheet9  = workbook.add_worksheet("9、3日京东模式省份情况")
worksheet10 = workbook.add_worksheet("10、3日京东模式产品情况")
worksheet11 = workbook.add_worksheet("11、7日省份激活率")
worksheet12 = workbook.add_worksheet("12、7日产品激活率")
worksheet13 = workbook.add_worksheet("13、7日盲投省份情况 ")
worksheet14 = workbook.add_worksheet("14、7日盲投产品情况 ")
worksheet15 = workbook.add_worksheet("15、7日京东模式省份情况 ")
worksheet16 = workbook.add_worksheet("16、7日京东模式产品情况 ")
worksheet17 = workbook.add_worksheet("17、15日省份激活率")
worksheet18 = workbook.add_worksheet("18、15日产品激活率")
worksheet19 = workbook.add_worksheet("19、25日省份激活率")
worksheet20 = workbook.add_worksheet("20、25日产品激活率")
# worksheet21 = workbook.add_worksheet("21、京粉汇总")
# worksheet22 = workbook.add_worksheet("22、米粉汇总")
# worksheet23 = workbook.add_worksheet("23、激活总计情况")
# worksheet24 = workbook.add_worksheet("24、盲投不含转线上")
# worksheet25 = workbook.add_worksheet("25、京东线下转化率含转线上")


headers1 = ['省份',"来单量",'拦截量','卡单量','v4待上传','异常量','发货量','发货率','激活量','激活比例']
headers2 = ["激活时效","激活数量","激活占比"]
headers3 = ['日期','4日激活占比','5-10日激活占比','11-15日激活占比','16-30日激活占比','30天以上激活占比']


# 设置样式
date_format = workbook.add_format({"pattern": 1,
                                   "bg_color": '#B7CFE9',
                                   "align": 'center',
                                   "valign": 'vcenter',
                                   'bold': True, 'border': 1,
                                   })



header_format1 = workbook.add_format({"pattern": 1,
                                     "bg_color": '#ECDDD2',
                                     "align": 'center',
                                     "valign": 'vcenter',
                                     'border': 1,
                                     })
header_format2 = workbook.add_format({"pattern": 1,
                                      "bg_color": '#8689A2',
                                      "align": 'center',
                                      "valign": 'vcenter',
                                      'border': 1,
                                      'bold': True,
                                      "font_size": 10})
header_format3 = workbook.add_format({"pattern": 1,
                                      "bg_color": '#FFFF00',
                                      "align": 'center',
                                      "valign": 'vcenter',
                                      'border': 1,
                                      'bold': True,
                                      'font_size': 10})
header_format4 = workbook.add_format({"pattern": 1,
                                      "bg_color": '#92D050',
                                      "align": 'center',
                                      "valign": 'vcenter',
                                      'border': 1,
                                      'bold': True,
                                      'font_size': 10})
header_format5 = workbook.add_format({"pattern": 1,
                                      "bg_color": '#C69A7D',
                                      "align": 'center',
                                      "valign": 'vcenter',
                                      'border': 1,
                                      'bold': True,
                                      'font_size': 10})
header_format6 = workbook.add_format({"pattern": 1,
                                      "bg_color": '#00B0F0',
                                      "align": 'center',
                                      "valign": 'vcenter',
                                      'border': 1,
                                      'bold': True,
                                      'font_size': 10})


data_format = workbook.add_format({"pattern": 1,
                                   "bg_color": '#cccccc',
                                   "align": 'center',
                                   "valign": 'vcenter',
                                   'border': 1,
                                   'font_name': 'Microsoft YaHei'
                                   })
data_format2 = workbook.add_format({"pattern": 1,
                                   "bg_color": '#cccccc',
                                   "align": 'center',
                                   "valign": 'vcenter',
                                   'border': 1,
                                   'font_name': 'Microsoft YaHei',
                                    'num_format': '0.00%'})
SUM_format1 = workbook.add_format({"align": 'center',
                                   "valign": 'vcenter',
                                   'border': 1,
                                   'font_name': 'Microsoft YaHei'
                                   })
SUM_format2 = workbook.add_format({"align": 'center',
                                   "valign": 'vcenter',
                                   'border': 1,
                                   'font_name': 'Microsoft YaHei',
                                   'num_format': '0.00%'
                                   })


# 写入标题
worksheet1.merge_range('A1:H1', date + "签收时效合计", date_format)  # 合并单元格
worksheet3.merge_range('A1:J1', date, date_format)
worksheet3.write_row('A2', headers1, header_format1)
worksheet4.merge_range('A1:J1', date, date_format)
worksheet4.write_row('A2', headers1, header_format1)
worksheet5.merge_range('A1:C1', date + "签收时效合计", date_format)
worksheet5.write_row('A2', headers2, header_format2)
worksheet6.write_row('A1', headers3, header_format2)
yangshi371525(worksheet7,'省份','   3日分省',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet8,'产品','   3日产品',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi37JD  (worksheet9,'省份','   3日京东模式省份数据',date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6)
yangshi37JD  (worksheet10,'产品','   3日京东模式产品数据',date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6)
yangshi371525(worksheet11,'省份','   7日分省数据',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet12,'产品','   7日产品数据',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi37Mang  (worksheet13,'省份','   7日盲投省份数据',date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6)
yangshi37Mang  (worksheet14,'产品','   7日盲投产品数据',date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6)
yangshi37JD  (worksheet15,'省份','   7日京东模式省份情况',date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6)
yangshi37JD  (worksheet16,'产品','   7日京东模式产品情况',date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6)
yangshi371525(worksheet17,'省份','   15日分省数据',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet18,'产品','   15日产品数据',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet19,'省份','   25日分省数据',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet20,'产品','   25日产品数据',date,date_format,header_format2,header_format3,header_format4,header_format5)


# 设定行格式
worksheet1.set_column('A:H', 10)
for i in range(100):
    worksheet3.set_row(i, 20)

worksheet3.set_column('A:J', 10)
for i in range(24):
    worksheet3.set_row(i, 20)

worksheet4.set_column('A:J', 10)
for i in range(rows1):
    worksheet4.set_row(i, 20)

worksheet5.set_column('A:C', 12)
for i in range(100):
    worksheet5.set_row(i, 15)

worksheet6.set_column('A:F', 16)
for i in range(100):
    worksheet6.set_row(i, 20)

worksheet7.set_column('A:O', 12)
for i in range(100):
    worksheet7.set_row(i, 15)

worksheet8.set_column('A:O', 12)
for i in range(100):
    worksheet8.set_row(i, 15)

worksheet9.set_column('A:R', 15)
for i in range(100):
    worksheet9.set_row(i, 15)

worksheet10.set_column('A:R', 15)
for i in range(100):
    worksheet10.set_row(i, 15)

worksheet11.set_column('A:O', 12)
for i in range(100):
    worksheet11.set_row(i, 15)

worksheet12.set_column('A:O', 12)
for i in range(100):
    worksheet12.set_row(i, 15)

worksheet13.set_column('A:U', 12)
for i in range(100):
    worksheet13.set_row(i, 15)

worksheet14.set_column('A:U', 12)
for i in range(100):
    worksheet14.set_row(i, 15)

worksheet15.set_column('A:R', 15)
for i in range(100):
    worksheet15.set_row(i, 15)

worksheet16.set_column('A:R', 15)
for i in range(100):
    worksheet16.set_row(i, 15)

worksheet17.set_column('A:O', 12)
for i in range(100):
    worksheet17.set_row(i, 15)

worksheet18.set_column('A:O', 12)
for i in range(100):
    worksheet18.set_row(i, 15)

worksheet19.set_column('A:O', 12)
for i in range(100):
    worksheet17.set_row(i, 15)

worksheet20.set_column('A:O', 12)
for i in range(100):
    worksheet18.set_row(i, 15)


# 写入数据
insertData1(worksheet1, data1, data_format,data_format2)
insertData2(worksheet3, data3, data_format)
insertData2(worksheet4, data4, data_format)
insertData4(worksheet5,data5,data_format,data_format2)
insertData5(worksheet6,data6,data_format,data_format2)
insertData3(worksheet7, data7, data_format)
insertData3(worksheet8, data8, data_format)
insertData6(worksheet9, data9, data_format,data_format2)
insertData6(worksheet10, data10, data_format,data_format2)
insertData3(worksheet11, data11, data_format)
insertData3(worksheet12, data12, data_format)
insertData7(worksheet13, data13, data_format,data_format2)
insertData7(worksheet14, data14, data_format,data_format2)
insertData6(worksheet15, data15, data_format,data_format2)
insertData6(worksheet16, data16, data_format,data_format2)
insertData3(worksheet17, data17, data_format)
insertData3(worksheet18, data18, data_format)




'''图表部分'''
chart_line = workbook.add_chart({"type":"line"})

# chart_line.add_series({'categories': ['激活展示',0,0,0,5]})

chart_line.add_series({
    'name':'=6、激活展示!$B$1',
    'values': ['6、激活展示',1,1,len(data6),1],
})
chart_line.add_series({
    'name':'=6、激活展示!$C$1',
    'values': ['6、激活展示',1,2,len(data6),2]
})
chart_line.add_series({
    'name':'=6、激活展示!$D$1',
    'values': ['6、激活展示',1,3,len(data6),3]
})
chart_line.add_series({
    'name':'=6、激活展示!$E$1',
    'values': ['6、激活展示',1,4,len(data6),4]
})
chart_line.add_series({
    'name':'=6、激活展示!$F$1',
    'values': ['6、激活展示',1,5,len(data6),5]
})

chart_line.set_title({'name':'激活展示'})
chart_line.set_style(100)
chart_line.height=600
chart_line.width=960


worksheet6.insert_chart('G6', chart_line)


# 打完收工
workbook.close()
endtime = datetime.now()
print("耗时（秒）")
print((endtime - starttime).seconds)