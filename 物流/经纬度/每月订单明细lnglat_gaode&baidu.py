import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlopen, quote,URLError, HTTPError
import time

# 解析高德地图API网址信息
def get_latlng_gaode(address,ak):
    ak= ak_gaode
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
    return contest

# 获取高德地图API地址信息
def get_receiver_lnglat_gaode(address):
    start_time = time.time()
    re_List_gaode = []
    for b in address:
    #     print(b)
        re_Dict_gaode = {}
        try:
            temp=get_latlng_gaode(b,ak_gaode)
        except HTTPError as e:
            print("请求出错")
            pass
        else:
            if ('geocodes' in temp):
                re_Dict_gaode["re_location_gaode"] = temp['geocodes'][0]['location']
                re_Dict_gaode["re_formatted_address_gaode"] = temp['geocodes'][0]['formatted_address']
                re_Dict_gaode["re_province_gaode"] = temp['geocodes'][0]['province']
                re_Dict_gaode["re_country_gaode"] = temp['geocodes'][0]['country']
                if ('citycode' in temp):
                    re_Dict_gaode["re_citycode_gaode"] = temp['geocodes'][0]['citycode']
                else:
                    pass
                re_Dict_gaode["re_city_gaode"] = temp['geocodes'][0]['city']
                re_Dict_gaode["re_district_gaode"] = temp['geocodes'][0]['district']
                re_Dict_gaode["re_level_gaode"] = temp['geocodes'][0]['level']
                re_Dict_gaode["re_township_gaode"] = temp['geocodes'][0]['township']
                re_Dict_gaode["re_adcode_gaode"] = temp['geocodes'][0]['adcode']
                re_Dict_gaode["re_street_gaode"] = temp['geocodes'][0]['street']
                re_Dict_gaode["re_number_gaode"] = temp['geocodes'][0]['number']
            else:
                pass
        re_List_gaode.append(re_Dict_gaode)
    #     time.sleep(1)
    end_time = time.time()
    print("高德总用时：",end_time-start_time)
    return re_List_gaode

# 解析百度地图API网址信息
def get_latlng_baidu(address,ak):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'#输出数据的格式
    ak = ak_baidu
    add = quote(address) #由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    return temp

# 获取高德地图API地址信息
def get_receiver_lnglat_baidu(address):
    start_time = time.time()
    re_List_baidu = []
    for b in address:
        print(b)
        re_Dict_baidu = {}
        try:
            temp = get_latlng_baidu(b,ak_baidu)
        except HTTPError as e:
            print("请求出错")
            pass
        else:
            if ('result' in temp):
                re_Dict_baidu["re_Lng_baidu"] = temp['result']['location']['lng']
                re_Dict_baidu["re_Lat_baidu"] = temp['result']['location']['lat']
                re_Dict_baidu["re_Precise_baidu"] = temp['result']['precise']
                re_Dict_baidu["re_Confidence_baidu"] = temp['result']['confidence']
                re_Dict_baidu["re_Comprehension_baidu"] = temp['result']['comprehension']
                re_Dict_baidu["re_Level_baidu"] = temp['result']['level']
            else:
                pass
        re_List_baidu.append(re_Dict_baidu)
    #     time.sleep(1)
    end_time = time.time()
    print("百度总用时：", end_time - start_time)
    return re_List_baidu


if __name__ == "__main__":
    # ak码
    ak_gaode = 'c71d9eda293d20db64955275557d92d4'
    ak_baidu = 'z3KEtliyTGvj0bFudEkz4GO0GN8eQQa5'

    # 导入数据
    inputpath = "G:\\work\\basic\\alter\\"
    inputFileName = "1812_info_alter_gai.csv"
    data = pd.read_csv(inputpath + inputFileName)
    df = data.sample(n=5) # 抽样

    # 导出数据
    outpath = "G:\\work\\basic\\alter\\"
    name_ANSI = "1812_info_alter_lnglat1.xlsx"
    name_UTF8 = "1812_info_alter_lnglat.csv"

    df["re_address_all"] = df["所在省"] + df["所在市"] + df["收货地址"]

    print("验证完整收货地址：")
    print(df["re_address_all"][0:3])
    print("&%"*50)

    df_re_lnglat_gaode = pd.DataFrame(get_receiver_lnglat_gaode(df["re_address_all"]))
    df_re_lnglat_baidu = pd.DataFrame(get_receiver_lnglat_baidu(df["re_address_all"]))

    split_gaode = pd.DataFrame((x.split(',') for x in df_re_lnglat_gaode['re_location_gaode']),
                               index=df_re_lnglat_gaode.index, columns=['re_Lng_gaode', 're_Lat_gaode'])
    df_re_lnglat_gaode = pd.merge(df_re_lnglat_gaode, split_gaode, left_index=True, right_index=True)

    df1 = pd.concat([df, df_re_lnglat_gaode], axis=1) # df_re_lnglat_baidu
    df.to_excel(outpath+name_ANSI,index=False)

