import pandas as pd
import os
import openpyxl

filename = "180105p"
filepath = r"G:\\work\\总数\\mysql\1月\\" + filename + ".xls"
writer = r"G:\\work\\总数\\mysql\1月\\完成\\" + filename + '.txt'


df = pd.read_excel(filepath)
print(df.shape)
print(df.columns)

list = ["订单编号","订单类型","订单状态","取消原因","订单挂起原因","订单来源","订单子状态","店铺","AB类型","订单金额","订单生成时间",
        "支付完成时间","支付平台","交易完成时间","发货时间","入网用户姓名","入网手机号","入网身份证号",
        "联系人电话号码","收货人姓名","收货地址","收货人电话号码","所在省 / 市 / 县","入网人所在省/市/县","号码归属地",
        "配送方式","CPS推荐人","订单备注","物流单号","物流签收时间","承运商","写卡渠道","销售品编号","销售品名称",
        "销售品类型","套餐","主号码","副号码","靓号等级",'靓号低消','靓号预存款','收货人邮箱']

df1 = df[list]
df1 = df1.rename(columns={'入网人所在省/市/县':'入网人所在地','靓号预存款':'靓号预存款'})
print(df1.shape)

outer = df1.to_csv(writer,sep="\t",index=True)


#engine='openpyxl'

