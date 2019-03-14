def get_JD_siteInfo_baidu(urls):
    start_time = time.time()
    listA = []
    for b in urls:
    #     print(b)
        dictA = {}
        try:
            temp = get_json_baidu(b)
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