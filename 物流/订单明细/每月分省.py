import pandas as pd

def FenSheng(df,col,writer,name):
    print("开始分省")
    print(df[col].value_counts())
    sheng_list = df[col].unique()
    for sheng in sheng_list:
        df_new = df[df[col] == sheng]
        df_new.to_excel(writer + sheng + name + '.xlsx', index=False)
        print("已完成：" + str(sheng))

df = pd.read_csv(r"G:/work/basic/alter/1812_info_alter_gai.csv")
writer = "G:/work/basic/province/DEC18\\"

col = "所在省"
name = "(所在省)"

FenSheng(df,col,writer,name)