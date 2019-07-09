import requests
import pandas as pd
from lxml import etree




def get_lines(all_lines):
	line_name = []
	line_url = []
	for line in all_lines:
		a = line.xpath("./a/text()")[0].strip()
		b = line.xpath("./a/@href")[0]
		line_name.append(a)
		line_url.append(b)        
	return line_name,line_url

def get_line_info(info_doc):
	infos = info_doc.xpath("//div[@class='gj01_line_header clearfix']") # 获取线路详情页目标板块
	for info in infos:
		target_stop = info.xpath("./dl/dt/a/text()") # 终点站名称
		target_stop_url = info.xpath("./dl/dt/a/@href") # 终点站网址
		# 运营时间
		op_times = info.xpath("./dl/dd/b/text()")  
		if len(op_times) == 0:
			op_times = ["未知"]
		# 发车间隔
		interval = info.xpath("./dl/dd[2]/text()") 
		if len(interval) == 0:
			interval = ["未知"]
		# 票价信息    
		price = info.xpath("./dl/dd[3]/text()") 
		if len(price) == 0:
			price = ["未知"]
		# 汽车公司    
		company = info.xpath("./dl/dd[4]/text()") 
		if len(company) == 0:
			company = ["未知"]
		# 更新时间    
		date_up = info.xpath("./dl/dd[5]/text()") 
		if len(date_up) == 0:
			date_up = ["未知"]
	    
	return target_stop,op_times,interval,price,company,date_up

def get_stops(info_doc):
	all_stops_up = info_doc.xpath('//ul[@class="gj01_line_img JS-up clearfix"]') # 获取线路详情页目标板块
	for stop in all_stops_up:
		stops_up = stop.xpath("./li/a/text()")
		if len(stops_up) == 0:
			stops_up = ["未知"]
	all_stops_down = info_doc.xpath('//ul[@class="gj01_line_img JS-down clearfix"]')
	for stop in all_stops_down:
		stops_down = stop.xpath("./li/a/text()")
		if len(stops_down) == 0:
			stops_down = ["未知"]
	return stops_up,stops_down


if __name__=='__main__':
	url = 'http://beijing.gongjiao.com/lines_all.html'
	text = requests.get(url).text
	doc = etree.HTML(text)
	all_lines = doc.xpath("//div[@class='list']/ul/li")

	line_name,line_url = get_lines(all_lines)
	for

	print(line_name)