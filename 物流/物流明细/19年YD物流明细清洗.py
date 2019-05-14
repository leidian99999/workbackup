import pandas as pd
import re

date = "1904"
carrier = "YD"

inputpath = "G:\\work\\logistica\\info\\input\\cha\\"+date+"cha\\"
inputname = date + "cha_"+carrier+".csv"
outpath = "G:\\work\\logistica\\info\\output\\CHA\\CSV\\"
outname1 = date+"_"+carrier+"_LS_cha"
outname2 = date+"_"+carrier+"_DM_cha"
outname3 = date+"_"+carrier+"_ST_cha"

df = pd.read_csv(inputpath + inputname,sep = None,encoding='utf8')

df1 = df[df["PARTNER_ACTION"] == "deliver"].reset_index(drop=True) # LS
df2 = df[df["PARTNER_ACTION"] == "deliver"].reset_index(drop=True) # DM
df3 = df[df["PARTNER_ACTION"] == "signed"].reset_index(drop=True) # ST

def get_YD19_lastStations(YD):
    YD_name_list = []
    for i in YD:
        YD_name_dict = {}
        YD_name_dict["YD_lastStation"] = str(re.findall("^(\\w+)\s【",i)).replace("['","").replace("']","")
        YD_name_list.append(YD_name_dict)
    return YD_name_list

def get_YD19_deliveryman(YD):
    YD_name_list = []
    for i in YD:
        YD_name_dict = {}
        YD_name_dict["YD_deliveryman_name"] = str(re.findall("派件员\s(\\w+)\s",i)).replace("['","").replace("']","")
        YD_name_dict["YD_deliveryman_tel"] = str(re.findall("(\\d+)\s正在",i)).replace("['","").replace("']","")
        YD_name_list.append(YD_name_dict)
    return YD_name_list

def get_YD19_status(YD):
    YD_name_list = []
    for i in YD:
        YD_name_dict = {}
        # if "签收人" in YD:
        YD_name_dict["YD_status"] = str(re.findall("快件已被\s(.*)。如有",i)).replace("['","").replace("']","")
        YD_name_list.append(YD_name_dict)
    return YD_name_list

data1 = pd.DataFrame(get_YD19_lastStations(df1["DESCRIPTION"]))
data2 = pd.DataFrame(get_YD19_deliveryman(df2["DESCRIPTION"]))
data3 = pd.DataFrame(get_YD19_status(df3["DESCRIPTION"]))
df_LS = pd.concat([df1,data1],axis=1)
df_DM = pd.concat([df2,data2],axis=1)
df_ST = pd.concat([df3,data3],axis=1)

print("df_LS:" + str(df_LS.shape))
print("df_DM:" + str(df_DM.shape))
print("df_ST:" + str(df_ST.shape))

df_LS.to_csv(outpath + outname1 + ".csv",index=False)
df_DM.to_csv(outpath + outname2 + ".csv",index=False)
df_ST.to_csv(outpath + outname3 + ".csv",index=False) 