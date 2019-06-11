import pandas as pd
import numpy as np


# df = data[["号码归属地","销售品编号","营业厅送货方式","派单","派卡","上门","首充","发货量","签收量","激活量"]]

# split1 = pd.DataFrame((x.split('/') for x in df['号码归属地']),index=df.index,columns=['所属省','所属市'])
# df = pd.merge(df, split1, left_index=True, right_index=True)

# df["销售品编号"] = df["销售品编号"].map(lambda x : str(x))
# biaoka["销售品编号"] = biaoka["销售品编号"].map(lambda x : str(x))

# df = pd.merge(df,biaoka,how="left",on="销售品编号")


# df_SHCH_product = df.groupby(by=["分类"])["首充"].sum()
# df["营业厅送货方式"] = df["营业厅送货方式"].fillna("盲投")
# df_M = df[df["营业厅送货方式"] == "盲投"]

# 盲投（省份）
def M_mode_province(df):
    df_SHCH_province = pd.pivot_table(df, index=[u'所属省'], values=['首充'],
                                      aggfunc=[np.sum], fill_value=0,
                                      margins=True, margins_name='合计')
    df["营业厅送货方式"] = df["营业厅送货方式"].fillna("盲投")
    df_M = df[df["营业厅送货方式"] == "盲投"]
    df_M_province = df_M.groupby(by=["所属省"]).sum()
    df_M_province.loc['合计'] = df_M_province.apply(lambda x: x.sum())
    df_M_province["省份订单量占比"] = df_M_province["来单量"].map(
        lambda x: (2 * x) / (sum(df_M_province["来单量"])+0.00001)
    )
    df_M_province["发货率"] = df_M_province["发货量"] / (df_M_province["来单量"] + 0.00001)
    df_M_province["异常筛查"] = df_M_province["来单量"] - df_M_province["发货量"]
    df_M_province["异常筛查率"] = df_M_province["异常筛查"] / (df_M_province["来单量"] + 0.00001)
    df_M_province["签收率"] = df_M_province["签收量"] / (df_M_province["发货量"] + 0.00001)
    df_M_province["未签收量"] = df_M_province["发货量"] - df_M_province["签收量"]   
    df_M_province["未签收率"] = df_M_province["未签收量"] / (df_M_province["发货量"] + 0.00001)
    df_M_province["省份激活量占比"] = df_M_province["激活量"].map(
        lambda x: (2 * x) / (sum(df_M_province["激活量"])+ 0.00001)
    )  
    df_M_province["激活率"] = df_M_province["激活量"] / (df_M_province["签收量"] + 0.00001)
    df_M_province["未激活量"] = df_M_province["签收量"] - df_M_province["激活量"]   
    df_M_province["未激活率"] = df_M_province["未激活量"] / (df_M_province["签收量"] + 0.00001)
    df_M_province["发货激活率"] = df_M_province["激活量"] / (df_M_province["发货量"] + 0.00001)
    df_M_province["省份首充量占比"] = df_M_province["首充"].map(
        lambda x: (2 * x) / (sum(df_M_province["首充"]) + 0.00001)
    )   
    df_M_province["首充率"] = df_M_province["首充"] / (df_M_province["发货量"] + 0.00001)
    df_M_province["全量首充"] = df_SHCH_province   
    df_M_province = df_M_province.reset_index('所属省')  
    df_M_province2 = df_M_province[["所属省","来单量",
                                    "省份订单量占比",
                                    "发货量",
                                    "发货率",
                                    "异常筛查",
                                    "异常筛查率",
                                    "签收量",
                                    "签收率",
                                    "未签收量",
                                    "未签收率",
                                    "激活量",
                                    "省份激活量占比",
                                    "激活率","未激活量","未激活率","发货激活率",
                                    "首充",
                                    "省份首充量占比",
                                    "首充率",
                                    "全量首充"]]
    return df_M_province2

# 盲投（产品）
def M_mode_product(df):
    # df_SHCH_product = df.groupby(by=["分类"])["首充"].sum()  # 省份全首充

    df_SHCH_product = pd.pivot_table(df, index=[u'分类'], values=['首充'],
                                      aggfunc=[np.sum], fill_value=0,
                                      margins=True, margins_name='合计')

    df["营业厅送货方式"] = df["营业厅送货方式"].fillna("盲投")
    df_M = df[df["营业厅送货方式"] == "盲投"]
    df_M_product = df_M.groupby(by=["分类"]).sum()
    df_M_product.loc['合计'] = df_M_product.apply(lambda x: x.sum())
    df_M_product["产品订单量占比"] = df_M_product["来单量"].map(
        lambda x: (2 * x) / (sum(df_M_product["来单量"])+0.00001)
    )
    df_M_product["发货率"] = df_M_product["发货量"] / (df_M_product["来单量"] + 0.00001)
    df_M_product["异常筛查"] = df_M_product["来单量"] - df_M_product["发货量"]
    df_M_product["异常筛查率"] = df_M_product["异常筛查"] / (df_M_product["来单量"] + 0.00001)
    df_M_product["签收率"] = df_M_product["签收量"] / (df_M_product["发货量"] + 0.00001)
    df_M_product["未签收量"] = df_M_product["发货量"] - df_M_product["签收量"]   
    df_M_product["未签收率"] = df_M_product["未签收量"] / (df_M_product["发货量"] + 0.00001)
    df_M_product["产品激活量占比"] = df_M_product["激活量"].map(
        lambda x: (2 * x) / (sum(df_M_product["激活量"])+ 0.00001)
    )  
    df_M_product["激活率"] = df_M_product["激活量"] / (df_M_product["签收量"] + 0.00001)
    df_M_product["未激活量"] = df_M_product["签收量"] - df_M_product["激活量"]   
    df_M_product["未激活率"] = df_M_product["未激活量"] / (df_M_product["签收量"] + 0.00001)
    df_M_product["发货激活率"] = df_M_product["激活量"] / (df_M_product["发货量"] + 0.00001)
    df_M_product["产品首充量占比"] = df_M_product["首充"].map(
        lambda x: (2 * x) / (sum(df_M_product["首充"]) + 0.00001)
    )   
    df_M_product["首充率"] = df_M_product["首充"] / (df_M_product["发货量"] + 0.00001)
    df_M_product["全量首充"] = df_SHCH_product   
    df_M_product = df_M_product.reset_index('分类')
    df_M_product2 = df_M_product[["分类","来单量",
                                    "产品订单量占比",
                                    "发货量",
                                    "发货率",
                                    "异常筛查",
                                    "异常筛查率",
                                    "签收量",
                                    "签收率",
                                    "未签收量",
                                    "未签收率",
                                    "激活量",
                                    "产品激活量占比",
                                    "激活率","未激活量","未激活率","发货激活率",
                                    "首充",
                                    "产品首充量占比",
                                    "首充率",
                                    "全量首充"]]
    return df_M_product2

# 京东线下（省份）


def JD_mode_province(df):
    # df_SHCH_province = df.groupby(by=["所属省"])["首充"].sum()  # 省份全首充

    df_SHCH_province = pd.pivot_table(df, index=[u'所属省'], values=['首充'],
                                      aggfunc=[np.sum], fill_value=0,
                                      margins=True, margins_name='合计')

    df_JD = df[df["营业厅送货方式"] == "线下送货（京东模式）"]
    df_JD_province = df_JD.groupby(by=["所属省"]).sum()
    df_JD_province.loc['合计'] = df_JD_province.apply(lambda x: x.sum())
    df_JD_province["省份派单量占比"] = df_JD_province["派单"].map(
        lambda x: (2 * x) / (sum(df_JD_province["派单"]) + 0.00001)
    )
    df_JD_province["派卡率"] = df_JD_province["派卡"] / (df_JD_province["派单"] + 0.00001)
    df_JD_province["异常筛查"] = df_JD_province["派单"] - df_JD_province["派卡"]
    df_JD_province["异常筛查率"] = df_JD_province["异常筛查"] / (df_JD_province["派单"] + 0.00001)
    df_JD_province["上门率"] = df_JD_province["上门"] / (df_JD_province["派卡"]+0.00001)
    df_JD_province["未上门"] = df_JD_province["派卡"] - df_JD_province["上门"]
    df_JD_province["未上门率"] = df_JD_province["未上门"] / (df_JD_province["派卡"]+0.00001)
    df_JD_province["省份激活量占比"] = df_JD_province["激活量"].map(
        lambda x: (2 * x) / (sum(df_JD_province["激活量"])+0.00001)
    )
    df_JD_province["激活率"] = df_JD_province["激活量"] / (df_JD_province["派卡"]+0.00001)
    df_JD_province["省份首充量占比"] = df_JD_province["首充"].map(
        lambda x: (2 * x) / (sum(df_JD_province["首充"])+0.00001)
    )
    df_JD_province["首充率"] = df_JD_province["首充"] / (df_JD_province["派卡"]+0.00001)
    df_JD_province["全量首充"] = df_SHCH_province
    df_JD_province = df_JD_province.reset_index('所属省')
    df_JD_province2 = df_JD_province[["所属省","派单",
                             "省份派单量占比",
                             "派卡",
                             "派卡率",
                             "异常筛查",
                             "异常筛查率",
                             "上门",
                             "上门率",
                             "未上门",
                             "未上门率",
                             "激活量",
                             "省份激活量占比",
                             "激活率",
                             "首充",
                             "省份首充量占比",
                             "首充率",
                             "全量首充"]]
    return df_JD_province2

# 京东线下（产品）

def JD_mode_product(df):
    # df_SHCH_product = df.groupby(by=["分类"])["首充"].sum()

    df_SHCH_product = pd.pivot_table(df, index=[u'分类'], values=['首充'],
                                      aggfunc=[np.sum], fill_value=0,
                                      margins=True, margins_name='合计')


    df_JD = df[df["营业厅送货方式"] == "线下送货（京东模式）"]
    df_JD_product = df_JD.groupby(by=["分类"]).sum()
    df_JD_product.loc['合计'] = df_JD_product.apply(lambda x: x.sum())
    df_JD_product["产品派单量占比"] = df_JD_product["派单"].map(
    lambda x: (2 * x) / (sum(df_JD_product["派单"])+0.00001)
    )
    df_JD_product["派卡率"] = df_JD_product["派卡"] / (df_JD_product["派单"] + 0.00001)
    df_JD_product["异常筛查"] = df_JD_product["派单"] - df_JD_product["派卡"]
    df_JD_product["异常筛查率"] = df_JD_product["异常筛查"] / (df_JD_product["派单"] + 0.00001)
    df_JD_product["上门率"] = df_JD_product["上门"] / (df_JD_product["派卡"] + 0.00001)
    df_JD_product["未上门"] = df_JD_product["派卡"] - df_JD_product["上门"]
    df_JD_product["未上门率"] = df_JD_product["未上门"] / (df_JD_product["派卡"] + 0.00001)
    df_JD_product["产品激活量占比"] = df_JD_product["激活量"].map(
    lambda x: (2 * x) / (sum(df_JD_product["激活量"])+0.00001)
    )
    df_JD_product["激活率"] = df_JD_product["激活量"] / (df_JD_product["派卡"] + 0.00001)
    df_JD_product["产品首充量占比"] = df_JD_product["首充"].map(
    lambda x: (2 * x) / (sum(df_JD_product["首充"])+0.00001)
    )
    df_JD_product["首充率"] = df_JD_product["首充"] / (df_JD_product["派卡"] + 0.00001)
    df_JD_product["全量首充"] = df_SHCH_product
    df_JD_product = df_JD_product.reset_index('分类')
    df_JD_product2 = df_JD_product[["分类","派单",
    "产品派单量占比",
    "派卡",
    "派卡率",
    "异常筛查",
    "异常筛查率",
    "上门",
    "上门率",
    "未上门",
    "未上门率",
    "激活量",
    "产品激活量占比",
    "激活率",
    "首充",
    "产品首充量占比",
    "首充率",
    "全量首充"]]


    return df_JD_product2
