import pandas as pd
import re
import openpyxl
pd.set_option('max_colwidth',1000)

df_cha = pd.read_csv("F:/temp/190218/cha_19Jan.csv")
print("查询接口：{}行，{}列：".format(df_cha.shape[0],df_cha.shape[1]))

df_cha["承运商"] = df_cha["承运商"].map(lambda x:str(x))
df_cha["承运商"] = df_cha["承运商"].map(str.strip)

dict ={'ems':'EMS','邮政':'EMS','100000137':'圆通','ZHAIJISONG':'宅急送','jingdongwuliu':'京东物流'}

df1_cha = df_cha.replace(dict)

print(df1_cha["承运商"].value_counts())

exit()

df1_cha_SF = df1_cha[df1_cha["承运商"] == "顺丰"]
df1_cha_EMS = df1_cha[df1_cha["承运商"] == "EMS"]
df1_cha_JD = df1_cha[df1_cha["承运商"] == "京东物流"]
df1_cha_YD = df1_cha[df1_cha["承运商"] == "韵达"]
df1_cha_ZT = df1_cha[df1_cha["承运商"] == "中通"]
df1_cha_ZJS = df1_cha[df1_cha["承运商"] == "宅急送"]
df1_cha_YT = df1_cha[df1_cha["承运商"] == "圆通"]
df1_cha_hyytes = df1_cha[df1_cha["承运商"] == "恒宇运通"]
df1_cha_YZ = df1_cha[df1_cha["承运商"] == "邮政包裹"]

df1_cha_YZ[['YZ签收情况','YZ签收人']] = df1_cha_YZ['已签收'].str.extract('已签收,(\w+)[:,：](\w+).*', expand=False)
df1_cha_hyytes[['hyytes签收情况','hyytes签收人']] = df1_cha_hyytes['已签收'].str.extract('(订单审核为已签收),签收人是：(\w+)', expand=False)
df1_cha_JD[['JD签收情况','JD签收人']] = df1_cha_JD['已签收'].str.extract('货物已由(\w+)，感谢您选择(京东物流！)', expand=False)
df1_cha_YD[['YD签收人','YD签收情况']] = df1_cha_YD['已签收'].str.extract('快件已被\s(\w+)\s(\w+)。如有问题请电联业务员', expand=False)
df1_cha_SF['SF签收情况'] = df1_cha_SF['已签收'].str.extract('(.*),感谢使用顺丰,期待再次为您服务', expand=False)
df1_cha_YT[['YT签收人','YT签收情况']] = df1_cha_YT['已签收'].str.extract('签收人: (\w+)\s(\w+)\s感谢使用圆通速递，期待再次为您服务', expand=False)
df1_cha_ZJS['ZJS签收情况'] = df1_cha_ZJS['已签收'].str.extract('(\w+)', expand=False)
df1_cha_EMS[['EMS签收情况','EMS签收人']] = df1_cha_EMS['已签收'].str.extract('(\w+)，签收人：(\w+)', expand=False)
df1_cha_ZT[['ZT签收情况','ZT签收人']] = df1_cha_ZT['已签收'].str.extract('\s(\w+),\s(.*), 如有疑问请电联', expand=False)


outpath = "F:/temp/190218/cha.xlsx"
writer = pd.ExcelWriter(outpath)
df1_cha_YZ.to_excel(writer,sheet_name="YZ",index=False)
df1_cha_hyytes.to_excel(writer,sheet_name="hyytes",index=False)
df1_cha_JD.to_excel(writer,sheet_name="JD",index=False)
df1_cha_YD.to_excel(writer,sheet_name="YD",index=False)
df1_cha_SF.to_excel(writer,sheet_name="SF",index=False)
df1_cha_YT.to_excel(writer,sheet_name="YT",index=False)
df1_cha_ZJS.to_excel(writer,sheet_name="ZJS",index=False)
df1_cha_EMS.to_excel(writer,sheet_name="EMS",index=False)
df1_cha_ZT.to_excel(writer,sheet_name="ZT",index=False)
writer.save()


