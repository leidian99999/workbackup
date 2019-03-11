import pandas as pd
import re
import openpyxl
pd.set_option('max_colwidth',1000)

df_tui = pd.read_csv("G:/work/logistica/input/tui/tui_Jan19.csv")
print("查询接口：{}行，{}列：".format(df_tui.shape[0],df_tui.shape[1]))

df_tui["承运商"] = df_tui["承运商"].map(lambda x:str(x))
df_tui["承运商"] = df_tui["承运商"].map(str.strip)

dict ={'ems':'EMS','邮政':'EMS','100000137':'圆通','ZHAIJISONG':'宅急送','jingdongwuliu':'京东物流'}

df1_tui = df_tui.replace(dict)

print(df1_tui["承运商"].value_counts())


df1_tui_SF = df1_tui[df1_tui["承运商"] == "顺丰"]
df1_tui_EMS = df1_tui[df1_tui["承运商"] == "EMS"]
df1_tui_JD = df1_tui[df1_tui["承运商"] == "京东物流"]
df1_tui_YD = df1_tui[df1_tui["承运商"] == "韵达"]
df1_tui_ZT = df1_tui[df1_tui["承运商"] == "中通"]
df1_tui_ZJS = df1_tui[df1_tui["承运商"] == "宅急送"]
df1_tui_YT = df1_tui[df1_tui["承运商"] == "圆通"]
df1_tui_hyytes = df1_tui[df1_tui["承运商"] == "恒宇运通"]
df1_tui_YZ = df1_tui[df1_tui["承运商"] == "邮政包裹"]

df1_tui_EMS[['EMS快递员','EMS快递员电话']] = df1_tui_EMS['物流轨迹'].str.extract('投递员姓名：(\\w+);联系电话：(\\d+)', expand=False)
df1_tui_JD[['JD快递员','JD快递员电话']] = df1_tui_JD['物流轨迹'].str.extract('配送员：(\\w+)，电话：(\\d+)', expand=False)
df1_tui_ZT[['ZT快递员','ZT快递员电话']] = df1_tui_ZT['物流轨迹'].str.extract('(\\w+)正在派件(\\d+)', expand=False)
df1_tui_YZ[['YZ快递员','YZ快递员电话']] = df1_tui_YZ['物流轨迹'].str.extract('配送员：(\\w+)，电话：(\\d+)', expand=False)
df1_tui_YD[['YD快递员','YD快递员电话']] = df1_tui_YD['物流轨迹'].str.extract('派件员\s(\\w+)\s(\\d+)', expand=False)
# df1_tui_hyytes[['hyytes快递员','hyytes快递员电话']] = df1_tui_hyytes['物流轨迹'].str.extract('派件员[(\\w+)]正在派件..电话[(\\d+)]', expand=False)
df1_tui_hyytes[['hyytes快递员姓名', 'hyytes快递员电话']] = df1_tui_hyytes['物流轨迹'].str.extract('派送员\[(\w+)\].*电话\[(\d+)\]', expand=False)

outpath = "G:/work/logistica/output/TUI/1901/1901_tui.xlsx"
writer = pd.ExcelWriter(outpath)
df1_tui_ZT.to_excel(writer,sheet_name="ZT",index=False)
df1_tui_JD.to_excel(writer,sheet_name="JD",index=False)
df1_tui_EMS.to_excel(writer,sheet_name="EMS",index=False)
df1_tui_YZ.to_excel(writer,sheet_name="YZ",index=False)
df1_tui_hyytes.to_excel(writer,sheet_name="hyytes",index=False)
df1_tui_YD.to_excel(writer,sheet_name="YD",index=False)
writer.save()


