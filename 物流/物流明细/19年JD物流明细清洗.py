import pandas as pd
import re

'''
JDXX:jingdongxianxia
JDWL:jingdongwuliu

'''


date = "1903"
carrier = "JDWL"

inputpath = "G:\\work\\logistica\\info\\input\\cha\\"+date+"cha\\"
inputname = date + "cha_"+carrier+".csv"
outpath = "G:\\work\\logistica\\info\\output\\CHA\\CSV\\"
outname1 = "20"+date+"_"+carrier+"_LS_cha"
outname2 = "20"+date+"_"+carrier+"_DM_cha"
outname3 = "20"+date+"_"+carrier+"_ST_cha"

df = pd.read_csv(inputpath + inputname,sep = None,encoding='utf8')

df1 = df[df["PARTNER_ACTION"] == "站点收货"].reset_index(drop=True)
df2 = df[df["PARTNER_ACTION"] == "配送员收货"].reset_index(drop=True)
df3 = df[df["PARTNER_ACTION"] == "妥投"].reset_index(drop=True)

def get_JD19_lastStations(JD):
    JD_name_list = []
    for i in JD:
        JD_name_dict = {}
        JD_name_dict["JD_lastStation"] = str(re.findall("货物已到达【(\\w+)】",i)).replace("['","").replace("']","")

        JD_name_list.append(JD_name_dict)
#         print(JD_name_dict["JD_lastStation"])
    return JD_name_list

def get_JD19_deliveryman(JD):
    JD_name_list = []
    for i in JD:
        JD_name_dict = {}
        JD_name_dict["JD_deliveryman_name"] = str(re.findall("配送员，(\\w+)",i)).replace("['","").replace("']","")
        JD_name_dict["JD_deliveryman_tel"] = str(re.findall("手机号，(\\d+)",i)).replace("['","").replace("']","")

        JD_name_list.append(JD_name_dict)
#         print(JD_name_dict["JD_lastStation"])
    return JD_name_list

def get_JD19_status(JD):
    JD_name_list = []
    for i in JD:
        JD_name_dict = {}
        JD_name_dict["JD_status"] = str(re.findall("货物已(\\w+)，",i)).replace("['","").replace("']","")
        JD_name_list.append(JD_name_dict)
#         print(JD_name_dict["JD_lastStation"])
    return JD_name_list

data1 = pd.DataFrame(get_JD19_lastStations(df1["DESCRIPTION"]))
data2 = pd.DataFrame(get_JD19_deliveryman(df2["DESCRIPTION"]))
data3 = pd.DataFrame(get_JD19_status(df3["DESCRIPTION"]))
df_LS = pd.concat([df1,data1],axis=1)
df_DM = pd.concat([df2,data2],axis=1)
df_ST = pd.concat([df3,data3],axis=1)
df_LS.to_csv(outpath + outname1 + ".csv",index=False)
df_DM.to_csv(outpath + outname2 + ".csv",index=False)
df_ST.to_csv(outpath + outname3 + ".csv",index=False)