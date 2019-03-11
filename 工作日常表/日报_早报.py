import numpy as np
import pandas as pd
import datetime
import time

date = "1201"

# 导数
data = pd.read_excel(r"G:\work\日报\早报\早午晚报数据\早午晚原数据\\"+date+"早-互联网联名卡查询列表.xlsx")
qudao = pd.read_excel("G:/work/日报/功能列表/集中和分省渠道号.xlsx",sheet_name='Sheet2')
writer = "G:\\work\\日报\\早报\\输出\\早报\\"+date+"早待生产.xlsx"


print("数据集共{}行，{}列".format(data.shape[0],data.shape[1]))

print('写卡表共{}行，{}列'.format(qudao.shape[0],qudao.shape[1]))



#匹配渠道号简称
data =pd.merge(data,qudao,how='left',on='写卡渠道号')
# a = data.merge(qudao[['省份','写卡渠道号']],how='left',on='写卡渠道号')
print("匹配后，行列数:%s行，%s列" % (data.shape[0],data.shape[1]))

#去除‘收货地址’列中含有‘测试’的行
data = data[~data['收货人地址'].str.contains('测试')]
print("'收货人地址'去除'测试'后:%s行，%s列" % (data.shape[0],data.shape[1]))

# a = data['订单状态'].groupby(data['省份','写卡渠道号']).count()
# print(a)

# b = data.groupby(['省份','写卡渠道号'])[['订单状态']].count().reset_index()

b = data.groupby(["省份","订单状态","写卡渠道号"],sort=True)[["销售品名称"]].count().reset_index()

b = b.sort_values(axis=0,ascending=True,by="订单状态")
# b['合计'] = b['订单状态']
# b = b.sort_values(by='合计',ascending=False)
b.to_excel(writer, index=False)
