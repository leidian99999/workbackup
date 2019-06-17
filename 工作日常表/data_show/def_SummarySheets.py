# coding=utf-8

import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)
# 忽略无用警告
import warnings
warnings.filterwarnings(action="ignore")
pd.options.display.max_seq_items = 8000
pd.options.display.max_rows = 8000



# data_M = pd.read_excel(r"G:\work\daily\DataShow\B_Fan190615.xlsx")
# data_New = pd.read_excel(r"G:\work\daily\DataShow\190616\A1_type_king_card (4).xlsx",sheet_name="全部产品激活情况",skiprows=2,header=0)


def summary_sheets(df1,df2,product):
    # df1["日期"] = df1["日期"].dt.strftime("%Y-%m-%d")
    df1 = df1.set_index("日期")
    df1 = df1.loc['2019-01-01':'2019-04-30']

    df2 = df2.drop(columns=["Unnamed: 0"], axis=1)
    df2 = df2.fillna(method="ffill")
    df2 = df2[df2["产品"] == product]
    df2 = df2[["日期","来单量","发货量","总激活量","3日激活率","7日激活率","15日激活率"]]
    df2.rename(columns={"总激活量":"激活量"},inplace=True)
    df2 = df2.set_index("日期")

    df = pd.concat([df1,df2])
    df = df.reset_index("日期")

    df["3日激活率"][-2:] = "空"
    df["7日激活率"][-6:] = "空"
    df["15日激活率"][-14:] = "空"

    return df

def summary_25days(df,days,cat = "省份"):
    df = df.drop(columns=["Unnamed: 0"], axis=1)
    df = df.fillna(method="ffill")
    df = df[df["日期"] == days]
    df = df.append(df.iloc[0])
    df = df.iloc[1:]
    df = df[[cat, "来单量", "发货量", "签收量", "总激活量"]]
    return df