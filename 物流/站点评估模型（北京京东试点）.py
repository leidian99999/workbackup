import pandas as pd 

data1 = pd.read_excel(r"G:\work\logistica\stations\JDStations\stations\gaode/JDstations_beijing_gaode.xlsx")
df_station = data1[["JD_siteName","JD_siteLng_gaode","JD_siteLat_gaode","JD_siteDistrict_gaode","JD_siteCity_gaode"]]

# data2 = pd.read_excel(r"G:\work\logistica\info\output\CHA\all\1901_JDWL.xlsx",header=None,skiprows=[0])

data2_WL = pd.read_excel(r"G:\work\logistica\info\output\CHA\all\1901_JDWL.xlsx",header=None,skiprows=[0])
data2_XX = pd.read_excel(r"G:\work\logistica\info\output\CHA\all\1901_JDXX.xlsx",header=None,skiprows=[0])
data2 = pd.concat([data2_WL,data2_XX])
data2.columns = ['ORDER_ID','MAIL_NO','ROUTE_TIME','JD_deliveryman_name','JD_deliveryman_tel','ROUTE_TIME','LOGISTICS_COMPANY','JD_lastStation','JD_status']
df_log = data2.copy()

data3 = pd.read_csv(r"G:\work\basic\alter/1901_info_alter_gai.csv")
df_info = data3[data3["所在省"] == "北京"]

print("  df_info:",df_info.shape)
print("  df_log:",df_log.shape)
print("  df_station:",df_station.shape)

df_info['订单编号'] = df_info['订单编号'].map(lambda x:str(x))
df_log['ORDER_ID'] = df_log['ORDER_ID'].map(lambda x:str(x))

df = pd.merge(pd.merge(df_info,df_log,how="inner",left_on='订单编号',right_on='ORDER_ID'),df_station,how="left",left_on="JD_lastStation",right_on="JD_siteName")

df["订单生成时间"] = pd.to_datetime(df["订单生成时间"])
df["交易完成时间"] = pd.to_datetime(df["交易完成时间"])
df["发货时间"] = pd.to_datetime(df["发货时间"])
df["物流签收时间"] = pd.to_datetime(df["物流签收时间"])

df["发货时效"] = round((df["发货时间"] - df["订单生成时间"]).dt.total_seconds() / 3600,0).map(lambda x:int(x))
df["签收时效"] = round((df["物流签收时间"] - df["发货时间"]).dt.total_seconds() / 3600,0).map(lambda x:int(x))
df["激活时效"] = round((df["交易完成时间"] - df["订单生成时间"]).dt.total_seconds() / 3600,0).fillna(-1).map(lambda x:int(x))


def get_sex(str1):
    #查看性别
    if str1 % 2 ==0:
        return '女'
    else:
        return '男'

df['性别'] = df["入网身份证号"].str.slice(16,17).map(lambda x:int(x)).apply(get_sex)

df['生日'] = pd.to_datetime(df['入网身份证号'].str[6:14])

now_year =datetime.datetime.today().year #当前的年份
df['年龄']=now_year-df["生日"].dt.year   

df = df[pd.notnull(df['JD_siteName'])]     

def target(str1):
    if str1 == "交易完成":
        return 1
    else:
        return 0

df["target"] = df["订单状态"].apply(target)     

  