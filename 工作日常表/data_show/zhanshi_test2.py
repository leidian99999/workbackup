import pandas as pd
import xlsxwriter
import numpy as np

df1 = pd.read_excel(r"F:\temp\190529\数据准备\3&7日189.xlsx")
df2 = pd.read_excel(r"F:\temp\190529\数据准备\3&7日前新生产线下京东下省.xlsx")
df3 = pd.read_excel(r"F:\temp\190529\数据准备\首充.xlsx",sheet_name="Sheet1")
df4 = pd.read_excel(r"F:\temp\190529\数据准备\首充0530.xlsx")
df5 = pd.read_excel(r"F:\temp\190529\数据准备\业务订单明细[20190530164757].xlsx")

def paidan(x):
    if x is np.nan :
        return 0
    else:
        return 1

# 各数据集处理
df1 = df1[(True ^ df1['订单状态'].isin(['办理成功','办理中','办理失败']))]
df1 = df1[pd.notnull(df1['所在省 / 市 / 县'])]
df1 = df1[df1["订单编号"].str.contains('订单编号') == False]
split1 = pd.DataFrame((x.split(' ') for x in df1['订单生成时间']), index=df1.index, columns=['订单生成日期','订单生成小时'])
df1 = pd.merge(df1,split1,left_index=True,right_index=True)

df2 = df2[df2["模式分类"] == "京东模式"]
df2 = df2[pd.notnull(df2['是否下省'])]

df34 = pd.concat([df3,df4])
df34 = df34.drop_duplicates(subset=['用户名'],keep='first')
df34 = df34[df34["订单编号"].str.contains('订单编号') == False]
df34['用户名'] = df34['用户名'].map(lambda x : round(x,0))

df51 = df5[["运营商单号","物流单号"]]
df52 = df5[["运营商单号","APP操作时间"]]
df51 = df51[pd.notnull(df51['物流单号'])]
df52 = df52[pd.notnull(df52['APP操作时间'])]

# 合表
df11 = pd.merge(df1,df2[["订单编号","模式分类","是否下省"]],left_on="订单编号",right_on="订单编号",how="left")
df11 = pd.merge(df11,df51,left_on="订单编号",right_on="运营商单号",how="left")
df11 = pd.merge(df11,df52,left_on="订单编号",right_on="运营商单号",how="left")
df11['入网手机号'] = df11['入网手机号'].apply(int)
df11 = pd.merge(df11,df34[['订单编号','用户名']],left_on="入网手机号",right_on="用户名",how="left")

df11['派单'] = df11["是否下省"].apply(paidan)
df11['派卡'] = df11["物流单号_y"].apply(paidan)
df11['上门'] = df11["APP操作时间"].apply(paidan)
df11['首充'] = df11["订单编号_y"].apply(paidan)

df11.to_excel(r"F:\temp\190529\数据准备\test1.xlsx",index=False)