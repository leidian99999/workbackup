import xlsxwriter
import pandas as pd
import numpy as np


import sys
print(sys.executable)

'''
数据清洗
'''
def clean271525(data):
    data = data.iloc[:, 1:]
    data[4] = data[4].apply(lambda x: format(x, '.2%'))
    data[6] = data[6].apply(lambda x: format(x, '.2%'))
    data[8] = data[8].apply(lambda x: format(x, '.2%'))
    data[10] = data[10].apply(lambda x: format(x, '.2%'))
    data[12] = data[12].apply(lambda x: format(x, '.2%'))
    data[14] = data[14].apply(lambda x: format(x, '.2%'))
    data[15] = data[15].apply(lambda x: format(x, '.2%'))
    return data

def cleanquan(data):
    data = data.drop([0, 9], axis=1)
    data[8] = data[8].apply(lambda x: format(x, '.2%'))
    data[11] = data[11].apply(lambda x: format(x, '.2%'))
    return data


'''
表标题
'''
def style371525(worksheet,col1, title,date,date_format,header_format2,header_format3,header_format4,header_format5):
    worksheet.merge_range('A1:O1', date + title, date_format)
    worksheet.merge_range('A2:A3', col1, header_format2)
    worksheet.merge_range('B2:B3', "订单总数S", header_format2)

    worksheet.merge_range('C2:C3', "生产发货A", header_format3)
    worksheet.write('D2', "发货率a", header_format3)
    worksheet.write('D3', "a=A/S*100%", header_format3)
    worksheet.write('E2', "异常筛查T", header_format3)
    worksheet.write('E3', "T=S-A", header_format3)
    worksheet.write('F2', "异常筛查率t", header_format3)
    worksheet.write('F3', "t=T/S*100", header_format3)

    worksheet.merge_range('G2:G3', "签收C", header_format4)
    worksheet.write('H2', "签收率c", header_format4)
    worksheet.write('H3', "a=A/S*100%", header_format4)
    worksheet.write('I2', "未签收R", header_format4)
    worksheet.write('I3', "R=A-C", header_format4)
    worksheet.write('J2', "未签收率r", header_format4)
    worksheet.write('J3', "r=R/A*100%", header_format4)

    worksheet.merge_range('K2:K3', "激活B", header_format5)
    worksheet.write('L2', "签收激活率b", header_format5)
    worksheet.write('L3', "b=B/C*100", header_format5)
    worksheet.write('M2', "未激活X", header_format5)
    worksheet.write('M3', "X=C-B", header_format5)
    worksheet.write('N2', "签收未激活率x", header_format5)
    worksheet.write('N3', "x=X/C*100%", header_format5)

    worksheet.write('O2', "发货激活率KPI", header_format2)
    worksheet.write('O3', "KPI=B/A*100%", header_format2)

def style37JD(worksheet, col1,title,date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6):
    worksheet.merge_range('A1:R1', date + title, date_format)
    worksheet.merge_range('A2:A3', col1, header_format2)
    worksheet.merge_range('B2:B3', "派单总数S", header_format2)
    worksheet.merge_range('C2:C3', col1+"派单量占比", header_format2)

    worksheet.merge_range('D2:D3', "派卡A", header_format3)
    worksheet.write('E2', "派卡率a", header_format3)
    worksheet.write('E3', "a=A/S*100%", header_format3)
    worksheet.write('F2', "异常筛查T", header_format3)
    worksheet.write('F3', "T=S-A", header_format3)
    worksheet.write('G2', "异常筛查率t", header_format3)
    worksheet.write('G3', "t=T/S*100", header_format3)

    worksheet.merge_range('H2:H3', "上门C", header_format4)
    worksheet.write('I2', "上门率c", header_format4)
    worksheet.write('I3', "c=C/A*100", header_format4)
    worksheet.write('J2', "未上门R", header_format4)
    worksheet.write('J3', "R=A-C", header_format4)
    worksheet.write('K2', "未上门率r", header_format4)
    worksheet.write('K3', "r=R/A*100%", header_format4)

    worksheet.merge_range('L2:L3', "激活B", header_format5)
    worksheet.merge_range('M2:M3', col1+"激活量占比", header_format5)
    worksheet.write('N2', "激活率KPI", header_format5)
    worksheet.write('N3', "KPI=B/A*100%", header_format5)

    worksheet.merge_range('O2:O3', "面对面首充D", header_format6)
    worksheet.merge_range('P2:P3', "面对面省份首充量占比", header_format6)
    worksheet.write('Q2', "面对面首充率d", header_format6)
    worksheet.write('Q3', "d=D/A*100", header_format6)
    worksheet.merge_range('R2:R3', "全量首充D", header_format6)

def style37Mang(worksheet, col1,title,date,date_format,header_format2,header_format3,header_format4,header_format5,header_format6):
    worksheet.merge_range('A1:R1', date + title, date_format)
    worksheet.merge_range('A2:A3', col1, header_format2)
    worksheet.merge_range('B2:B3', "订单总数S", header_format2)
    worksheet.merge_range('C2:C3', col1+"订单量占比", header_format2)

    worksheet.merge_range('D2:D3', "生产发货A", header_format3)
    worksheet.write('E2', "发货率a", header_format3)
    worksheet.write('E3', "a=A/S*100%", header_format3)
    worksheet.write('F2', "异常筛查T", header_format3)
    worksheet.write('F3', "T=S-A", header_format3)
    worksheet.write('G2', "异常筛查率t", header_format3)
    worksheet.write('G3', "t=T/S*100", header_format3)

    worksheet.merge_range('H2:H3', "签收C", header_format4)
    worksheet.write('I2', "签收率c", header_format4)
    worksheet.write('I3', "c=C/A*100", header_format4)
    worksheet.write('J2', "未签收R", header_format4)
    worksheet.write('J3', "R=A-C", header_format4)
    worksheet.write('K2', "未签收率r", header_format4)
    worksheet.write('K3', "r=R/A*100%", header_format4)

    worksheet.merge_range('L2:L3', "激活B", header_format5)
    worksheet.merge_range('M2:M3', col1+"激活量占比", header_format5)
    worksheet.write('N2', "签收激活率b", header_format5)
    worksheet.write('N3', "b=B/C*100", header_format5)
    worksheet.write('O2', "未激活X", header_format5)
    worksheet.write('O3', "X=C-B", header_format5)
    worksheet.write('P2', "签收未激活率x", header_format5)
    worksheet.write('P3', "x=X/C*100%", header_format5)

    worksheet.write('Q2', "发货激活率KPI", header_format2)
    worksheet.write('Q3', "KPI=B/A*100%", header_format2)

    worksheet.merge_range('R2:R3', "盲投首充D", header_format6)
    worksheet.merge_range('S2:S3', "盲投"+col1+"首充量占比", header_format6)
    worksheet.write('T2', "盲投首充率d", header_format6)
    worksheet.write('T3', "d=D/A*100", header_format6)
    worksheet.merge_range('U2:U3', "全量首充D", header_format6)


'''
写入数据
'''
def insertData1(worksheet, df,data_format,data_format2):
    '''
    1、签收时效
    :param worksheet:
    :param df:
    :param data_format:
    :param data_format2:
    :return:
    '''
    row1 = 1
    col1 = 0
    for xieka, sheng, kuaidi, fahuo, sanri, qiri, jihuol, jihuoqianshoul in df.values:
        worksheet.write(row1, col1 + 0, xieka, data_format)
        worksheet.write(row1, col1 + 1, sheng, data_format)
        worksheet.write(row1, col1 + 2, kuaidi, data_format)
        worksheet.write(row1, col1 + 3, fahuo, data_format)
        worksheet.write(row1, col1 + 4, sanri, data_format2)
        worksheet.write(row1, col1 + 5, qiri, data_format2)
        worksheet.write(row1, col1 + 6, jihuol, data_format2)
        worksheet.write(row1, col1 + 7, jihuoqianshoul, data_format2)
        row1 += 1

def insertData2(worksheet, df,data_format):
    '''
    昨日省、产品
    :param worksheet:
    :param df:
    :param data_format:
    :return:
    '''
    row1 = 2
    col1 = 0
    for sheng, laidan, lanjie, kadan, v4shang, yichang, fahuo, fahuol, jihuo, jihuob in df.values:
        worksheet.write(row1, col1 + 0, sheng, data_format)
        worksheet.write(row1, col1 + 1, laidan, data_format)
        worksheet.write(row1, col1 + 2, lanjie, data_format)
        worksheet.write(row1, col1 + 3, kadan, data_format)
        worksheet.write(row1, col1 + 4, v4shang, data_format)
        worksheet.write(row1, col1 + 5, yichang, data_format)
        worksheet.write(row1, col1 + 6, fahuo, data_format)
        worksheet.write(row1, col1 + 7, fahuol, data_format)
        worksheet.write(row1, col1 + 8, jihuo, data_format)
        worksheet.write(row1, col1 + 9, jihuob, data_format)
        row1 += 1



def insertData3(worksheet, df,data_format,data_format2):
    '''
    3,7,15，25省产品
    :param worksheet:
    :param df:
    :param data_format:
    :return:
    '''
    row1 = 3
    col1 = 0
    for sheng, LD, FH, FHL, YCH, YCHL, QSH, QSHL, WQSH, WQSHL, JH, QSHJHL, WJH, QSHWJHL, FHJHL in df.values:
        worksheet.write(row1, col1 + 0, sheng, data_format)
        worksheet.write(row1, col1 + 1, LD, data_format)
        worksheet.write(row1, col1 + 2, FH, data_format)
        worksheet.write(row1, col1 + 3, FHL, data_format2)
        worksheet.write(row1, col1 + 4, YCH, data_format)
        worksheet.write(row1, col1 + 5, YCHL, data_format2)
        worksheet.write(row1, col1 + 6, QSH, data_format)
        worksheet.write(row1, col1 + 7, QSHL, data_format2)
        worksheet.write(row1, col1 + 8, WQSH, data_format)
        worksheet.write(row1, col1 + 9, WQSHL, data_format2)
        worksheet.write(row1, col1 + 10, JH, data_format)
        worksheet.write(row1, col1 + 11, QSHJHL, data_format2)
        worksheet.write(row1, col1 + 12, WJH, data_format)
        worksheet.write(row1, col1 + 13, QSHWJHL, data_format2)
        worksheet.write(row1, col1 + 14, FHJHL, data_format2)
        row1 += 1

def insertData4(worksheet,df,data_format,data_format2):
    '''
    5、激活时效
    :param worksheet:
    :param df:
    :param data_format:
    :param data_format2:
    :return:
    '''
    row1 = 1
    col1 = 0
    for JHSX,JHSL,JHZHB in df.values:
        worksheet.write(row1, col1 + 0, JHSX, data_format)
        worksheet.write(row1, col1 + 1, JHSL, data_format)
        worksheet.write(row1, col1 + 2, JHZHB, data_format2)
        row1 += 1

def insertData5(worksheet,df,date_format,data_format2):
    '''

    :param worksheet:
    :param df:
    :param date_format:
    :param data_format2:
    :return:
    '''
    row1 = 1
    col1 = 0
    for date,A_ZHB,B_ZHB,C_ZHB,D_ZHB,E_ZHB in df.values:
        worksheet.write(row1, col1 + 0, date, date_format)
        worksheet.write(row1, col1 + 1, A_ZHB, data_format2)
        worksheet.write(row1, col1 + 2, B_ZHB, data_format2)
        worksheet.write(row1, col1 + 3, C_ZHB, data_format2)
        worksheet.write(row1, col1 + 4, D_ZHB, data_format2)
        worksheet.write(row1, col1 + 5, E_ZHB, data_format2)
        row1 += 1

def insertData6(worksheet, df,data_format,data_format2):
    '''
    京东模式3&7日
    :param worksheet:
    :param df:
    :param data_format:
    :param data_format2:
    :return:
    '''
    row1 = 3
    col1 = 0
    for sheng, PD, PDB, PK, PKL, YCH, YCHL, SHM, SHML, WSHM, WSHML, JH, JHB, JHL, SHCH,SHCHB,SHCHL,QSHCH in df.values:
        worksheet.write(row1, col1 + 0, sheng, data_format)
        worksheet.write(row1, col1 + 1, PD, data_format)
        worksheet.write(row1, col1 + 2, PDB, data_format2)
        worksheet.write(row1, col1 + 3, PK, data_format)
        worksheet.write(row1, col1 + 4, PKL, data_format2)
        worksheet.write(row1, col1 + 5, YCH, data_format)
        worksheet.write(row1, col1 + 6, YCHL, data_format2)
        worksheet.write(row1, col1 + 7, SHM, data_format)
        worksheet.write(row1, col1 + 8, SHML, data_format2)
        worksheet.write(row1, col1 + 9, WSHM, data_format)
        worksheet.write(row1, col1 + 10, WSHML, data_format2)
        worksheet.write(row1, col1 + 11, JH, data_format)
        worksheet.write(row1, col1 + 12, JHB, data_format2)
        worksheet.write(row1, col1 + 13, JHL, data_format2)
        worksheet.write(row1, col1 + 14, SHCH, data_format)
        worksheet.write(row1, col1 + 15, SHCHB, data_format2)
        worksheet.write(row1, col1 + 16, SHCHL, data_format2)
        worksheet.write(row1, col1 + 17, QSHCH, data_format)
        row1 += 1

def insertData7(worksheet, df,data_format,data_format2):
    '''
    盲投7日
    :param worksheet:
    :param df:
    :param data_format:
    :param data_format2:
    :return:
    '''
    row1 = 3
    col1 = 0
    for sheng, LD, LDB, FH, FHL, YCSHCH, YCSHCHL, QSH, QSHL, WQSH, WQSHL,JH , JHB, JHL,WJH,WJHL,FHJH, SHCH,SHCHB,SHCHL,QSHCH in df.values:
        worksheet.write(row1, col1 + 0, sheng, data_format)
        worksheet.write(row1, col1 + 1, LD, data_format)
        worksheet.write(row1, col1 + 2, LDB, data_format2)
        worksheet.write(row1, col1 + 3, FH, data_format)
        worksheet.write(row1, col1 + 4, FHL, data_format2)
        worksheet.write(row1, col1 + 5, YCSHCH, data_format)
        worksheet.write(row1, col1 + 6, YCSHCHL, data_format2)
        worksheet.write(row1, col1 + 7, QSH, data_format)
        worksheet.write(row1, col1 + 8, QSHL, data_format2)
        worksheet.write(row1, col1 + 9, WQSH, data_format)
        worksheet.write(row1, col1 + 10, WQSHL, data_format2)
        worksheet.write(row1, col1 + 11, JH, data_format)
        worksheet.write(row1, col1 + 12, JHB, data_format2)
        worksheet.write(row1, col1 + 13, JHL, data_format2)
        worksheet.write(row1, col1 + 14, WJH, data_format)
        worksheet.write(row1, col1 + 15, WJHL, data_format2)
        worksheet.write(row1, col1 + 16, FHJH, data_format)
        worksheet.write(row1, col1 + 17, SHCH, data_format)
        worksheet.write(row1, col1 + 18, SHCHB, data_format2)
        worksheet.write(row1, col1 + 19, SHCHL, data_format2)
        worksheet.write(row1, col1 + 20, QSHCH, data_format)
        row1 += 1