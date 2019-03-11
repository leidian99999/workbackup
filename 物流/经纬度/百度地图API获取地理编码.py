import pandas as pd
import json
from urllib.request import urlopen, quote,URLError, HTTPError
import requests
import time

data = pd.read_excel(r"D:\work\logistica\stations\JDStations\stations\website\XLSX\JDstations_zhejiang.xlsx")
data_city = pd.read_excel(r"D:\work\logistica\stations\JDStations\zhejiangcityID.xlsx")
province = "浙江省"
print("读取表格")
outpath = "D:\\work\\logistica\\stations\\JDStations\\stations\\"
# name_UTF8 = "JDstations_zhejiang_baidu.csv"
name_ANSI = "JDstations_zhejiang_baidu.xlsx"

print(data.columns)
print("*"*30)
print(data_city.columns)

df = pd.merge(data,data_city,how="left",on="cityId")

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'#输出数据的格式	
    ak = 'z3KEtliyTGvj0bFudEkz4GO0GN8eQQa5'
    add = quote(address) #由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak 
    req = urlopen(uri)
    res = req.read().decode() 
    temp = json.loads(res)
    return temp

print("地址去空前：{}".format(df['siteAddress'].isnull().value_counts()))
df = df.dropna(subset=["siteAddress"])
print("地址去空后：{}".format(df['siteAddress'].isnull().value_counts()))

df["siteAddress_all"] = province+ df['cityName'] + df['siteAddress']

start_time = time.time()
listA = []
for b in df['siteAddress_all']:
#     print(b)
    dictA = {}
    try:
        temp = getlnglat(b)
    except HTTPError as e:
        print("请求出错")
        pass
    else:    
        if ('result' in temp):
            dictA["siteLongitude_baidu"] = temp['result']['location']['lng']
            dictA["siteLatitude_baidu"] = temp['result']['location']['lat']
            dictA["sitePrecise_baidu"] = temp['result']['precise']
            dictA["siteConfidence_baidu"] = temp['result']['confidence']
            dictA["siteComprehension_baidu"] = temp['result']['comprehension']
            dictA["siteLevel_baidu"] = temp['result']['level']
        else:
            pass
    listA.append(dictA)
#     time.sleep(1)
end_time = time.time()
print("总用时：",end_time-start_time)

df_A = pd.DataFrame(listA)

df_all = pd.concat([df,df_A],axis=1,join_axes=[df.index])

print("data:{}行".format(data.shape[0]))
print("df:{}行".format(df.shape[0]))
print("df_A:{}行".format(df_A.shape[0]))
print("df_all:{}行".format(df_all.shape[0]))

df_all.to_excel(outpath + name_ANSI)