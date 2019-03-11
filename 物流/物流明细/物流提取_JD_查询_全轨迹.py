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

def get_JD_name(JD):
    JD_name_list = []
    for i in JD:
        JD_name_dict = {}
        #deliveryman_JD = re.findall('(\\d+)\\s(\\w+)\\s(\\w+).*配送员，(\\w+)，手机号，(\\d+).*(货物已由\\w+|货物已\\w+)',i)
        #JD_name_dict["JD_OrderId"] = str(re.findall("(\\d+)\\sjingdongwuliu",i))        

        JD_name_dict["JD_OrderId"] = str(re.findall("(\\d+)\\sjingdongwuliu",i)).replace("['","").replace("']","")
        JD_name_dict["JD_trackingID"] = str(re.findall("jingdongwuliu\\s(\\w+)",i)).replace("['","").replace("']","")
        JD_name_dict["JD_deliveryman_name"] = str(re.findall("配送员\，(\\w+)\，手机号\，\\d+\s货物已",i)).replace("['","").replace("']","")
        JD_name_dict["JD_deliveryman_tel"] = str(re.findall("配送员\，\\w+\，手机号\，(\\d+)\s货物已",i)).replace("['","").replace("']","")
        JD_name_dict["JD_orderstatus"] = str(re.findall("\\d+\s(货物已由\\w+|货物已\\w+)，感谢您选择京东物流！",i)).replace("['","").replace("']","")
        JD_name_dict["JD_LastStation"] = str(re.findall("\【(\\w+)\】\s货物已分配\，等待配送",i)).replace("['","").replace("']","")
        # JD_name_dict["JD_LastStation"] = str(re.findall("【(.+?)】",i)).replace("['","").replace("']","")
        JD_name_list.append(JD_name_dict)
        # print(JD_name_dict["JD_LastStation"])
    return JD_name_list

if __name__ == "__main__":
    # 路径变量 (每次要改的地方)
    date = "201812"
    filename = "Dec_JDSF_cha.csv"
    inputPath = "G:\\work\\logistica\\input\\Dec_cha\\"
    outpath = "G:\\work\\logistica\\output\\"
    name_UTF8 = date + "_JD_cha.csv"
    name_ANSI = date + "_JD_cha.xlsx"

    # 读取数据
    data = pd.read_csv(inputPath + filename)

    # 数据清洗
    dayslist = get_del_list(40)
    df = data.copy().fillna("kong")
    df.drop(dayslist,axis=1, inplace=True)
    print(df["LOGISTICS_COMPANY"].value_counts())
    
    # 提取关键信息
    JD = df[df["LOGISTICS_COMPANY"] == "jingdongwuliu"]
    JD_list = get_carrier_list(JD)
    JD_name = get_JD_name(JD_list)
    print("JD_name:" + str(len(JD_name)))
    
    # 输出
    pd.DataFrame(JD_name).to_excel(outpath + name_ANSI, sheet_name="京东", index=False)
    pd.DataFrame(JD_name).to_csv(outpath + name_UTF8, index=False)