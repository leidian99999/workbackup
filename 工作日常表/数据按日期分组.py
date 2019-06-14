import pandas as pd

data = pd.read_excel(r"F:\temp\190614\2月合表.xlsx")

df = df[df["订单编号"].str.contains('订单编号') == False]

split1 = pd.DataFrame((x.split(' ') for x in df['订单日期']),index=df.index,columns=['分列后订单日期','分列后订单小时'])
df = pd.merge(df, split1, left_index=True, right_index=True)

writer = "F:/temp/190614/" # 输出路径

def FenSheng(df,col,writer):
    print("开始分省")
    print(df[col].value_counts())
    sheng_list = df[col].unique()
    print("*"*100)
    print(sheng_list)

    for sheng in sheng_list:
        df_new = df[df[col] == sheng]
        df_new.to_excel(writer + sheng  +'.xlsx', index=False)
    print('拆分完成！')

FenSheng(df,"分列后订单日期",writer)