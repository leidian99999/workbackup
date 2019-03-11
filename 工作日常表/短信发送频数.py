import pandas as pd
import numpy as np


fold = "异网"

# 读取文件
data = pd.read_excel(r"G:\work\日报\短信\输出\11.15-11.25"+fold+"短信汇总明细.xlsx")
data = data[data['订单生成时间'].str.contains('订单生成时间') == False]

data2 = pd.read_excel(r"G:\work\日报\短信反馈\11.1-11.25激活明细.xlsx")
data2 = data2[data2['交易完成时间'].str.contains('交易完成时间') == False]


# 文件备份
df1 = data.copy()
df2 = data2.copy()
df1 = df1[['订单生成时间','收货人电话号码','收货人姓名','物流签收时间', '入网手机号','所属省','分类']]
df2 = df2[['交易完成时间', '入网身份证号', '入网手机号','所属省','分类','生日', '年龄', 'sex', '性别']]
df2['入网手机号'] = df2['入网手机号'].astype("str")



# 文件处理
dft = pd.merge(df1,df2,how="left",on="入网手机号")
dft["is_null"] = dft['交易完成时间'].isnull()
dft["is_null"] = dft["is_null"].astype("str")

# 分是否激活数据集
dfa = dft[dft["is_null"].str.contains('False')] #激活
dfb = dft[dft["is_null"].str.contains('True')]  #未激活

a_MsgNum = dfa.groupby(by=["收货人电话号码",'分类_x']).agg({"收货人电话号码":"count"})
b_MsgNum = dfb.groupby(by=["收货人电话号码",'分类_x']).agg({"收货人电话号码":"count"})

a_MsgNum = a_MsgNum.rename(columns={'收货人电话号码':"发短信数"})
b_MsgNum = b_MsgNum.rename(columns={'收货人电话号码':"发短信数"})

print(a_MsgNum.shape)
a_MsgNum = a_MsgNum.reset_index()
print(b_MsgNum.shape)
b_MsgNum = b_MsgNum.reset_index()

df4 = dft.drop_duplicates(subset=['收货人电话号码'],keep='first')

df5a = pd.merge(a_MsgNum,df4,how="inner",on="收货人电话号码")
df5b = pd.merge(b_MsgNum,df4,how="inner",on="收货人电话号码")

#计算激活时效
df5a['订单生成时间'] = pd.to_datetime(df5a['订单生成时间'])
df5a['交易完成时间'] = pd.to_datetime(df5a['交易完成时间'])
df5a["激活时效"] = (df5a['交易完成时间'] - df5a['订单生成时间']).dt.days

df5b['订单生成时间'] = pd.to_datetime(df5b['订单生成时间'])
df5b['交易完成时间'] = pd.to_datetime(df5b['交易完成时间'])
df5b["激活时效"] = (df5b['交易完成时间'] - df5b['订单生成时间']).dt.days

# 区分沉默用户
bins =[-1,10,100] 
df5a['silence'] = pd.cut(df5a['激活时效'],bins,labels=["非沉默用户","沉默用户"])
df5b['silence'] = pd.cut(df5b['激活时效'],bins,labels=["非沉默用户","沉默用户"])




df5a.to_excel(r"G:\work\日报\短信\输出\11.15-11.25"+fold+"短信频数明细已激活改.xlsx",index=False)
df5b.to_excel(r"G:\work\日报\短信\输出\11.15-11.25"+fold+"短信频数明细未激活改.xlsx",index=False)