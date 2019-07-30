import pandas as pd
import numpy as np

# 路径参数修改
inputPath = "D:/work/temp/190729/"
inputname1 = "725 新线问卷不带站点"
inputname2 = "725新线问卷过闸站点"

outPath = "D:/work/temp/190729/"
outName = "out"



def NotSameday(df):
    DiffDays_list = []
    for index, row in df.iterrows():
        DiffDays_dict = {}
        if row["submit_date"] == row["entry_date_time_date"]:
            DiffDays_dict["tong"] = "同日"
        else:
            DiffDays_dict["tong"] = "不同"            
        DiffDays_list.append(DiffDays_dict)
    return DiffDays_list

def AfterTime(df):
    AfterTime_list = []
    for index, row in df.iterrows():
        AfterTime_dict = {}
        if row["submit_hour"] >= row["entry_date_time_hours"]:
            AfterTime_dict["AfterTime"] = "AfterTime"
        else:
            AfterTime_dict["AfterTime"] = "Not"            
        AfterTime_list.append(AfterTime_dict)
    return AfterTime_list

if __name__=='__main__':

	# 读取数据
	data1 = pd.read_excel(inputPath + inputname1 + ".xlsx")
	data2 = pd.read_excel(inputPath + inputname2 + ".xlsx")
	# 查看数据
	print("data1:"+str(data1.shape))
	print("data2:"+str(data2.shape))
	# 合并数据
	df = pd.merge(data1[["user_id","submit_date","submit_time"]],data2[["userid","entry_date_time_str"]],how="right",left_on="user_id",right_on="userid")

	# df = data.copy()
	'''数据格式转化'''
	# 转化进站时间数据
	df['entry_date_time_str']  = df['entry_date_time_str'].map(lambda x:str(x))
	df['entry_date_time_date'] = pd.to_datetime(df['entry_date_time_str'].str[0:8])
	df['entry_date_time_hours'] = pd.to_datetime(df["entry_date_time_str"]).dt.hour
	# 转化提交时间数据
	df['submit_date']  = pd.to_datetime(df['submit_date'])#.dt.date
	df['submit_time']  = df['submit_time'].map(lambda x:str(x))
	split1 = pd.DataFrame((x.split(':') for x in df['submit_time']),index=df.index,columns=['submit_hour','submit_min','submit_sec'])
	df = pd.merge(df, split1, left_index=True, right_index=True)

	df = df[~df['submit_hour'].str.contains('nan')]
	df.submit_hour.value_counts()
	df['submit_hour'] = df['submit_hour'].astype("int")

	# 删除日期不同的样本
	df3 = pd.DataFrame(NotSameday(df))
	df3 = pd.concat([df,df3],axis=1)
	df_SameDay  = df3[df3["tong"].str.contains("同日")].reset_index(drop=True)

	# 删除进站时间大于提交时间的样本
	df4 = pd.DataFrame(AfterTime(df_SameDay))
	df5 = pd.concat([df_SameDay,df4],axis=1)
	df_AfterTime = df5[df5["AfterTime"].str.contains("AfterTime")].reset_index(drop=True)

	# 计算时间差
	df_fin = df_AfterTime[["userid","entry_date_time_hours","submit_hour"]]
	df_fin["MinTime"] = df_fin["submit_hour"] - df_fin["entry_date_time_hours"]

	# 取分组最小值，即距离答题时间最近的时间样本
	df_out = df_fin.sort_values('MinTime', ascending=True).groupby('userid', as_index=False).first()

	# 输出结果
	df_out.to_excel(outPath + outName +".xlsx",index=False)