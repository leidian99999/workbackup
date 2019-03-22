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
#         print(b)
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
	dirDate = "FEB19"
	date = "1902"
	provinceName = "浙江(所在省).xlsx"
	pinyin = "zhejiang"
	inputpath = "G:\\work\\basic\\province\\" + dirDate + "\\"
	data = pd.read_excel(inputpath + provinceName)

	# 导出数据路径
	outpath_gaode = "G:\\work\\basic\\province\\GAODE\\"
	name_ANSI_gaode = date + "Info_lnglat_" + pinyin + "_gaode.xlsx"
	name_UTF8_gaode = date + "Info_lnglat_" + pinyin + "_gaode.csv"
	outpath_baidu = "G:\\work\\basic\\province\\BAIDU\\"
	name_ANSI_baidu = date + "Info_lnglat_" + pinyin + "_baidu.xlsx"
	name_UTF8_baidu = date + "Info_lnglat_" + pinyin + "_baidu.csv"

	# 选取有用字段
	df = data[["所在省","所在市","收货地址","订单编号","承运商"]]
	df["address_all"]= df["所在省"] +"省"+ df["所在市"] + df["收货地址"]

	# 文件分组并检查
	print("data:" + str(data.shape))
	print("df:" + str(df.shape))
	df_EMS = df[df["承运商"] == "EMS"].reset_index(drop=True)
	df_JDWL = df[df["承运商"] == "京东物流"].reset_index(drop=True)
	df_YD = df[df["承运商"] == "韵达"].reset_index(drop=True)
	df_JDXX = df[df["承运商"] == "京东线下"].reset_index(drop=True)

	print("df_EMS:" + str(df_EMS.shape))
	print("df_JDWL:" + str(df_JDWL.shape))
	print("df_YD:" + str(df_YD.shape))
	print("df_JDXX:" + str(df_JDXX.shape))

	# 高德地址解析
	list_JDXX_gaode = get_receiver_lnglat_gaode(df_JDXX["address_all"])
	list_JDWL_gaode = get_receiver_lnglat_gaode(df_JDWL["address_all"])
	list_EMS_gaode = get_receiver_lnglat_gaode(df_EMS["address_all"])
	list_YD_gaode = get_receiver_lnglat_gaode(df_YD["address_all"])
	# df化(高德)
	df_EMS_gaode = pd.DataFrame(list_EMS_gaode)
	df_JDXX_gaode = pd.DataFrame(list_JDXX_gaode)
	df_JDWL_gaode = pd.DataFrame(list_JDWL_gaode)
	df_YD_gaode = pd.DataFrame(list_YD_gaode)

	data_JDWL_gaode = pd.concat([df_JDWL,df_JDWL_gaode],axis=1)
	data_JDXX_gaode = pd.concat([df_JDXX,df_JDXX_gaode],axis=1)
	data_EMS_gaode = pd.concat([df_EMS,df_EMS_gaode],axis=1)
	data_YD_gaode = pd.concat([df_YD,df_YD_gaode],axis=1)

	# 百度地址解析
	list_JDXX_baidu = get_receiver_lnglat_baidu(df_JDXX["address_all"])
	list_JDWL_baidu = get_receiver_lnglat_baidu(df_JDWL["address_all"])
	list_EMS_baidu = get_receiver_lnglat_baidu(df_EMS["address_all"])
	list_YD_baidu = get_receiver_lnglat_baidu(df_YD["address_all"])

	# df化(百度)
	df_EMS_baidu = pd.DataFrame(list_EMS_baidu)
	df_JDXX_baidu = pd.DataFrame(list_JDXX_baidu)
	df_JDWL_baidu = pd.DataFrame(list_JDWL_baidu)
	df_YD_baidu = pd.DataFrame(list_YD_baidu)

	data_JDWL_baidu = pd.concat([df_JDWL,df_JDWL_baidu],axis=1)
	data_JDXX_baidu = pd.concat([df_JDXX,df_JDXX_baidu],axis=1)
	data_EMS_baidu = pd.concat([df_EMS,df_EMS_baidu],axis=1)
	data_YD_baidu = pd.concat([df_YD,df_YD_baidu],axis=1)

	# 检查各df
	print("data_JDWL_gaode:" + str(data_JDWL_gaode.shape))
	print("data_JDXX_gaode:" + str(data_JDXX_gaode.shape))
	print("data_YD_gaode:" + str(data_YD_gaode.shape))
	print("data_EMS_gaode:" + str(data_EMS_gaode.shape))
	print("*"*50)
	print("data_JDWL_baidu:" + str(data_JDWL_baidu.shape))
	print("data_JDXX_baidu:" + str(data_JDXX_baidu.shape))
	print("data_YD_baidu:" + str(data_YD_baidu.shape))
	print("data_EMS_baidu:" + str(data_EMS_baidu.shape))

	# 合表
	data_gaode_all = pd.concat([data_JDWL_gaode,data_JDXX_gaode,data_EMS_gaode,data_YD_gaode],axis=0)
	split_gaode = pd.DataFrame((x.split(',') for x in data_gaode_all['re_location_gaode']), index=data_gaode_all.index, columns=['re_siteLng_gaode','re_siteLat_gaode'])
	data_gaode_all = pd.merge(data_gaode_all,split_gaode,left_index=True,right_index=True)

	data_baidu_all = pd.concat([data_JDWL_baidu,data_JDXX_baidu,data_EMS_baidu,data_YD_baidu],axis=0)

	# 检查合并后结构
	print("data:" + str(data.shape))
	print("df:" + str(df.shape))
	print("data_gaode_all:" + str(data_gaode_all.shape))
	print("data_baidu_all:" + str(data_baidu_all.shape))


	# 输出
	data_gaode_all.to_csv(outpath_gaode + name_UTF8_gaode,index=False)
	data_baidu_all.to_csv(outpath_baidu + name_UTF8_baidu,index=False)