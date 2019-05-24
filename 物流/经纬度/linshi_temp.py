import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlopen, quote,URLError, HTTPError
import time

data = pd.read_excel(r"F:\temp\190523\面对面15日.xlsx")

df = data[["收货地址","订单编号","所在省 / 市 / 县"]]

split = pd.DataFrame((x.split('/') for x in df['所在省 / 市 / 县']), index=df.index, columns=['所在省','所在市','所在县'])
df = pd.merge(df,split,left_index=True,right_index=True)

df['所在省'] = df['所在省'].map(lambda x:str(x))
df['所在市'] = df['所在市'].map(lambda x:str(x))
df['收货地址'] = df['收货地址'].map(lambda x:str(x))

df["收货人地址"] = df["所在省"] + df["所在市"] + df["收货地址"]

# 解析高德地图API网址信息
def get_latlng_gaode(address,ak):
    ak= ak
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
    return contest

def get_receiver_lnglat_gaode(address):
    start_time = time.time()
    re_List_gaode = []
    for b in address:
        print(b)
        re_Dict_gaode = {}
        try:
            temp=get_latlng_gaode(b,ak_gaode)
        except requests.exceptions.ConnectionError: # HTTPError
            re_Dict_gaode["re_location_gaode"] = "请求出错"         
        else:
            if ('geocodes' in temp):
                re_Dict_gaode["re_location_gaode"] = temp['geocodes'][0]['location']
                re_Dict_gaode["re_formatted_address_gaode"] = temp['geocodes'][0]['formatted_address']
                re_Dict_gaode["re_province_gaode"] = temp['geocodes'][0]['province']
                re_Dict_gaode["re_country_gaode"] = temp['geocodes'][0]['country']
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

def parse_gaode(df,address):
    # 解析高德
    list_gaode = get_receiver_lnglat_gaode(address)
    # df化(高德)
    df_gaode = pd.DataFrame(list_gaode)
    data_gaode = pd.concat([df,df_gaode],axis=1)
    print("data_gaode:" + str(data_gaode.shape))
    return data_gaode

ak_gaode = "1c2682317206ccaa18ec2487bb45d880"

data_gaode = parse_gaode(df,df["收货人地址"])

data_gaode.to_csv()