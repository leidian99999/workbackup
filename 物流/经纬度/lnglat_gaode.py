import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlopen, quote,URLError, HTTPError
import time

# 解析高德地图API网址信息
def get_latlng_gaode(address,ak):
    ak= ak
    url="http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s"%(ak,address)
    data=requests.get(url)
    contest=data.json()
    return contest

# 获取高德地图API地址信息
def get_receiver_lnglat_gaode(address):
    start_time = time.time()
    re_List_gaode = []
    for b in address:
        print(b)
        re_Dict_gaode = {}
        try:
            temp=get_latlng_gaode(b,ak_gaode)
        except requests.exceptions.ConnectionError: # HTTPError
            re_Dict_gaode["re_location_gaode"] = "0,0"         
        else:
            if (temp['status'] == "0"):
                print('status=0')
                pass
            else:
                if (temp['status'] == "1"):
                    if (temp['count'] == "1"):
                        if('location' in temp['geocodes'][0]):
                            re_Dict_gaode["re_location_gaode"] = temp['geocodes'][0]['location']
                        else:
                            pass
                        if ('formatted_address' in temp['geocodes'][0]):
                            re_Dict_gaode["re_formatted_address_gaode"] = temp['geocodes'][0]['formatted_address']
                        else:
                            pass
                        if ('province' in temp['geocodes'][0]):
                            re_Dict_gaode["re_province_gaode"] = temp['geocodes'][0]['province']
                        else:
                            pass
                        if ('country' in temp['geocodes'][0]):
                            re_Dict_gaode["re_country_gaode"] = temp['geocodes'][0]['country']
                        else:
                            pass
                        if ('city' in temp['geocodes'][0]):
                            re_Dict_gaode["re_city_gaode"] = temp['geocodes'][0]['city']
                        else:
                            pass
                        if ('district' in temp['geocodes'][0]):
                            re_Dict_gaode["re_district_gaode"] = temp['geocodes'][0]['district']
                        else: 
                            pass
                        if ('level' in temp['geocodes'][0]):
                            re_Dict_gaode["re_level_gaode"] = temp['geocodes'][0]['level']
                        else:
                            pass
                        if ('township' in temp['geocodes'][0]):
                            re_Dict_gaode["re_township_gaode"] = temp['geocodes'][0]['township']
                        else:
                            pass
                        if ('adcode' in temp['geocodes'][0]):
                            re_Dict_gaode["re_adcode_gaode"] = temp['geocodes'][0]['adcode']
                        else:
                            pass
                        if ('street' in temp['geocodes'][0]):
                            re_Dict_gaode["re_street_gaode"] = temp['geocodes'][0]['street']
                        else:
                            pass
                        if ('number' in temp['geocodes'][0]):
                            re_Dict_gaode["re_number_gaode"] = temp['geocodes'][0]['number']
                        else:
                            pass
                    else:
                        if (temp['count'] == "0"):
                            print("count=0")
                            pass
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

if __name__ == "__main__":

    # ak码
    ak_gaode = 'c71d9eda293d20db64955275557d92d4'

    # 导入数据
    date = "1812"
    fileName = date + "JDXX.xlsx"
    pinyin = "JDXX"
    inputpath = "/root/lnglat_gaode/"
    data = pd.read_excel(inputpath + fileName)

    # 导出数据路径
    outpath_gaode = "/root/lnglat_gaode/"
    name_ANSI_gaode = date + "Info_lnglat_" + pinyin + "_gaode.xlsx"
    name_UTF8_gaode = date + "Info_lnglat_" + pinyin + "_gaode.csv"


    # 选取有用字段
    df = data[["所在省","所在市","收货地址","订单编号","承运商"]]
    df["address_all"]= df["所在省"] +"省"+ df["所在市"] + df["收货地址"]

    # 文件分组并检查
    print("data:" + str(data.shape))
    print("df:" + str(df.shape))

    # 解析高德
    data_gaode = parse_gaode(df,df["address_all"])

    data_gaode['re_location_gaode'] = data_gaode['re_location_gaode'].map(lambda x:str(x))

    # 合表
    split_gaode = pd.DataFrame((x.split(',') for x in data_gaode['re_location_gaode']), index=data_gaode.index, columns=['re_siteLng_gaode','re_siteLat_gaode'])
    data_gaode = pd.merge(data_gaode,split_gaode,left_index=True,right_index=True)

    # 检查合并后结构
    print("data:" + str(data.shape))
    print("df:" + str(df.shape))
    print("data_gaode:" + str(data_gaode.shape))

    data_gaode.to_csv(outpath_gaode + name_UTF8_gaode,index=False)
