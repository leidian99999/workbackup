import pandas as pd
import xlsxwriter
from def_zhanshi import clean271525,cleanquan ,yangshi371525, insertData1,insertData2,insertData3


date = '2019/5/26'

inputPath = "D:/work/daily/"

rows2 = 14

'''读取数据'''
# 数据集1
data3 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                      skiprows=41,
                      header=None,
                      sheet_name="生产流程分省情况",
                      nrows=31)

# 数据集2

data4 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                      skiprows=4,
                      header=None,
                      sheet_name="生产流程分产品情况",
                      nrows=rows2)


# 数据集3
data1 = pd.read_excel(inputPath + "A1_sign_active_1.xlsx",
                      skiprows=3,
                      header=0,
                      sheet_name="8日前签收时效合计",
                      nrows=100)
data1 = data1.drop(columns=["Unnamed: 0"], axis=1)
data1 = data1.fillna(method="ffill")
data1 = data1.iloc[:-2]
data1["发货占比"] = data1["发货占比"].apply(lambda x: format(x, '.2%'))
data1["3日签收率"] = data1["3日签收率"].apply(lambda x: format(x, '.2%'))
data1["7日签收率"] = data1["7日签收率"].apply(lambda x: format(x, '.2%'))
data1["激活率"] = data1["激活率"].apply(lambda x: format(x, '.2%'))
data1 = data1[data1["承运商"].str.contains("京东线下") == False]

# 数据集7
data7 = pd.read_excel(r'D:\work\daily\A1_type_active_quanliucheng_3day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程分省情况",
                      nrows=32)
# 数据集8

data8 = pd.read_excel(r'D:\work\daily\A1_type_active_quanliucheng_3day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程产品情况",
                      nrows=rows2)

'''数据清洗'''
data3 = cleanquan(data3)
data4 = cleanquan(data4)
data7 = clean271525(data7)
data8 = clean271525(data8)



# 设置输出sheet
workbook = xlsxwriter.Workbook(inputPath + 'test01.xlsx')
worksheet1 = workbook.add_worksheet("签收时效")
worksheet2 = workbook.add_worksheet("地址校验")
worksheet3 = workbook.add_worksheet("昨日省份激活率")
worksheet4 = workbook.add_worksheet("昨日产品激活率")
worksheet5 = workbook.add_worksheet("昨日激活时效")
worksheet6 = workbook.add_worksheet("激活展示")
worksheet7 = workbook.add_worksheet("3日省份激活率")
worksheet8 = workbook.add_worksheet("3日产品激活率")

# worksheet9 = workbook.add_worksheet("7日省份激活率")
# worksheet10 = workbook.add_worksheet("7日产品激活率")
# worksheet11 = workbook.add_worksheet("7日盲投省份情况")
# worksheet12 = workbook.add_worksheet("7日盲投产品情况")
# worksheet13 = workbook.add_worksheet("7日京东模式省份情况 ")
# worksheet14 = workbook.add_worksheet("7日京东模式产品情况 ")
# worksheet15 = workbook.add_worksheet("15日省份激活率")
# worksheet16 = workbook.add_worksheet("15日产品激活率")
# worksheet17 = workbook.add_worksheet("25日省份激活率")
# worksheet18 = workbook.add_worksheet("25日产品激活率")
# worksheet19 = workbook.add_worksheet("激活展示")
# worksheet20 = workbook.add_worksheet("京粉汇总")
# worksheet21 = workbook.add_worksheet("米粉汇总")
# worksheet22 = workbook.add_worksheet("激活总计情况")
# worksheet23 = workbook.add_worksheet("盲投不含转线上")
# worksheet24 = workbook.add_worksheet("京东线下转化率含转线上")
# worksheet25 = workbook.add_worksheet("昨日产品激活率")


headers1 = [
    '省份',
    "来单量",
    '拦截量',
    '卡单量',
    'v4待上传',
    '异常量',
    '发货量',
    '发货率',
    '激活量',
    '激活比例']



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
yangshi371525(
    worksheet7,
    '   3日分省',
    date,
    date_format,
    header_format2,
    header_format3,
    header_format4,
    header_format5)
yangshi371525(
    worksheet8,
    '   3日产品',
    date,
    date_format,
    header_format2,
    header_format3,
    header_format4,
    header_format5)

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

worksheet7.set_column('A:O', 12)
for i in range(100):
    worksheet7.set_row(i, 15)

worksheet8.set_column('A:O', 12)
for i in range(100):
    worksheet8.set_row(i, 15)



# 写入数据
insertData1(worksheet1, data1, data_format)
insertData2(worksheet3, data3, data_format)
insertData2(worksheet4, data4, data_format)
insertData3(worksheet7, data7, data_format)
insertData3(worksheet8, data8, data_format)


# 计算合计（昨日省份激活率）
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

# 计算合计（昨日产品激活率）
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



# 打完收工
workbook.close()
