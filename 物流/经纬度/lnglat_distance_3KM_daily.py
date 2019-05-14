import pandas as pd
from geopy.distance import vincenty
import time

date = "190426"

df_old = pd.read_csv(r"G:\work\logistica\distance\input/1901info_lnglat_gaode.csv")
df_new = pd.read_excel(r"F:\temp\190428/" + date + ".xlsx")
# standard = pd.read_excel("/root/lnglat_gaode/daily_distance/standard_1901-03(55%).xlsx")
df_info = pd.read_csv(r"G:\work\basic\CSV/1901_info.csv")
# county = list(standard.iloc[:,2])

df_old = df_old[df_old["所在省"].str.contains("所在省") == False]
df_old = df_old[df_old["re_district_gaode"].str.contains("\[\]",regex=True) == False]
df_new = df_new[df_new["re_district_gaode"].str.contains("\[\]",regex=True) == False]
# df_new = df_new[df_new["所在县"].isin(county)]

def FenSheng(df_new,df_old,col_province,col_city,col_district,col_lng,col_lat):
    start_time = time.time()
    dfA = pd.DataFrame(columns=['orderID_old','orderID_new','distance'])
    limit_KM = round(3 /(3.14 * 6400 /180),6)
    
    
    province_list = df_new[col_province].unique()
    for sheng in province_list:
#         print(sheng)

        dfold_sheng = df_old[df_old[col_province] == sheng].reset_index(drop=True)
        dfnew_sheng = df_new[df_new[col_province] == sheng].reset_index(drop=True)
        
               
        city_list = dfnew_sheng[col_city].unique()
        for shi in city_list:
#             print(sheng+shi)

            dfold_shi = dfold_sheng[(dfold_sheng[col_city] == shi)].reset_index(drop=True)
            dfnew_shi = dfnew_sheng[(dfnew_sheng[col_city] == shi)].reset_index(drop=True)   
            
            district_list = dfnew_shi[col_district].unique()              
            for xian in district_list:
#                 print(sheng+shi+xian)
#                 print("*"*30)
                dfold = dfold_shi[dfold_shi[col_district] == xian].reset_index(drop=True)
                dfnew = dfnew_shi[dfnew_shi[col_district] == xian].reset_index(drop=True)
                if dfnew.empty == True:
                    print(sheng + xian + "：为空")
                    pass
                elif dfold.empty == True:
                    print("原所在市不存在")
                    pass
                else:
                    for i in range(0,len(dfnew[col_lng])):
                        for j in range(0,len(dfold[col_lng])):
                            start_lng = round(dfnew[col_lng][i],6)
                            start_lat = round(dfnew[col_lat][i],6)
                            end_lng = round(dfold[col_lng][j],6)
                            end_lat = round(dfold[col_lat][j],6)
                            start_lnglat = (start_lat,start_lng)
                            end_lnglat = (end_lat,end_lng)
                            if (abs(start_lat - end_lat) <= limit_KM or abs(start_lng - end_lng) <= limit_KM ):
                                a = vincenty(start_lnglat, end_lnglat).km
                                row={'orderID_old':dfold['订单编号'][j],'orderID_new':dfnew['订单编号'][i],'distance':a}
                                dfA = dfA.append(row,ignore_index=True)
                            else:
                                pass
                    print(str(sheng) + str(shi) + str(xian) + "：已完成")
    end_time = time.time()
    print("总用时：",end_time-start_time)
    return dfA


df_old['re_siteLat_gaode'] = df_old['re_siteLat_gaode'].map(lambda x:float(x))
df_old['re_siteLng_gaode'] = df_old['re_siteLng_gaode'].map(lambda x:float(x))
df_new['re_siteLat_gaode'] = df_new['re_siteLat_gaode'].map(lambda x:float(x))
df_new['re_siteLng_gaode'] = df_new['re_siteLng_gaode'].map(lambda x:float(x))

dfA = FenSheng(df_new,df_old,"re_province_gaode","re_city_gaode","re_district_gaode","re_siteLng_gaode","re_siteLat_gaode")

# dfB = dfA[dfA['distance'] <= 3]

print("df_new:" + str(df_new.shape))
print("df_old:" + str(df_old.shape))

dfC = pd.merge(dfA,df_info,how = "inner",left_on="orderID_old",right_on="订单编号")



dfC.to_excel(r"G:\work\logistica\distance\output/" + date + "info_lnglat_dis_WS.xlsx",index=False)
# dfA.to_excel("/root/lnglat_gaode/daily/output/" + date + "_lnglat_disAll.xlsx",index=False)
