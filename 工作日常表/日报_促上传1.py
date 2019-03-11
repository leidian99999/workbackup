import pandas as pd
import datetime
import time

fold = "181211"
noon = '上午'


data = pd.read_excel("G:/work/日报/促上传\\"+fold+"\\"+fold+"促上传导出" + noon + ".xlsx")
biaoka = pd.read_excel("G:/work/日报/功能列表/产品标卡.xlsx")
outpath = 'G:/work/日报/促上传/'+ fold +'/'+ noon +'/'
# today = datetime.datetime(2018,10,31)

print("读取数据行列数：{}行，{}列。".format(data.shape[0],data.shape[1]))
print("*"*100)

data = data.set_index(['订单生成时间'],drop=False)
print("更改索引：{}行，{}列。".format(data.shape[0],data.shape[1]))
print("*"*100)

#去除‘收货地址’列中含有‘测试’的行
data2 = data[data['收货地址'].str.contains('测试') == False]
print("‘收货地址’去除'测试'后:%s行，%s列" % (data2.shape[0],data2.shape[1]))
print("*"*100)


# data_ceshi = data[data['收货地址'].str.contains('测试')]
# print("‘收货地址’含测试{}行，{}列。".format(data_ceshi.shape[0],data_ceshi.shape[1]))
# print("查看含测试行：{}".format(data_ceshi[["收货地址","订单编号"]]))


print("*"*100)


#订单生成时间分列
split = pd.DataFrame((x.split(' ') for x in data['订单生成时间']), index=data.index, columns=['订单生成日期','订单时间'])
data = pd.merge(data,split,left_index=True,right_index=True)



#vlookup产品标卡
data2 =pd.merge(data2,biaoka,how='left',on='销售品编号')
print("匹配标卡后，行列数:%s行，%s列" % (data2.shape[0],data2.shape[1]))
print("*"*100)

data_evening = data2


# #筛选"订单生成日期"中指定日期
# data_evening = data2[today] #改时间状态
# print("筛选'订单生成日期'中指定日期后，行列数:%s行，%s列" % (data2.shape[0],data2.shape[1]))
# print("*"*100)

print(data_evening["分类"].value_counts())
# 打印空白行
data_kong = data_evening[data_evening['分类'].isnull()]
print('*'*100)
print(data_kong.columns)
print("*"*100)
print("打印为空行{}".format(data_kong[["销售品名称_x","销售品编号"]]))
print("*"*100)


# "分类"中去除"新装"和空白
data_evening = data_evening[data_evening['分类'].notnull()]
print("分类去空：{}行{}列".format(data_evening.shape[0],data_evening.shape[1]))
print("&"*100)


data_evening = data_evening[~data_evening['分类'].str.contains('新装')]
print("'分类'中去除'新装'后，行列数:%s行，%s列" % (data_evening.shape[0],data_evening.shape[1]))
print("*"*100)


#电话去重
data_evening = data_evening.drop_duplicates(subset='收货人电话号码',keep='first')
print("电话去重：{}行，{}列。".format(data_evening.shape[0],data_evening.shape[1]))
print("*"*100)


# 导出
data_outer = data_evening[['收货人电话号码','分类','订单生成时间','号码归属地']]
print("准备导出：{}行，{}列。".format(data_outer.shape[0],data_outer.shape[1]))
print("*"*100)



outer = outpath + str(time.strftime("%Y-%m-%d", time.localtime())) + "促上传待分省(不含新装,电话去重)" + noon + ".xlsx"
data_outer.to_excel(outer,index=False)









