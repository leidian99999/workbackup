import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os

# def all_path(dirname):
#     result = []#所有的文件
#     for maindir, subdir, file_name_list in os.walk(dirname):
#         #os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
#         print("读取目录:",maindir) #当前主目录
#         urls =[]

#         for a in file_name_list:
#             url = "http://www.jdwl.com/site/querySiteList?" + a[:-5]
#             urls.append(url)
#         return urls

# urls = all_path("D:/work/logistica/stations/JDStations/yuanURL/湖南/")

outpath = "G:\\work\\logistica\\stations\\JDStations\\stations\\website\\"
# name_UTF8 = "\\CSV\\JDstations_zhejiang.csv"
name_ANSI = "JDstations_zhejiang_JD.xlsx"

df = pd.read_excel(r"G:\\work\\logistica\\stations\\JDStations\\yuanURL\\浙江/浙江.xlsx")

urls = []
for a in df["url"]:
    urls.append( "http://www.jdwl.com/site/querySiteList?" +a )


listA = []
for url in urls:

    request = requests.get(url)
    soup = BeautifulSoup(request.content, "lxml").get_text()
    jsonlist = json.loads(soup)

    
    for i in range(len(jsonlist)):
        dictA = {}
        dictA["siteBusinessName"] = jsonlist[i]["siteBusinessName"]
        dictA["provinceId"] = jsonlist[i]["provinceId"]
        dictA["cityId"] = jsonlist[i]["cityId"]
        dictA["countyId"] = jsonlist[i]["countyId"]
        dictA["siteName"] = jsonlist[i]["siteName"]
        if 'address' in jsonlist[i]:
            dictA["siteAddress"] = jsonlist[i]["address"]
        else:
            pass
        if 'latitude' in jsonlist[i]:
            dictA["siteLatitude"] = jsonlist[i]['latitude']
        else:
            pass  
        if 'longitude' in jsonlist[i]:
            dictA["siteLongitude"] = jsonlist[i]['longitude']
        else:
            pass       
        if "telephone" in jsonlist[i]:
            dictA["siteTelephone"] = jsonlist[i]["telephone"]
        else:
            pass
        
        listA.append(dictA)
    
df_A = pd.DataFrame(listA)


# print(df_A['siteAddress'].isnull().value_counts())
# df_A = df_A.dropna(subset=["siteAddress"])
# print(df_A['siteAddress'].isnull().value_counts())


print("df_A:" + str(df_A.shape))
df_A.to_excel(outpath + name_ANSI)

