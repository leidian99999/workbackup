import pandas as pd

data = pd.read_excel(r"F:\temp\190625/0623激活.xlsx",sheet_name = "Sheet1")
biaoka = pd.read_excel(r"G:\work\daily\DataShow\产品标卡.xlsx")


# 分列
split1 = pd.DataFrame((x.split('/') for x in data['号码归属地']),index=data.index,columns=['所属省','所属市'])
data = pd.merge(data, split1, left_index=True, right_index=True)

data_New = pd.merge(data, biaoka, how="left", on="销售品编号")


data_New["是否线下模式"] = data_New["是否线下模式"].fillna("否")

df = pd.pivot_table(data_New, index=[u'所属省'], values=['订单编号'],columns=[u'是否线下模式'],
                                      aggfunc=[len], fill_value=0,
                                      margins=True, margins_name='合计')


writer=pd.ExcelWriter(r'G:\work\daily\DataShow\新表.xlsx')
df.to_excel(writer,sheet_name='sheet1')
data_New.to_excel(writer,sheet_name='sheet2')

writer.save()