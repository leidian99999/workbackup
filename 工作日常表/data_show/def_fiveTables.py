import pandas as pd
import xlsxwriter
import numpy as np
from os import walk
from datetime import datetime,timedelta


# inputPath = "D:/work/daily/"
#
# for root,dirs,files in walk(inputPath + "7日",topdown=False):
#     print(files)
# num = len(files)
# df1 = pd.DataFrame()
# for i in range(num):
#     newdata = pd.read_excel(inputPath + '7日\%s'%files[i])
#     df1 = df1.append(newdata) # 189
#
#
# # df1 = pd.read_excel(r"F:\temp\190529\数据准备\3&7日189.xlsx")
# df2 = pd.read_excel(inputPath + "七日新生产"+ date + ".xlsx") # 新生产表
# df3 = pd.read_excel(inputPath + "首充成功明细.xlsx", sheet_name="Sheet1") # 首充历史表
# df4 = pd.read_excel(inputPath + "首充" + date + ".xlsx") # 当日历史表
# df5 = pd.read_excel(inputPath + "京东" + date +".xlsx") # 京东表

def laidan(x):
    if x is np.nan:
        return 0
    else:
        return 1


def fahuo(a,b,c):
    if a is not np.nan:
        return 1
    elif a is np.nan and b == "交易完成":
        return 1
    elif a is np.nan and c is not np.nan:
        return 1
    else:
        return 0

def qianshou(a,b):
    if a is not np.nan:
        return 1
    elif a is np.nan and b == "交易完成":
        return 1
    else:
        return 0

def jihuo(x):
    if x == "交易完成":
        return 1
    else:
        return 0

def paidan(x):
    if x is np.nan:
        return 0
    else:
        return 1

def shouchong(x):
    if x == -1:
        return 0
    else:
        return 1

# 各数据集处理


def five_tables(df1, df2, df3, df4, df5):
    df1 = df1[(True ^ df1['订单状态'].isin(['办理成功', '办理中', '办理失败']))]
    df1 = df1[pd.notnull(df1['所在省 / 市 / 县'])]
    df1 = df1[df1["订单编号"].str.contains('订单编号') == False]
    df1 = df1.drop_duplicates(subset=['订单编号'], keep='first')
    df1 = df1[pd.notnull(df1['号码归属地'])]
    df1 = df1[pd.notnull(df1['入网手机号'])]
    df1["入网手机号"] = df1['入网手机号'].astype('int64')

    df2 = df2[df2["模式分类"] == "京东模式"]
    df2 = df2[pd.notnull(df2['是否下省'])]

    df34 = pd.concat([df3, df4],sort=False)
    df34 = df34.drop_duplicates(subset=['用户名'], keep='first') # 用户名
    df34 = df34[pd.notnull(df34['用户名'])]
    df34["用户名"] = df34['用户名'].astype('int64')

    df51 = df5[["运营商单号", "物流单号"]]
    df52 = df5[["运营商单号", "APP操作时间"]]
    df51 = df51[pd.notnull(df51['物流单号'])]
    df52 = df52[pd.notnull(df52['APP操作时间'])]

    # 合表
    df11 = pd.merge(df1, df2[["订单编号", "模式分类", "是否下省"]],
                    left_on="订单编号", right_on="订单编号", how="left")
    df11 = pd.merge(df11, df51, left_on="订单编号", right_on="运营商单号", how="left")
    df11 = pd.merge(df11, df52, left_on="订单编号", right_on="运营商单号", how="left")
    df11['入网手机号'] = df11['入网手机号'].apply(int)
    df11 = pd.merge(df11, df34[['用户名']],left_on="入网手机号", right_on="用户名", how="left") #'订单编号',
    # df11 = df11[df11["订单状态"] == "交易完成"]
    df11["用户名_y"] = df11["用户名_y"].fillna(-1)
    df11["用户名_y"] = df11['用户名_y'].astype('int64')

    # 计算变量
    df11['派单'] = df11["是否下省"].apply(paidan)
    df11['派卡'] = df11["物流单号_y"].apply(paidan)
    df11['上门'] = df11["APP操作时间"].apply(paidan)
    df11['首充'] = df11["用户名_y"].apply(shouchong) #订单编号_y
    df11['来单量'] = df11['订单编号'].apply(laidan) #订单编号_x
    df11['发货量'] = df11.apply(lambda x: fahuo(x["物流单号_x"], x["订单状态"], x["物流签收时间"]), axis=1)
    df11['签收量'] = df11.apply(lambda x: qianshou(x["物流签收时间"], x["订单状态"]), axis=1)
    df11['激活量'] = df11["订单状态"].apply(jihuo)
    # 精简数据集
    df = df11[["号码归属地","销售品编号","营业厅送货方式","派单","派卡","上门","首充","发货量","签收量","激活量","来单量"]]
    # 最后处理
    split1 = pd.DataFrame((x.split('/') for x in df['号码归属地']),index=df.index,columns=['所属省','所属市'])
    df = pd.merge(df, split1, left_index=True, right_index=True)

    df["销售品编号"] = df["销售品编号"].map(lambda x : str(x))

    return df,df34

# 获取前n日日期
def get_nday_list(date,n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:
        result_date = datetime.strptime(date, '%Y-%m-%d') - timedelta(days=i)
        d = result_date.strftime('%Y-%m-%d')
        before_n_days.append(d)
    print(before_n_days)
    return before_n_days