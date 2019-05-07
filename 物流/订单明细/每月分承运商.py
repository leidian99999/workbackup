import pandas as pd

def FenCarrier(df,col,writer,name):
    print("开始分承运商")
    print(df[col].value_counts())
    carrier_list = df[col].unique()
    for carrier in carrier_list:
        df_new = df[df[col] == carrier]
        df_new.to_excel(writer + carrier + name + '.xlsx', index=False)
        print("已完成：" + str(carrier))

date = "1903"
data = pd.read_csv(r"G:\work\basic\alter\\"+date+"_info_alter_gai.csv")
writer = "G:\\work\\basic\\carriers_lnglat\\"+date+"\\"
df = data[data["承运商"].isin(["京东线下","EMS","顺丰","京东物流","韵达","中通","宅急送"])]
df["承运商"] = df["承运商"].map(lambda x:str(x))


col = "承运商"  
name = "_info_carrier"

FenCarrier(df,col,writer,name)