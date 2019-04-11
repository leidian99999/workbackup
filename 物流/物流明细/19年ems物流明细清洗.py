import pandas as pd
import re

'''
JDXX:jingdongxianxia
JDWL:jingdongwuliu

'''


date = "1903"
carrier = "ems"

inputpath = "G:\\work\\logistica\\info\\input\\cha\\"+date+"cha\\"
inputname = date + "cha_"+carrier+".csv"
outpath = "G:\\work\\logistica\\info\\output\\CHA\\CSV\\"
outname1 = "20"+date+"_"+carrier+"_LS_cha"
outname2 = "20"+date+"_"+carrier+"_DM_cha"
outname3 = "20"+date+"_"+carrier+"_ST_cha"

df = pd.read_csv(inputpath + inputname,sep = None,encoding='utf8')

df1 = df[df["PARTNER_ACTION"] == 50].reset_index(drop=True)
df2 = df[df["PARTNER_ACTION"] == 50].reset_index(drop=True)
df3 = df[df["PARTNER_ACTION"] == 10].reset_index(drop=True)

def get_ems19_lastStations(ems):
    ems_name_list = []
    for i in ems:
        ems_name_dict = {}
        ems_name_dict["ems_lastStation"] = str(re.findall("(\\w+)安排投递",i)).replace("['","").replace("']","")

        ems_name_list.append(ems_name_dict)
#         print(ems_name_dict["ems_lastStation"])
    return ems_name_list

def get_ems19_deliveryman(ems):
    ems_name_list = []
    for i in ems:
        ems_name_dict = {}
        ems_name_dict["ems_deliveryman_name"] = str(re.findall("投递员姓名：(\\w+);",i)).replace("['","").replace("']","")
        ems_name_dict["ems_deliveryman_tel"] = str(re.findall("联系电话：(\\d+)",i)).replace("['","").replace("']","")

        ems_name_list.append(ems_name_dict)
#         print(ems_name_dict["ems_lastStation"])
    return ems_name_list

def get_ems19_status(ems):
    ems_name_list = []
    for i in ems:
        ems_name_dict = {}
        # if "签收人" in ems:
        ems_name_dict["ems_status"] = str(re.findall("签收人：(\\w+)",i)).replace("['","").replace("']","")
        ems_name_list.append(ems_name_dict)
#         else:
#             ems_name_dict["ems_status"] = "自提点"
# #         print(ems_name_dict["ems_lastStation"])
    return ems_name_list

data1 = pd.DataFrame(get_ems19_lastStations(df1["DESCRIPTION"]))
data2 = pd.DataFrame(get_ems19_deliveryman(df2["DESCRIPTION"]))
data3 = pd.DataFrame(get_ems19_status(df3["DESCRIPTION"]))
df_LS = pd.concat([df1,data1],axis=1)
df_DM = pd.concat([df2,data2],axis=1)
df_ST = pd.concat([df3,data3],axis=1)
df_LS.to_csv(outpath + outname1 + ".csv",index=False)
df_DM.to_csv(outpath + outname2 + ".csv",index=False)
df_ST.to_csv(outpath + outname3 + ".csv",index=False)