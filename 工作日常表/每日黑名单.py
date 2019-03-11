import pandas as pd 

df_gongxin = pd.read_excel(r"G:\work\日报\黑名单\生产风险信息库v1.4-2019.1.25gai.xlsx",sheet_name="明细") 
df_laidan = pd.read_excel(r"G:\work\日报\黑名单\test\0122数据-0123取数1.xlsx")
writer = pd.ExcelWriter(r"G:\work\日报\黑名单\test\\190125黑名单.xlsx")

df_gongxin["风险入网人身份证号"] = df_gongxin["风险入网人身份证号"].fillna("无身份证")
df_gongxin["风险收件人手机号"] = df_gongxin["风险收件人手机号"].fillna("无手机号")

df_gongxin["风险收件人手机号"] = df_gongxin["风险收件人手机号"].map(lambda x:str(x))
df_gongxin["风险入网人身份证号"] = df_gongxin["风险入网人身份证号"].map(lambda x:str(x))

df_gongxin_id = df_gongxin[df_gongxin["风险入网人身份证号"].str.contains("无身份证") == False]
df_gongxin_tel = df_gongxin[df_gongxin["风险收件人手机号"].str.contains("无手机号") == False]

df_laidan["收货人电话号码"] = df_laidan["收货人电话号码"].map(lambda x:str(x))
df_laidan["入网身份证号"] = df_laidan["入网身份证号"].map(lambda x:str(x))

print("df_gongxin" +str(df_gongxin.shape))
print("df_gongxin_tel" +str(df_gongxin_tel.shape))
print("df_gongxin_id" +str(df_gongxin_id.shape))

df_tel = pd.merge(df_gongxin_tel,df_laidan,how="inner",left_on="风险收件人手机号", right_on="收货人电话号码") 
df_id  = pd.merge(df_gongxin_id,df_laidan,how="inner",left_on="风险入网人身份证号",right_on="入网身份证号")

print(df_tel)
exit()

pd.DataFrame(df_tel).to_excel(writer,sheet_name="风险手机号名单",index=False)
pd.DataFrame(df_id).to_excel( writer,sheet_name="风险身份证名单",index=False)