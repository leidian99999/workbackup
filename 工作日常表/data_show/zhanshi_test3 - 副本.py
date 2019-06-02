import pandas as pd
import xlsxwriter
from def_zhanshi import clean271525, yangshi371525, insertData4,insertData5

date = '19/5/26'

inputPath = "D:/work/daily/"

data5 = pd.read_excel(inputPath + "A1_type_active_shengchan.xlsx",
                     skiprows=4,
                     header=None,
                     sheet_name="激活时效",
                     nrows=6)

data5 = data5.drop([0, 1], axis=1)

data6 = pd.read_excel(inputPath + "jihuozhanbi.xlsx")
data6 = data6.drop(columns=["总计"])
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
# data6["日期"] = pd.to_datetime(data6["日期"])


workbook = xlsxwriter.Workbook(inputPath + 'test02.xlsx')



date_format = workbook.add_format({"pattern": 1,
                                   "bg_color": '#B7CFE9',
                                   "align": 'center',
                                   "valign": 'vcenter',
                                   'bold': True,
                                   'border': 1,
                                   'num_format':'yy/mm/dd'
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
                                   'font_name': 'Microsoft YaHei'})
SUM_format2 = workbook.add_format({"align": 'center',
                                   "valign": 'vcenter',
                                   'border': 1,
                                   'font_name': 'Microsoft YaHei',
                                   'num_format': '0.00%'})

worksheet5 = workbook.add_worksheet("昨日激活时效")
worksheet6 = workbook.add_worksheet("激活展示")

worksheet5.set_column('A:C', 12)
for i in range(100):
    worksheet5.set_row(i, 15)
worksheet6.set_column('A:F', 16)
for i in range(100):
    worksheet6.set_row(i, 20)


headers2 = ["激活时效","激活数量","激活占比"]
headers3 = ['日期','4日激活占比','5-10日激活占比','11-15日激活占比','16-30日激活占比','30天以上激活占比']
worksheet5.merge_range('A1:C1', date + "签收时效合计", date_format)  # 合并单元格
worksheet5.write_row('A2', headers2, header_format2)
worksheet6.write_row('A1', headers3, header_format2)

insertData4(worksheet5,data5,data_format,data_format2)
insertData5(worksheet6,data6,data_format,data_format2)

chart_line = workbook.add_chart({"type":"line"})

chart_line.add_series({'categories': ['激活展示',0,0,0,5]})

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


workbook.close()
