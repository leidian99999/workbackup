import pandas as pd
import re


def get_del_list(n):
    '''选出路径时间列'''
    dayslist = []
    for i in range(1, n + 1)[::-1]: # 倒序
        route_time = "ROUTE_TIME" + str(i)
        dayslist.append(route_time)
    return dayslist


def get_carrier_list(carrier):
    '''将DataFrame行转换为list'''
    a = []
    for indexs in carrier.index:
        b = carrier.loc[indexs].values[0:-1]
        c = ' '.join('%s' %id for id in b)
        a.append(c)
    return a

def get_EMS_name(EMS):
    EMS_name_list = []
    for i in EMS:
        EMS_name_dict = {}
#         deliveryman_EMS = re.findall('(\\d+)\\s(\\w+)\\s(\\d+)\\s.*(投递员姓名：\\w+);联系电话：(\\d+).*(签收人：\\w+)',i)
        EMS_name_dict["EMS_OrderId"] = str(re.findall("(\\d+)\sems",i)).replace("['","").replace("']","")
        EMS_name_dict["EMS_trackingID"] = str(re.findall("ems\s(\\d+)",i)).replace("['","").replace("']","")
        EMS_name_dict["EMS_deliveryman_name"] = str(re.findall("投递员姓名：(\\w+)",i)).replace("['","").replace("']","")
        EMS_name_dict["EMS_deliveryman_tel"] = str(re.findall("联系电话：(\\d+)",i)).replace("['","").replace("']","")
        EMS_name_dict["EMS_orderstatus"] = str(re.findall("签收人：(\\w+)",i)).replace("['","").replace("']","")
        # print(EMS_name_dict)
        EMS_name_list.append(EMS_name_dict)
    return EMS_name_list

if __name__ == "__main__":
    # 路径变量 (每次要改的地方)
    date = "201812"
    filename = "Dec_ems_2018_cha.csv"
    inputPath = "G:\\work\\logistica\\Dec_cha\\"
    outpath = "G:\\work\\logistica\\output\\"
    name_UTF8 = date + "_EMS_cha.csv"
    name_ANSI = date + "_EMS_cha.xlsx"

    # 读取数据
    data = pd.read_csv(inputPath + filename)

    # 数据清洗
    dayslist = get_del_list(40)
    df = data.copy().fillna("kong")
    df.drop(dayslist,axis=1, inplace=True)
    print(df["LOGISTICS_COMPANY"].value_counts())
    
    # 提取关键信息
    EMS = df[df["LOGISTICS_COMPANY"] == "ems"]
    EMS_list = get_carrier_list(EMS)
    EMS_name = get_EMS_name(EMS_list)
    print("EMS_name:" + str(len(EMS_name)))
    
    # 输出
    pd.DataFrame(EMS_name).to_excel(outpath + name_ANSI, sheet_name="EMS", index=False)
    pd.DataFrame(EMS_name).to_csv(outpath + name_UTF8, index=False)