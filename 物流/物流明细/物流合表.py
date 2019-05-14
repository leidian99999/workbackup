import pandas as pd


inputpath = "G:/work/logistica/info/output/CHA/CSV/"
outpath = "G:/work/logistica/info/output/CHA/all/"
pinyin = "JDXX"
date = "1903"

data_DM = pd.read_csv(inputpath + "20"+date+"_"+pinyin+"_DM_cha.csv")
data_LS = pd.read_csv(inputpath + "20"+date+"_"+pinyin+"_LS_cha.csv")
data_ST = pd.read_csv(inputpath + "20"+date+"_"+pinyin+"_ST_cha.csv")
print("data_DM:"+str(data_DM.shape))
print("data_LS:"+str(data_LS.shape))
print("data_ST:"+str(data_ST.shape))

df_DM = data_DM.drop_duplicates(subset=['MAIL_NO'],keep='last')
df_LS = data_LS.drop_duplicates(subset=['MAIL_NO'],keep='last')
df_ST = data_ST.drop_duplicates(subset=['MAIL_NO'],keep='last')

print("df_DM:"+str(df_DM.shape))
print("df_LS:"+str(df_LS.shape))
print("df_ST:"+str(df_ST.shape))

df = pd.merge(
    pd.merge(
        df_DM[['﻿"ORDER_ID"','MAIL_NO','ROUTE_TIME','JD_deliveryman_name','JD_deliveryman_tel','ROUTE_TIME']],
        df_LS[['MAIL_NO','LOGISTICS_COMPANY','JD_lastStation']],
        how="inner",on='MAIL_NO'
    ),
    df_ST[['MAIL_NO','JD_status']],how='inner',on='MAIL_NO')
print("df:"+str(df.shape))

df.to_excel(outpath+date+'_'+pinyin+'.xlsx',index=False)

print("完成：" + str(df.duplicated().value_counts()))