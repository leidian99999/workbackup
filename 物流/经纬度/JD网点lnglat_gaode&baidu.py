import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlopen, quote,URLError, HTTPError
import time
from sqlalchemy import create_engine
import pymysql

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
            JD_siteDict["JD_siteName"] = jsonlist[i]["siteName"]
            if 'address' in jsonlist[i]:
                JD_siteDict["JD_siteAddress"] = jsonlist[i]["address"]
            else:
                pass
            if 'latitude' in jsonlist[i]:
                JD_siteDict["JD_siteLat"] = jsonlist[i]['latitude']
            else:
                pass  
            if 'longitude' in jsonlist[i]:
                JD_siteDict["JD_siteLng"] = jsonlist[i]['longitude']
            else:
                pass       
            if "telephone" in jsonlist[i]:
                JD_siteDict["JD_siteTelephone"] = jsonlist[i]["telephone"]
            else:
                pass
            JD_siteList.append(JD_siteDict)
    return JD_siteList

# 解析高德地图API网址信息
def get_json_gaode(address,ak):
    ak = ak_gaode
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
    return contest


# 获取高德地图API地址信息
def get_JD_siteInfo_gaode(address):
    print("开始获取高德地址信息")
    start_time = time.time()
    JD_siteList_gaode = []
    for b in address:
        print(b)
        JD_siteDict_gaode = {}
        try:
            temp=get_json_gaode(b,ak_gaode)
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
    print("高德总用时：",end_time-start_time)
    return JD_siteList_gaode

# 解析百度地图API网址信息
def get_json_baidu(address,ak):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'#输出数据的格式
    ak = ak_baidu
    add = quote(address) #由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    return temp


# 获取百度地图API地址信息
def get_JD_siteInfo_baidu(address):
    print("开始获取百度地址信息")
    start_time = time.time()
    JD_siteList_baidu = []
    for b in address:
        print(b)
        JD_siteDict_baidu = {}
        try:
            temp = get_json_baidu(b,ak_baidu)
        except HTTPError as e:
            print("请求出错")
            pass
        else:
            if ('result' in temp):
                JD_siteDict_baidu["JD_siteLng_baidu"] = temp['result']['location']['lng']
                JD_siteDict_baidu["JD_siteLat_baidu"] = temp['result']['location']['lat']
                JD_siteDict_baidu["JD_sitePrecise_baidu"] = temp['result']['precise']
                JD_siteDict_baidu["JD_siteConfidence_baidu"] = temp['result']['confidence']
                JD_siteDict_baidu["JD_siteComprehension_baidu"] = temp['result']['comprehension']
                JD_siteDict_baidu["JD_siteLevel_baidu"] = temp['result']['level']
            else:
                pass
        JD_siteList_baidu.append(JD_siteDict_baidu)
    #     time.sleep(1)
    end_time = time.time()
    print("百度总用时：",end_time-start_time)
    return JD_siteList_baidu


if __name__ == "__main__":
    province = "广东省"
    pinyin = "guangdong"

    inputpath_urls = "G:\\work\\logistica\\stations\\JDStations\\yuanURL\\yuanURL_" + pinyin + ".xlsx"
    inputpath_citys = "G:\\work\\logistica\\stations\\JDStations\\cityId\\" + pinyin + "CityID.xlsx"

    # 导入数据
    df = pd.read_excel(inputpath_urls)
    data_city = pd.read_excel(inputpath_citys)


    # ak码
    ak_gaode = 'c71d9eda293d20db64955275557d92d4'
    ak_baidu = 'z3KEtliyTGvj0bFudEkz4GO0GN8eQQa5'

    # 导出数据路径
    outpath_JD = "G:\\work\\logistica\\stations\\JDStations\\stations\\website\\"
    name_ANSI_JD = "JDstations_" + pinyin + "_JD.xlsx"

    outpath_gaode = "G:\\work\\logistica\\stations\\JDStations\\stations\\gaode\\"
    name_ANSI_gaode = "JDstations_" + pinyin + "_gaode.xlsx"
    name_UTF8_gaode = "JDstations_" + pinyin + "_gaode.csv"
    outpath_baidu = "G:\\work\\logistica\\stations\\JDStations\\stations\\baidu\\"
    name_ANSI_baidu = "JDstations_" + pinyin + "_baidu.xlsx"
    name_UTF8_baidu = "JDstations_" + pinyin + "_baidu.csv"
    # 建立url池
    urls = []
    for a in df["url"]:
        urls.append("http://www.jdwl.com/site/querySiteList?" + a)
    print("验证完整URL地址：")
    print(urls[0:3])

    # 获取京东官网网点信息
    df_JD_siteInfo = pd.DataFrame(get_JD_siteInfo(urls))

    # 去除空白地址所在行
    print("去除空白地址前：")
    print(df_JD_siteInfo['JD_siteAddress'].isnull().value_counts())
    df_JD_siteInfo = df_JD_siteInfo.dropna(subset=["JD_siteAddress"])
    print("去除空白地址后：")
    print(df_JD_siteInfo['JD_siteAddress'].isnull().value_counts())
    print("*"*50)
    print("查看JD网店及对应城市列名：")
    print(df_JD_siteInfo.columns)
    print("$"*30)
    print(data_city.columns)
    print("*"*50)

    # data_city['cityId'] = data_city['cityId'].map(lambda x:str(x))
    # df_JD_siteInfo["JD_siteCityId"] = df_JD_siteInfo["JD_siteCityId"].map(lambda x:str(x))
    df_JD_siteInfo = pd.merge(df_JD_siteInfo,data_city,how="left",left_on="JD_siteCityId",right_on="cityId")
    df_JD_siteInfo.rename(columns={'cityName': 'JD_cityName'}, inplace=True)

    df_JD_siteInfo["JD_siteAddress_all"] = province + df_JD_siteInfo['JD_cityName'] + df_JD_siteInfo['JD_siteAddress']
    print("验证完整收货地址：")
    print(df_JD_siteInfo["JD_siteAddress_all"][0:3])
    print("&%"*50)

    # 获取京东高德网点信息
    df_JD_siteList_gaode = pd.DataFrame(get_JD_siteInfo_gaode(df_JD_siteInfo["JD_siteAddress_all"]))
    # 合并并清洗
    df_JD_siteInfo_gaode = pd.concat([df_JD_siteList_gaode,df_JD_siteInfo],axis=1)
    df_JD_siteInfo_gaode = df_JD_siteInfo_gaode.drop(columns=['JD_siteLng','JD_siteLat'])
    split_gaode = pd.DataFrame((x.split(',') for x in df_JD_siteInfo_gaode['JD_siteLocation_gaode']), index=df_JD_siteInfo_gaode.index, columns=['JD_siteLng_gaode','JD_siteLat_gaode'])
    df_JD_siteInfo_gaode = pd.merge(df_JD_siteInfo_gaode,split_gaode,left_index=True,right_index=True)


    # 获取京东百度网点信息
    df_JD_siteList_baidu = pd.DataFrame(get_JD_siteInfo_baidu(df_JD_siteInfo["JD_siteAddress_all"]))
    df_JD_siteInfo_baidu = pd.concat([df_JD_siteList_baidu,df_JD_siteInfo],axis=1)
    df_JD_siteInfo_baidu = df_JD_siteInfo_baidu.drop(columns=['JD_siteLng','JD_siteLat'])


    # 最后检查
    print("JD官网网点信息：" + str(df_JD_siteInfo.shape))
    print("$"*30)
    print("高德合并之前：" + str(df_JD_siteList_gaode.shape))
    print("$"*30)
    print("JD网点高德信息：" + str(df_JD_siteInfo_gaode.shape))
    print("*"*30)
    print("百度合并之前：" + str(df_JD_siteList_baidu.shape))
    print("*"*30)
    print("JD网点百度信息：" + str(df_JD_siteInfo_gaode.shape))
    print("$"*50)

    # 输出
    df_JD_siteInfo.to_excel(outpath_JD + name_ANSI_JD,index=False)
    df_JD_siteInfo_gaode.to_excel(outpath_gaode + name_ANSI_gaode,index=False)
    df_JD_siteInfo_baidu.to_excel(outpath_baidu + name_ANSI_baidu,index=False)
    df_JD_siteInfo_gaode.to_csv(outpath_gaode + name_UTF8_gaode,index=False)
    df_JD_siteInfo_baidu.to_csv(outpath_baidu + name_UTF8_baidu,index=False)


    