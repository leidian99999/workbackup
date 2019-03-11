import pandas as pd
import csv

df = pd.read_csv(r"G:\work\basic\alter\1812_info_alter.csv")
df_tui = pd.read_csv(r"G:\work\logistica\output\CHA\CSV\201812_JD_cha.csv")

carrier = "京东物流"
# province

df1 = df[[ '订单编号','承运商','收货地址',"号码归属地","物流签收时间","是否线下模式","物流单号"]]

split = pd.DataFrame((x.split('/') for x in df1['号码归属地']), index=df1.index, columns=['号码归属省','号码归属地区'])
df1 = pd.merge(df1,split,left_index=True,right_index=True)
df1 = df1.drop(columns="号码归属地")

df1 = df1.dropna(subset=["收货地址"])

dict ={'ems':'EMS','邮政':'EMS','100000137':'圆通','ZHAIJISONG':'宅急送','jingdongwuliu':'京东物流','yunda':'韵达','shunfeng':'顺丰','EMS物流':'EMS'}

df1 =df1.replace(dict)

df1_JD = df1[df1["承运商"] == carrier]

df1_ZJ_JD = df1_JD[df1_JD["号码归属省"] == "浙江省"]
df1_SC_JD = df1_JD[df1_JD["号码归属省"] == "四川省"]

df1_ZJ_JD_tui = pd.merge(df1_ZJ_JD,df_tui,how="inner",left_on="订单编号",right_on="JD_OrderId")
df1_SC_JD_tui = pd.merge(df1_SC_JD,df_tui,how="inner",left_on="订单编号",right_on="JD_OrderId")

df1_ZJ_JD_tui = df1_ZJ_JD_tui.drop(columns=['JD_OrderId','JD_trackingID'])
df1_SC_JD_tui = df1_SC_JD_tui.drop(columns=['JD_OrderId','JD_trackingID'])

df1_ZJ_JD_tui["导航地址"] = df1_ZJ_JD_tui[ '号码归属省'] + df1_ZJ_JD_tui[ '号码归属地区'] +df1_ZJ_JD_tui[ '收货地址']
df1_SC_JD_tui["导航地址"] = df1_SC_JD_tui[ '号码归属省'] + df1_SC_JD_tui[ '号码归属地区'] +df1_SC_JD_tui[ '收货地址']


df1_SC_JD_tui.to_excel(r"F:\temp\190306\1812四川京东推送明细.xlsx",index=False)
df1_ZJ_JD_tui.to_excel(r"F:\temp\190306\1812浙江京东推送明细.xlsx",index=False)