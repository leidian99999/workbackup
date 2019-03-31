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
            re_Dict_gaode["re_location_gaode"] = "请求出错"         
        else:
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
            elif (temp['count'] == "0"):
                pass
            elif (temp['status'] == "0"):
                pass
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
    ak = ak
    add = quote(address) #由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    return temp

# 获取百度地图API地址信息
def get_receiver_lnglat_baidu(address):
    start_time = time.time()
    re_List_baidu = []
    for b in address:
#         print(b)
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
	date = "1902"
	fileName = "韵达(承运商).xlsx"
	pinyin = "YD"
	inputpath = "G:\\work\\basic\\carriers\\" + date + "\\"
	data = pd.read_excel(inputpath + fileName)

	# 导出数据路径
	outpath_gaode = "G:\\work\\basic\\carriers\\" + date + "\\output\\gaode\\"
	name_ANSI_gaode = date + "Info_lnglat_" + pinyin + "_gaode.xlsx"
	name_UTF8_gaode = date + "Info_lnglat_" + pinyin + "_gaode.csv"

	outpath_baidu = "G:\\work\\basic\\carriers\\" + date + "\\output\\baidu\\"
	name_ANSI_baidu = date + "Info_lnglat_" + pinyin + "_baidu.xlsx"
	name_UTF8_baidu = date + "Info_lnglat_" + pinyin + "_baidu.csv"

    print("各省样本量：")
    print(data["所在省"].value_counts())


	# 选取有用字段
	df = data[["所在省","所在市","收货地址","订单编号","承运商"]]
	df["address_all"]= df["所在省"] +"省"+ df["所在市"] + df["收货地址"]

    df1 = df[df["所在省"].isin(["广东"])].reset_index(drop=True)
    df2 = df[df["所在省"].isin(["山东"])].reset_index(drop=True)
    df3 = df[df["所在省"].isin(["河南"])].reset_index(drop=True)

    df4 = df[df["所在省"].isin(["江苏"])].reset_index(drop=True)
    df5 = df[df["所在省"].isin(["河北"])].reset_index(drop=True)
    df6 = df[df["所在省"].isin(["湖北"])].reset_index(drop=True)
    df7 = df[df["所在省"].isin(["北京"])].reset_index(drop=True)
    df8 = df[df["所在省"].isin(["湖南"])].reset_index(drop=True)

    df9 = df[df["所在省"].isin(["浙江","上海"])].reset_index(drop=True)
    df10 = df[df["所在省"].isin(["四川","云南","广西"])].reset_index(drop=True)
    df11 = df[df["所在省"].isin(["辽宁","黑龙江","安徽"])].reset_index(drop=True)
    df12 = df[df["所在省"].isin(["陕西","山西"])].reset_index(drop=True)

    df13 = df[df["所在省"].isin(["吉林","内蒙古","重庆","江西","福建","贵州","甘肃","天津","宁夏","海南","青海","西藏","新疆"])].reset_index(drop=True)

	# 文件分组并检查
	print("data:" + str(data.shape))
	print("df:" + str(df.shape))

    data1_gaode = parse_gaode(df1,df1["address_all"])
    data2_gaode = parse_gaode(df2,df2["address_all"])
    data3_gaode = parse_gaode(df3,df3["address_all"])
    data4_gaode = parse_gaode(df4,df4["address_all"])
    data5_gaode = parse_gaode(df5,df5["address_all"])
    data6_gaode = parse_gaode(df6,df6["address_all"])
    data7_gaode = parse_gaode(df7,df7["address_all"])
    data8_gaode = parse_gaode(df8,df8["address_all"])
    data9_gaode = parse_gaode(df9,df9["address_all"])
    data10_gaode = parse_gaode(df10,df10["address_all"])
    data11_gaode = parse_gaode(df11,df11["address_all"])
    data12_gaode = parse_gaode(df12,df12["address_all"])
    data13_gaode = parse_gaode(df13,df13["address_all"])

    data_gaode = pd.concat([data1_gaode,data2_gaode,data3_gaode,data4_gaode,data5_gaode,data6_gaode,data7_gaode,data8_gaode,data9_gaode,data10_gaode,data11_gaode,data12_gaode,data13_gaode])

    # 合表
    split_gaode = pd.DataFrame((x.split(',') for x in data_gaode['re_location_gaode']), index=data_gaode.index, columns=['re_siteLng_gaode','re_siteLat_gaode'])
    data_gaode = pd.merge(data_gaode,split_gaode,left_index=True,right_index=True)

    # 检查合并后结构
    print("data:" + str(data.shape))
    print("df:" + str(df.shape))
    print("data_gaode:" + str(data_gaode.shape))

    data_gaode.to_csv(outpath_gaode + name_UTF8_gaode,index=False)
    data_baidu.to_csv(outpath_baidu + name_UTF8_baidu,index=False)