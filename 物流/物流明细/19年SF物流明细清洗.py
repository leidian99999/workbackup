import pandas as pd
import re

date = "1904"
carrier = "SF"

inputpath = "G:\\work\\logistica\\info\\input\\cha\\"+date+"cha\\"
inputname = date + "cha_"+carrier+".csv"
outpath = "G:\\work\\logistica\\info\\output\\CHA\\CSV\\"
outname1 = date+"_"+carrier+"_LS_cha"
outname2 = date+"_"+carrier+"_DM_cha"
outname3 = date+"_"+carrier+"_ST_cha"

df = pd.read_csv(inputpath + inputname,sep = None,encoding='utf8')

df1 = df[df["PARTNER_ACTION"] == 31].reset_index(drop=True) #LS
df2 = df[df["PARTNER_ACTION"] == 44].reset_index(drop=True) #DM
df3 = df[df["PARTNER_ACTION"] == 80].reset_index(drop=True) #ST1
df4 = df[df["PARTNER_ACTION"] == 125].reset_index(drop=True) # ST2

print("df1:" + str(df1.shape))
print("df2:" + str(df2.shape))
print("df3:" + str(df3.shape))
print("df4:" + str(df4.shape))

print("*"*50)

def get_SF19_lastStations(SF):
    SF_name_list = []
    for i in SF:
        SF_name_dict = {}
        SF_name_dict["SF_lastStation"] = str(re.findall("快件到达 【(\\w+)】",i)).replace("['","").replace("']","")

        SF_name_list.append(SF_name_dict)
#         print(ems_name_dict["ems_lastStation"])
    return SF_name_list

def get_SF19_deliveryman(SF):
    SF_name_list = []
    for i in SF:
        SF_name_dict = {}
        SF_name_dict["SF_deliveryman_name"] = str(re.findall("派件人:(\\w+)",i)).replace("['","").replace("']","")
        SF_name_dict["SF_deliveryman_tel"] = str(re.findall("电话:(\\d+)",i)).replace("['","").replace("']","")

        SF_name_list.append(SF_name_dict)
#         print(JD_name_dict["JD_lastStation"])
    return SF_name_list

def get_SF19_status1(SF):
    SF_name_list = []
    for i in SF:
        SF_name_dict = {}
        SF_name_dict["SF_status"] = str(re.findall("(\\w+),感谢使用顺丰,期待再次为您服务",i)).replace("['","").replace("']","")
        SF_name_list.append(SF_name_dict)
#         print(JD_name_dict["JD_lastStation"])
    return SF_name_list

def get_SF19_status2(SF):
    SF_name_list = []
    for i in SF:
        SF_name_dict = {}
        SF_name_dict["SF_status"] = str(re.findall("快件派送至【(\\w+)】,",i)).replace("['","").replace("']","")
        SF_name_list.append(SF_name_dict)
#         print(JD_name_dict["JD_lastStation"])
    return SF_name_list

data1 = pd.DataFrame(get_SF19_lastStations(df1["DESCRIPTION"]))
data2 = pd.DataFrame(get_SF19_deliveryman(df2["DESCRIPTION"]))
data3 = pd.DataFrame(get_SF19_status1(df3["DESCRIPTION"]))
data4 = pd.DataFrame(get_SF19_status2(df4["DESCRIPTION"]))

df_LS = pd.concat([df1,data1],axis=1)
df_DM = pd.concat([df2,data2],axis=1)
df_ST1 = pd.concat([df3,data3],axis=1)
df_ST2 = pd.concat([df4,data4],axis=1)
df_ST = pd.concat([df_ST1,df_ST2],axis=0)

print("df_LS:" + str(df_LS.shape))
print("df_DM:" + str(df_DM.shape))
print("df_ST1:" + str(df_ST1.shape))
print("df_ST2:" + str(df_ST2.shape))
print("df_ST:" + str(df_ST.shape))

df_LS.to_csv(outpath + outname1 + ".csv",index=False)
df_DM.to_csv(outpath + outname2 + ".csv",index=False)
df_ST.to_csv(outpath + outname3 + ".csv",index=False)