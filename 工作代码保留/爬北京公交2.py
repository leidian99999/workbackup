
import requests
import pandas as pd
from lxml import etree



city = "langfang"

url = 'http://'+city+'.gongjiao.com/lines_all.html'
# url = 'http://www.gongjiao.com/'
text = requests.get(url).text
doc = etree.HTML(text)
all_lines = doc.xpath("//div[@class='list']/ul/li")
# all_citis = doc.xpath("//div[@class='g-cities2']")

df_dict = {
    'line_name': [],
    'line_url': [],
    'line_start': [],
    'line_stop': [],
    'line_op_time': [],
    'line_interval': [],
    'line_price': [],
    'line_company': [],
    'line_up_times': [],
    'line_station_up': [],
    'line_station_up_len': [],
    'line_station_down': [],
    'line_station_down_len': [] 
}

for line in all_lines:
    line_name = line.xpath("./a/text()")[0].strip()
    line_url = line.xpath("./a/@href")[0]
#     print(line_name, line_url)
    info_text = requests.get(line_url).text
    info_doc = etree.HTML(info_text)
    infos = info_doc.xpath("//div[@class='gj01_line_header clearfix']")
    for info in infos:
        start_stop = info.xpath("./dl/dt/a/text()")
#         print(start_stop)
        op_times = info.xpath("./dl/dd[1]/b/text()")
        if len(op_times) == 0:
            op_times = ["未知"]
#         print(op_times)
        interval = info.xpath("./dl/dd[2]/text()")
        if len(interval) == 0:
            interval = ["未知"]
#         print(interval)
        price = info.xpath("./dl/dd[3]/text()")
        if len(price) == 0:
            price = ["未知"]
#         print(price)
        company = info.xpath("./dl/dd[4]/text()")
        if len(company) == 0:
            company = ["未知"]
#         print(company)
        up_times = info.xpath("./dl/dd[5]/text()")
        if len(up_times) == 0:
            up_times = ["未知"]
#         print(up_times)
        all_stations_up = info_doc.xpath('//ul[@class="gj01_line_img JS-up clearfix"]')
        for station in all_stations_up:
            station_up_name = station.xpath('./li/a/text()')
            if len(station_up_name) == 0:
                station_up_name = ["未知"]
#             print(station_up_name)
        all_stations_down = info_doc.xpath('//ul[@class="gj01_line_img JS-down clearfix"]')
        for station in all_stations_down:
            station_down_name = station.xpath('./li/a/text()')
            if len(station_down_name) == 0:
                station_down_name = ["未知"]
#             print(station_down_name)
    try:
        
        df_dict['line_name'].append(line_name)
        df_dict['line_url'].append(line_url)
        df_dict['line_start'].append(start_stop[0])
        df_dict['line_stop'].append(start_stop[1])
        df_dict['line_op_time'].append(op_times[0])
        df_dict['line_interval'].append(interval[0][5:])
        df_dict['line_company'].append(company[0][5:])
        df_dict['line_price'].append(price[0][5:])
        df_dict['line_up_times'].append(up_times[0][5:])
        df_dict['line_station_up'].append(station_up_name)
        df_dict['line_station_up_len'].append(len(station_up_name))
        df_dict['line_station_down'].append(station_down_name)
        df_dict['line_station_down_len'].append(len(station_down_name))
        print('{} success!'.format(line_name))
    except:
        print(line_name, line_url)
        continue
#     break
df = pd.DataFrame(df_dict)
df.to_csv(city + 'Bus_lines_utf8.csv', index=None)
print("OK！爬取完毕")