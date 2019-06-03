import pandas as pd
import xlsxwriter
from def_zhanshi import *


date = '19/5/26'
filename = 'testc.xlsx'
inputPath = "F:/temp/190529/"

rows2 = 14




'''读取数据'''
# 数据集1
data1 = pd.read_excel(inputPath + "A1_sign_active_1.xlsx",
                      skiprows=3,
                      header=0,
                      sheet_name="8日前签收时效合计",
                      nrows=100)
data1 = data1.drop(columns=["Unnamed: 0"], axis=1)
data1 = data1.fillna(method="ffill")
data1 = data1.iloc[:-2]
# data1["发货占比"] = data1["发货占比"].apply(lambda x: format(x, '.2%'))
# data1["3日签收率"] = data1["3日签收率"].apply(lambda x: format(x, '.2%'))
# data1["7日签收率"] = data1["7日签收率"].apply(lambda x: format(x, '.2%'))
# data1["激活率"] = data1["激活率"].apply(lambda x: format(x, '.2%'))
data1 = data1[data1["承运商"].str.contains("京东线下") == False]

# 数据集2




# 数据集3
data3 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                      skiprows=41,
                      header=None,
                      sheet_name="生产流程分省情况",
                      nrows=31)

# 数据集4
data4 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                      skiprows=4,
                      header=None,
                      sheet_name="生产流程分产品情况",
                      nrows=rows2)

# 数据集5
data5 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                     skiprows=4,
                     header=None,
                     sheet_name="激活时效",
                     nrows=6)

data5 = data5.drop([0, 1], axis=1)

# 数据集6
data6 = pd.read_excel(inputPath + "jihuozhanbi.xlsx")
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
data6=data6.append(new,ignore_index=True)


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
                      nrows=rows2)

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
                      nrows=rows2)

# 数据集17
data17 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng_15day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程分省情况",
                      nrows=32)

# 数据集18
data18 = pd.read_excel(inputPath + 'A1_type_active_quanliucheng_3day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程产品情况",
                      nrows=rows2)



'''数据清洗'''
data3 = cleanquan(data3)
data4 = cleanquan(data4)
data7 = clean271525(data7)
data8 = clean271525(data8)
data11 = clean271525(data11)
data12 = clean271525(data12)
data17 = clean271525(data17)
data18 = clean271525(data18)





# 设置输出sheet
workbook = xlsxwriter.Workbook(inputPath + filename)
worksheet1 = workbook.add_worksheet("签收时效")
worksheet2 = workbook.add_worksheet("地址校验")
worksheet3 = workbook.add_worksheet("昨日省份激活率")
worksheet4 = workbook.add_worksheet("昨日产品激活率")
worksheet5 = workbook.add_worksheet("昨日激活时效")
worksheet6 = workbook.add_worksheet("激活展示")
worksheet7 = workbook.add_worksheet("3日省份激活率")
worksheet8 = workbook.add_worksheet("3日产品激活率")

# worksheet9 = workbook.add_worksheet("3日京东模式省份情况")
# worksheet10 = workbook.add_worksheet("3日京东模式产品情况")
worksheet11 = workbook.add_worksheet("7日省份激活率")
worksheet12 = workbook.add_worksheet("7日产品激活率")
# worksheet13 = workbook.add_worksheet("7日盲投省份情况 ")
# worksheet14 = workbook.add_worksheet("7日盲投产品情况 ")
# worksheet15 = workbook.add_worksheet("7日京东模式省份情况 ")
# worksheet16 = workbook.add_worksheet("7日京东模式产品情况 ")
worksheet17 = workbook.add_worksheet("15日省份激活率")
worksheet18 = workbook.add_worksheet("15日产品激活率")
# worksheet19 = workbook.add_worksheet("25日省份激活率")
# worksheet20 = workbook.add_worksheet("25日产品激活率")
# worksheet21 = workbook.add_worksheet("京粉汇总")
# worksheet22 = workbook.add_worksheet("米粉汇总")
# worksheet23 = workbook.add_worksheet("激活总计情况")
# worksheet24 = workbook.add_worksheet("盲投不含转线上")
# worksheet25 = workbook.add_worksheet("京东线下转化率含转线上")


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
header_format = workbook.add_format({"pattern": 1,
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
worksheet3.merge_range('A1:J1', date, date_format)  # 合并单元格
worksheet3.write_row('A2', headers1, header_format)
worksheet4.merge_range('A1:J1', date, date_format)  # 合并单元格
worksheet4.write_row('A2', headers1, header_format)
worksheet5.merge_range('A1:C1', date + "签收时效合计", date_format)  # 合并单元格
worksheet5.write_row('A2', headers2, header_format2)
worksheet6.write_row('A1', headers3, header_format2)
yangshi371525(worksheet7,'   3日分省',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet8,'   3日产品',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet11,'   7日分省',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet12,'   7日产品',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet17,'   15日分省',date,date_format,header_format2,header_format3,header_format4,header_format5)
yangshi371525(worksheet18,'   15日产品',date,date_format,header_format2,header_format3,header_format4,header_format5)


# 设定行格式
worksheet1.set_column('A:H', 10)
for i in range(100):
    worksheet3.set_row(i, 20)

worksheet3.set_column('A:J', 10)
for i in range(24):
    worksheet3.set_row(i, 20)

worksheet4.set_column('A:J', 10)
for i in range(rows2):
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

worksheet11.set_column('A:O', 12)
for i in range(100):
    worksheet11.set_row(i, 15)

worksheet12.set_column('A:O', 12)
for i in range(100):
    worksheet12.set_row(i, 15)

worksheet17.set_column('A:O', 12)
for i in range(100):
    worksheet17.set_row(i, 15)

worksheet18.set_column('A:O', 12)
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
insertData3(worksheet11, data11, data_format)
insertData3(worksheet12, data12, data_format)
insertData3(worksheet17, data17, data_format)
insertData3(worksheet18, data18, data_format)



'''计算部分'''

# 计算合计（sheet3）
worksheet3.write("A34", '合计', SUM_format1)
SUM_list = ["B", 'C', 'D', 'E', 'F', 'G', 'I']
for w in SUM_list:
    worksheet3.write_formula(
        w + "34",
        '=SUM(' + w + '3:' + w + '33)',
        SUM_format1)
    # print('=SUM(' + w + '3:' + w + '33)')
worksheet3.write_formula("H34", '=G34/B34', SUM_format2)
worksheet3.write_formula("J34", '=I34/G34', SUM_format2)

# 计算合计（sheet4）
worksheet4.write("A" + str(int(rows2) + 3), '合计', SUM_format1)
SUM_list = ["B", 'C', 'D', 'E', 'F', 'G', 'I']
for w in SUM_list:
    worksheet4.write_formula(w + str(int(rows2) + 3),
                             '=SUM(' + w + '3:' + w +
                             str(int(rows2) + 2) + ')',
                             SUM_format1)
    # print('=SUM(' + w + '3:' + w + str(int(rows2) + 2) + ')')
worksheet4.write_formula("H" + str(int(rows2) + 3),
                         "=G" + str(int(rows2) + 3) + "/" +
                         "B" + str(int(rows2) + 3),
                         SUM_format2)
worksheet4.write_formula("J" + str(int(rows2) + 3),
                         "=I" + str(int(rows2) + 3) + "/" +
                         "G" + str(int(rows2) + 3),
                         SUM_format2)

'''图表部分'''
chart_line = workbook.add_chart({"type":"line"})

# chart_line.add_series({'categories': ['激活展示',0,0,0,5]})

chart_line.add_series({
    'name':'=激活展示!$B$1',
    'values': ['激活展示',1,1,len(data6),1],
})
chart_line.add_series({
    'name':'=激活展示!$C$1',
    'values': ['激活展示',1,2,len(data6),2]
})
chart_line.add_series({
    'name':'=激活展示!$D$1',
    'values': ['激活展示',1,3,len(data6),3]
})
chart_line.add_series({
    'name':'=激活展示!$E$1',
    'values': ['激活展示',1,4,len(data6),4]
})
chart_line.add_series({
    'name':'=激活展示!$F$1',
    'values': ['激活展示',1,5,len(data6),5]
})

chart_line.set_title({'name':'激活展示'})
chart_line.set_style(100)
chart_line.height=600
chart_line.width=960


worksheet6.insert_chart('G6', chart_line)


# 打完收工
workbook.close()
