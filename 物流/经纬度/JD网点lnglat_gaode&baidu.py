import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlopen, quote,URLError, HTTPError
import time

inputpath_urls = "G:\\work\\logistica\\stations\\JDStations\\yuanURL\\浙江/浙江.xlsx"
inputpath_citys = "G:\\work\\logistica\\stations\\JDStations\\stations\\zhejiangcityID.xlsx"

# 导入数据
df = pd.read_excel(inputpath_urls)
data_city = pd.read_excel(inputpath_citys)
province = "浙江省"

# ak码
ak_gaode='c71d9eda293d20db64955275557d92d4'

# 导出数据路径
outpath_JD = "G:\\work\\logistica\\stations\\JDStations\\stations\\website\\"
outpath_gaode = "G:\\work\\logistica\\stations\\JDStations\\stations\\gaode\\"
name_ANSI_JD = "JDstations_zhejiang_JD_test.xlsx"
name_ANSI_gaode = "JDstations_zhejiang_gaode_test.xlsx"

# 建立url池
urls = []
for a in df["url"]:
    urls.append("http://www.jdwl.com/site/querySiteList?" + a)

print("验证完整地址：")
print(urls[0:3])

# 遍历获取JD官网网点信息
def get_JD_siteInfo(urls):
    JD_siteList = []
    for url in urls:
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "lxml").get_text()
        jsonlist = json.loads(soup)
        for i in range(len(jsonlist)):
            JD_siteDict = {}
            JD_siteDict["JD_siteBusinessName"] = jsonlist[i]["siteBusinessName"]
            JD_siteDict["JD_siteProvinceId"] = jsonlist[i]["provinceId"]
            JD_siteDict["JD_siteCityId"] = jsonlist[i]["cityId"]
            JD_siteDict["JD_siteCountyId"] = jsonlist[i]["countyId"]
            JD_siteDict["siteName"] = jsonlist[i]["siteName"]
            if 'address' in jsonlist[i]:
                JD_siteDict["JD_siteAddress"] = jsonlist[i]["address"]
            else:
                pass
            if 'latitude' in jsonlist[i]:
                JD_siteDict["JD_siteLatitude"] = jsonlist[i]['latitude']
            else:
                pass  
            if 'longitude' in jsonlist[i]:
                JD_siteDict["JD_siteLongitude"] = jsonlist[i]['longitude']
            else:
                pass       
            if "telephone" in jsonlist[i]:
                JD_siteDict["JD_siteTelephone"] = jsonlist[i]["telephone"]
            else:
                pass
            JD_siteList.append(JD_siteDict)
    return JD_siteList

# 获取高德地图API地址信息
def get_latlng_Gaode(address,ak):
    ak = ak_gaode
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
    return contest

def get_JD_siteInfo_gaode(urls):
    start_time = time.time()
    JD_siteList_gaode = []
    for b in urls:
        # print(b)
        JD_siteDict_gaode = {}
        try:
            temp=get_latlng_Gaode(b)
        except HTTPError as e:
            print("请求出错")
            pass
        else:
            if ('geocodes' in temp):
                JD_siteDict_gaode["JD_siteLocation_gaode"] = temp['geocodes'][0]['location']
                JD_siteDict_gaode["JD_siteFormatted_address_gaode"] = temp['geocodes'][0]['formatted_address']
                JD_siteDict_gaode["JD_siteProvince_gaode"] = temp['geocodes'][0]['province']
                JD_siteDict_gaode["JD_siteCountry_gaode"] = temp['geocodes'][0]['country']
                if ('citycode' in temp):
                    JD_siteDict_gaode["JD_siteCitycode_gaode"] = temp['geocodes'][0]['citycode']
                else:
                    pass
                JD_siteDict_gaode["JD_siteCity_gaode"] = temp['geocodes'][0]['city']
                JD_siteDict_gaode["JD_siteDistrict_gaode"] = temp['geocodes'][0]['district']
                JD_siteDict_gaode["JD_siteLevel_gaode"] = temp['geocodes'][0]['level']
                JD_siteDict_gaode["JD_siteTownship_gaode"] = temp['geocodes'][0]['township']
                JD_siteDict_gaode["JD_siteAdcode_gaode"] = temp['geocodes'][0]['adcode']
                JD_siteDict_gaode["JD_siteStreet_gaode"] = temp['geocodes'][0]['street']
                JD_siteDict_gaode["JD_siteNumber_gaode"] = temp['geocodes'][0]['number']
            else:
                pass
        JD_siteList_gaode.append(JD_siteDict_gaode)
    #     time.sleep(1)
    end_time = time.time()
    print("总用时：",end_time-start_time)
    return JD_siteList_gaode




'''
获取京东官网网点信息
'''
df_JD_siteInfo = pd.DataFrame(get_JD_siteInfo(urls))
# 去除空白地址所在行
print(df_JD_siteInfo['JD_siteAddress'].isnull().value_counts())
df_JD_siteInfo = df_JD_siteInfo.dropna(subset=["JD_siteAddress"])
print(df_JD_siteInfo['JD_siteAddress'].isnull().value_counts())
print("*"*50)
print("查看JD网店及对应城市列名：")
print(df_JD_siteInfo.columns)
print("$"*30)
print(data_city.columns)
print("*"*50)



'''
获取京东高德网点信息
'''
df["JD_siteAddress_all"] = province + df['cityname'] + df['JD_siteAddress']
print("验证完整地址：")
print(df["siteAddress_all"][0:3])
print("*"*50)
df_JD_siteList_gaode = pd.DataFrame(get_JD_siteInfo(urls))
# 合并并清洗
df_JD_siteInfo_gaode = pd.concat([df_JD_siteList_gaode,df_JD_siteInfo],axis=1)
df_JD_siteInfo_gaode = df_JD_siteInfo_gaode.drop(columns=['JD_siteLongitude','JD_siteLatitude'])
split_gaode = pd.DataFrame((x.split(',') for x in df_JD_siteInfo_gaode['JD_siteLocation_gaode']), index=df_JD_siteInfo_gaode.index, columns=['JD_siteLng_gaode','JD_siteLat_gaode'])
df_JD_siteInfo_gaode = pd.merge(df_JD_siteInfo_gaode,split_gaode,left_index=True,right_index=True)

# 最后检查
print("JD官网网点信息：" + str(df_JD_siteInfo.shape))
print("合并之前：" + str(df_JD_siteList_gaode.shape))
print("JD网点高德信息：" + str(df_JD_siteInfo_gaode.shape))
print("*"*50)

# 输出
df_JD_siteInfo.to_excel(outpath_JD + name_ANSI_JD,index=False)
df_JD_siteInfo_gaode.to_excel(outpath_gaode + name_ANSI_gaode,index=False)




