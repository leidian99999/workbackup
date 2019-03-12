import pandas as pd
import json
from urllib.request import urlopen, quote,URLError, HTTPError
import requests
import time

# 输入
data = pd.read_excel(r"G:\work\logistica\stations\JDStations\stations\website\JDstations_zhejiang_JD.xlsx")
data_city = pd.read_excel(r"G:\work\logistica\stations\JDStations\stations\zhejiangcityID.xlsx")
province = "浙江省"

# 输出
outpath = r"G:\work\logistica\stations\JDStations\stations\gaode\\"
name_ANSI = "JDstations_zhejiang_gaode_test1.xlsx"

df = pd.merge(data,data_city,how="left",on="cityId")


def getlatlng_Gaode2(address):
    ak='c71d9eda293d20db64955275557d92d4'
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
#     contest=contest['geocodes'][0]['location']
    return contest

df["siteAddress_all"] = province + df['cityname'] + df['siteAddress']

start_time = time.time()
listA = []
for b in df['siteAddress_all']:
    print(b)
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

df_A = pd.DataFrame(listA) # 转dataframe

df_all = pd.concat([df,df_A],axis=1)
df_all = df_all.drop(columns=['siteLatitude','siteLongitude'])

split = pd.DataFrame((x.split(',') for x in df_all['siteLocation_gaode']), index=df_all.index, columns=['site_Lng_gaode','site_Lat_gaode'])
df_all = pd.merge(df_all,split,left_index=True,right_index=True)

# 整理检查
print(data.shape)
print(df.shape)
print(df_A.shape)
print(df_all.shape)
print(df_allA.shape)

df_allA.to_excel(outpath + name_ANSI,index=False)