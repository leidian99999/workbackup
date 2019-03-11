import numpy as np
import pandas as pd
# from pandas import Series,DataFrame
import re
import datetime
import time
import xlsxwriter
import zipfile,os

starttime = datetime.datetime.now()

#修改区域
fold = "190213"
yesterday = "2019-02-12"
#修改区域

data   = pd.read_excel('G:/work/日报/促上传/' + fold + '/' + fold + '促上传导出上午.xlsx')  #改路径
writer = "G:/work/日报/促上传/" + fold + "/输出/"
biaoka = pd.read_excel("G:/work/日报/功能列表/产品标卡.xlsx")
fankui = pd.read_excel("G:/work/日报/功能列表/促上传反馈字段.xlsx")
get_files_path = "G:\\work\\日报\\促上传\\" + fold + "\\输出"  # 需要压缩的文件夹
set_files_path = "G:\\work\\日报\\促上传\\"+fold+"\\"+fold+"促上传分省.zip"  # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样)
HXZ =  'G:/work/日报/促上传/'+fold+'/'


#去除‘收货地址’列中含有‘测试’的行
data = data[data['收货地址'].str.contains('测试') == False]
print("'收货地址'去除'测试'后:%s行，%s列" % (data.shape[0],data.shape[1]))

# 去除多余表头
data = data[data['收货地址'].str.contains("收货地址") == False]

#订单生成时间分列
split = pd.DataFrame((x.split(' ') for x in data['订单生成时间']), index=data.index, columns=['订单生成日期','订单时间'])
data = pd.merge(data,split,left_index=True,right_index=True)

#号码归属地分列
split1 = pd.DataFrame((x.split('/') for x in data['号码归属地']), index=data.index, columns=['所属省','地区'])
data = pd.merge(data,split1,left_index=True,right_index=True)
print("'分裂后'行列数:%s行，%s列" % (data.shape[0],data.shape[1]))
print('*'*100)
#vlookup产品标卡
data =pd.merge(data,biaoka,how='left',on='销售品编号')
print("匹配标卡后，行列数:%s行，%s列" % (data.shape[0],data.shape[1]))
print('*'*100)
# #筛选"订单生成日期"中指定日期
data = data.loc[data["订单生成日期"] == yesterday] #改前一日期
print("筛选'订单生成日期'中指定日期后，行列数:%s行，%s列" % (data.shape[0],data.shape[1]))


#检查分类列中有无空值并打印
data1 = data[data['分类'].isnull()]
print('*'*100)
print(data1.columns)
print("打印为空行{}".format(data1[["销售品名称_x","销售品编号"]]))


#分省前导出备份
outer1 = HXZ + str(time.strftime("%Y-%m-%d", time.localtime())) + "促上传上午(含新装).xlsx"
data.to_excel(outer1,index=False)
print("含新装共{}行，{}列".format(data.shape[0],data.shape[1]))

#"分类"中去除"新装",同时也去掉空白行
data = data[data['分类'].notnull()]
data = data[~data['分类'].str.contains('新装')]
print("'分类'中去除'新装'后，行列数:%s行，%s列" % (data.shape[0],data.shape[1]))

#合并反馈表
data = pd.merge(fankui,data,right_index=True,left_index=True,how='outer')
print("合并反馈表后:%s行，%s列" % (data.shape[0],data.shape[1]))

#分省前导出备份，改路径
outer2 = HXZ + str(time.strftime("%Y-%m-%d", time.localtime())) + "促上传待分省(不含新装).xlsx"
data.to_excel(outer2,index=False)

#开始分省

print(data['所属省'].value_counts())


sheng_list = data['所属省'].unique()

for sheng in sheng_list:
    child_wb = data[data['所属省'] == sheng]
    child_wb.to_excel(writer + str(time.strftime("%Y-%m-%d", time.localtime())) +  sheng + '上传.xlsx', index=False)

print('拆分完成！')

#打包起来
def compress(get_files_path, set_files_path):
    f = zipfile.ZipFile(set_files_path , 'w', zipfile.ZIP_DEFLATED )
    for dirpath, dirnames, filenames in os.walk( get_files_path ):
        fpath = dirpath.replace(get_files_path,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            f.write(os.path.join(dirpath,filename), fpath+filename)
    f.close()
    print("打完收工")

print('打包起来~')
compress(get_files_path, set_files_path)
endtime = datetime.datetime.now()
print("耗时（秒）")
print((endtime - starttime).seconds)


