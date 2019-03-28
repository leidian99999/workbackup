import pandas as pd

def FenSheng(df,col,writer,name):
    print("开始分承运商")
    print(df[col].value_counts())
    sheng_list = df[col].unique()
    for sheng in sheng_list:
        df_new = df[df[col] == sheng]
        df_new.to_excel(writer + sheng + name + '.xlsx', index=False)
        print("已完成：" + str(sheng))

date = "1808"
data = pd.read_csv(r"G:\work\basic\alter\\"+date+"_info_alter_gai.csv")
writer = "G:\\work\\basic\\carriers\\"+date+"\\"
df = data[data["承运商"].isin(["京东线下","EMS","顺丰","京东物流","韵达","中通","宅急送"])]
df["承运商"] = df["承运商"].map(lambda x:str(x))


col = "承运商"  
name = "(承运商)"

FenSheng(df,col,writer,name)