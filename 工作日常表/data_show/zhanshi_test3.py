import xlsxwriter
import pandas as pd
from def_zhanshi import clean271525, yangshi371525, insertData3

date = '2019/5/26'

data7 = pd.read_excel(r'D:\work\daily\A1_type_active_quanliucheng_3day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程分省情况",
                      nrows=32)

rows2 = 14
data8 = pd.read_excel(r'D:\work\daily\A1_type_active_quanliucheng_3day.xlsx',
                      skiprows=3,
                      header=None,
                      sheet_name="全流程产品情况",
                      nrows=rows2)

data7 = clean271525(data7)
data8 = clean271525(data8)
workbook = xlsxwriter.Workbook(r'D:\work\daily\test05.xlsx')
worksheet7 = workbook.add_worksheet("3日省份激活率")
worksheet8 = workbook.add_worksheet("3日产品激活率")

worksheet7.set_column('A:O', 12)
for i in range(100):
    worksheet7.set_row(i, 15)
worksheet8.set_column('A:O', 12)
for i in range(100):
    worksheet8.set_row(i, 15)

date_format = workbook.add_format({"pattern": 1,
                                   "bg_color": '#B7CFE9',
                                   "align": 'center',
                                   "valign": 'vcenter',
                                   'bold': True,
                                   'border': 1,
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
                                   'font_name': 'Microsoft YaHei'})
SUM_format1 = workbook.add_format({"align": 'center',
                                   "valign": 'vcenter',
                                   'border': 1,
                                   'font_name': 'Microsoft YaHei'})
SUM_format2 = workbook.add_format({"align": 'center',
                                   "valign": 'vcenter',
                                   'border': 1,
                                   'font_name': 'Microsoft YaHei',
                                   'num_format': '0.00%'})


yangshi371525(
    worksheet7,
    '   3日分省',
    date,
    date_format,
    header_format2,
    header_format3,
    header_format4,
    header_format5)
insertData3(worksheet7, data7, data_format)
yangshi371525(
    worksheet8,
    '   3日产品',
    date,
    date_format,
    header_format2,
    header_format3,
    header_format4,
    header_format5)
insertData3(worksheet8, data8, data_format)


workbook.close()
