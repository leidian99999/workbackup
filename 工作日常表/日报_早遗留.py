import pandas as pd


fold = "181201"
today = "2018-12-01"
yestoday = "2018-11-30"
disk = "G"


# 导数
data = pd.read_excel(disk + r":\work\日报\早报\早午晚报数据\早午晚原数据\\"+fold+"早-互联网联名卡查询列表.xlsx")
qudao = pd.read_excel(disk + ":/work/日报/功能列表/集中和分省渠道号.xlsx",sheet_name='Sheet2')
writer = disk + ":\\work\\日报\\早报\\输出\\早报\\"+fold+"早遗留.xlsx"

#匹配渠道号简称
data =pd.merge(data,qudao,how='left',on='写卡渠道号')
# a = data.merge(qudao[['省份','写卡渠道号']],how='left',on='写卡渠道号')
print("匹配后，行列数:%s行，%s列" % (data.shape[0],data.shape[1]))

#去除‘收货地址’列中含有‘测试’的行
data = data[data['收货人地址'].str.contains('测试') == False]
print("'收货人地址'去除'测试'后:%s行，%s列" % (data.shape[0],data.shape[1]))
data1 = data[data['收货人地址'].str.contains('测试')]
print("打印含“测试”行{}".format(data1[["订单编号","收货人地址",'写卡渠道号']]))


# 筛选时间
data["订单生成时间"] = pd.to_datetime(data["订单生成时间"])
data["小时"] = data["订单生成时间"].dt.hour
data["日期"] = data["订单生成时间"].dt.date

data["日期"] = data["日期"].map(lambda x : str(x))
data = data[data["日期"].str.contains(today) == False]
df1 = data[(data["日期"] == yestoday) & (data["小时"] >= 16)]
data = data.drop(df1.index)

b = data.groupby(["省份","订单状态","写卡渠道号"],sort=True)[["销售品名称"]].count().reset_index()

b = b.sort_values(axis=0,ascending=True,by="订单状态")
# b['合计'] = b['订单状态']
# b = b.sort_values(by='合计',ascending=False)
b.to_excel(writer, index=False)