# coding=utf-8

'''
# .set_bg_color('#ECDDD2') 1
# .set_bg_color('#8689A2') 2
# .set_bg_color('#FFFF00') 3
# .set_bg_color('#92D050') 4
# .set_bg_color('#C69A7D') 5
# .set_bg_color('#00B0F0') 6

# .set_num_format('0.00%') data2 SUM2
'''


# SUM_format2 = workbook.add_format({"align": 'center',
#                                    "valign": 'vcenter',
#                                    'border': 1,
#                                    'font_name': 'Microsoft YaHei',
#                                    'num_format': '0.00%'
#                                    })

# data_format2 = workbook.add_format({"pattern": 1,
#                                    "bg_color": '#cccccc',
#                                    "align": 'center',
#                                    "valign": 'vcenter',
#                                    'border': 1,
#                                    'font_name': 'Microsoft YaHei',
#                                     'num_format': '0.00%'})

# header_format1 = workbook.add_format({"pattern": 1,
#                                      "bg_color": '#ECDDD2',
#                                      "align": 'center',
#                                      "valign": 'vcenter',
#                                      'border': 1,
#                                      })
# header_format2 = workbook.add_format({"pattern": 1,
#                                       "bg_color": '#8689A2',
#                                       "align": 'center',
#                                       "valign": 'vcenter',
#                                       'border': 1,
#                                       'bold': True,
#                                       "font_size": 10})
# header_format3 = workbook.add_format({"pattern": 1,
#                                       "bg_color": '#FFFF00',
#                                       "align": 'center',
#                                       "valign": 'vcenter',
#                                       'border': 1,
#                                       'bold': True,
#                                       'font_size': 10})
# header_format4 = workbook.add_format({"pattern": 1,
#                                       "bg_color": '#92D050',
#                                       "align": 'center',
#                                       "valign": 'vcenter',
#                                       'border': 1,
#                                       'bold': True,
#                                       'font_size': 10})
# header_format5 = workbook.add_format({"pattern": 1,
#                                       "bg_color": '#C69A7D',
#                                       "align": 'center',
#                                       "valign": 'vcenter',
#                                       'border': 1,
#                                       'bold': True,
#                                       'font_size': 10})
# header_format6 = workbook.add_format({"pattern": 1,
#                                       "bg_color": '#00B0F0',
#                                       "align": 'center',
#                                       "valign": 'vcenter',
#                                       'border': 1,
#                                       'bold': True,
#                                       'font_size': 10})


'''计算部分'''

# 计算合计（sheet3）
# worksheet3.write("A34", '合计', SUM_format1)
# SUM_list = ["B", 'C', 'D', 'E', 'F', 'G', 'I']
# for w in SUM_list:
#     worksheet3.write_formula(
#         w + "34",
#         '=SUM(' + w + '3:' + w + '33)',
#         SUM_format1)
#     # print('=SUM(' + w + '3:' + w + '33)')
# worksheet3.write_formula("H34", '=G34/B34', SUM_format2)
# worksheet3.write_formula("J34", '=I34/G34', SUM_format2)

# 计算合计（sheet4）
# worksheet4.write("A" + str(int(rows1) + 3), '合计', SUM_format1)
# SUM_list = ["B", 'C', 'D', 'E', 'F', 'G', 'I']
# for w in SUM_list:
#     worksheet4.write_formula(w + str(int(rows1) + 3),
#                              '=SUM(' + w + '3:' + w +
#                              str(int(rows1) + 2) + ')',
#                              SUM_format1)
#     # print('=SUM(' + w + '3:' + w + str(int(rows2) + 2) + ')')
# worksheet4.write_formula("H" + str(int(rows1) + 3),
#                          "=G" + str(int(rows1) + 3) + "/" +
#                          "B" + str(int(rows1) + 3),
#                          SUM_format2)
# worksheet4.write_formula("J" + str(int(rows1) + 3),
#                          "=I" + str(int(rows1) + 3) + "/" +
#                          "G" + str(int(rows1) + 3),
#                          SUM_format2)