import pandas as pd
import re

date = "1904"
carrier = "ZT"

inputpath = "G:\\work\\logistica\\info\\input\\cha\\"+date+"cha\\"
inputname = date + "cha_"+carrier+".csv"
outpath = "G:\\work\\logistica\\info\\output\\CHA\\CSV\\"
outname1 = date+"_"+carrier+"_LS_cha"
outname2 = date+"_"+carrier+"_DM_cha"
outname3 = date+"_"+carrier+"_ST_cha"

df = pd.read_csv(inputpath + inputname,sep = None,encoding='utf8')

df1 = df[df["PARTNER_ACTION"] == "派件"].reset_index(drop=True) #LS
df2 = df[df["PARTNER_ACTION"] == "派件"].reset_index(drop=True) #DM
df3 = df[df["PARTNER_ACTION"] == "签收"].reset_index(drop=True) #ST

def get_ZT19_lastStations(ZT):
    ZT_name_list = []
    for i in ZT:
        ZT_name_dict = {}
        ZT_name_dict["ZT_lastStation"] = str(re.findall("【(\\w+)】 的",i)).replace("['","").replace("']","")

        ZT_name_list.append(ZT_name_dict)
#         print(ZT_name_dict["ZT_lastStation"])
    return ZT_name_list

def get_ZT19_deliveryman(ZT):
    ZT_name_list = []
    for i in ZT:
        ZT_name_dict = {}
        ZT_name_dict["ZT_deliveryman_name"] = str(re.findall("】 的(\\w+)（",i)).replace("['","").replace("']","")
        ZT_name_dict["ZT_deliveryman_tel"] = str(re.findall("（(\\d+)）",i)).replace("['","").replace("']","")

        ZT_name_list.append(ZT_name_dict)
#         print(ZT_name_dict["ZT_lastStation"])
    return ZT_name_list

def get_ZT19_status(ZT):
    ZT_name_list = []
    for i in ZT:
        ZT_name_dict = {}
        # if "签收人" in ZT:
        ZT_name_dict["ZT_status"] = str(re.findall("签收人: (\\w+),",i)).replace("['","").replace("']","")
        ZT_name_list.append(ZT_name_dict)
#         else:
#             ZT_name_dict["ZT_status"] = "自提点"
# #         print(ZT_name_dict["ZT_lastStation"])
    return ZT_name_list

data1 = pd.DataFrame(get_ZT19_lastStations(df1["DESCRIPTION"]))
data2 = pd.DataFrame(get_ZT19_deliveryman(df2["DESCRIPTION"]))
data3 = pd.DataFrame(get_ZT19_status(df3["DESCRIPTION"]))

df_LS = pd.concat([df1,data1],axis=1)
df_DM = pd.concat([df2,data2],axis=1)
df_ST = pd.concat([df3,data3],axis=1)
print("df_LS:" + str(df_LS.shape))
print("df_DM:" + str(df_DM.shape))
print("df_ST:" + str(df_ST.shape))

df_LS.to_csv(outpath + outname1 + ".csv",index=False)
df_DM.to_csv(outpath + outname2 + ".csv",index=False)
df_ST.to_csv(outpath + outname3 + ".csv",index=False)

df_LS.to_csv(outpath + outname1 + ".csv",index=False)
df_DM.to_csv(outpath + outname2 + ".csv",index=False)
df_ST.to_csv(outpath + outname3 + ".csv",index=False)