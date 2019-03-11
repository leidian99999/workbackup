import pandas as pd
import json
from urllib.request import urlopen, quote,URLError, HTTPError
import requests
import time



data = pd.read_excel(r"D:\work\logistica\stations\JDStations\stations\website\XLSX\JDstations_sichuan.xlsx")
data_city = pd.read_excel(r"D:\work\logistica\stations\JDStations\sichuancityID.xlsx")
province = "四川省"
outpath = "D:\\work\\logistica\\stations\\JDStations\\stations\\"
name_ANSI = "JDstations_sichuan_gaode.xlsx"


print(data.columns)
print("*"*30)
print(data_city.columns)

df = data.copy()
df = pd.merge(data,data_city,how="left",on="cityId")

def getlatlng_Gaode2(address):
    ak='1c2682317206ccaa18ec2487bb45d880'
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
#     contest=contest['geocodes'][0]['location']
    return contest

print(df['siteAddress'].isnull().value_counts())
df = df.dropna(subset=["siteAddress"])
print(df['siteAddress'].isnull().value_counts())


df["siteAddress_all"] = province + df['cityName'] + df['siteAddress']

start_time = time.time()
listA = []
for b in df['siteAddress_all']:
    # print(b)
    dictA = {}
    try:
        temp=getlatlng_Gaode2(b)
    except HTTPError as e:
        print("请求出错")
        pass
    else:    
        if ('geocodes' in temp):
            dictA["siteLocation_gaode"] = temp['geocodes'][0]['location']
            dictA["siteFormatted_address_gaode"] = temp['geocodes'][0]['formatted_address']
            dictA["siteProvince_gaode"] = temp['geocodes'][0]['province']
            dictA["siteCountry_gaode"] = temp['geocodes'][0]['country']
            if ('citycode' in temp):
                dictA["siteCitycode_gaode"] = temp['geocodes'][0]['citycode']
            else:
                pass
            dictA["siteCity_gaode"] = temp['geocodes'][0]['city']
            dictA["siteDistrict_gaode"] = temp['geocodes'][0]['district']
            dictA["siteLevel_gaode"] = temp['geocodes'][0]['level']
            dictA["siteTownship_gaode"] = temp['geocodes'][0]['township']
            dictA["siteAdcode_gaode"] = temp['geocodes'][0]['adcode']
            dictA["siteStreet_gaode"] = temp['geocodes'][0]['street']
            dictA["siteNumber_gaode"] = temp['geocodes'][0]['number']
        else:
            pass
    listA.append(dictA)
#     time.sleep(1)
end_time = time.time()
print("总用时：",end_time-start_time)

df_A = pd.DataFrame(listA)
df_all = pd.concat([df,df_A],axis=1,join_axes=[df.index])

print(df.shape)
print(df_A.shape)
print(df_all.shape)

df_all = df_all.drop(columns=['siteLatitude','siteLongitude'])
df_all['siteLocation_gaode'] = df_all['siteLocation_gaode'].map(lambda x:str(x))
split = pd.DataFrame((x.split(',') for x in df_all['siteLocation_gaode']), index=df_all.index, columns=['siteLatitude_gaode','siteLongitude_gaode'])
df_allA = pd.merge(df_all,split,left_index=True,right_index=True)
df_allA.to_excel(outpath + name_ANSI)

