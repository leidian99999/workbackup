import pandas as pd
import numpy as np
import datetime
import time


pd.set_option("display.max_columns",200)



today_file = "181212"
yestoday = "2018-12-11"
today = datetime.datetime(2018,12,12)
fold = "本网"
writer = r"G:\work\日报\短信反馈\\保存\\"
out_name = today_file+fold

df = pd.read_excel("G:\\work\\日报\\短信反馈\\"+"每日激活量"+"\\"+yestoday+"激活量.xlsx")
biaoka = pd.read_excel("G:/work/日报/功能列表/产品标卡.xlsx")
print("读取表格" + str(df.shape))
print("*"*100)

def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:
        result_date = today - datetime.timedelta(days=i)
        d = result_date.strftime('%m.%d')
        before_n_days.append(d)
    return before_n_days

gg = get_nday_list(5)
print("取数对比日期" + str(gg))
print("*"*100)

#合表
new_df = pd.DataFrame()
for i in gg:
    a = pd.read_excel("G:/work/日报/短信/输出/"+fold+"全表/"+fold+"签收未激活去新装去重-"+str(i)+"取数.xlsx")
    b = pd.merge(df,a[['订单编号']],how='inner',on='订单编号')
    new_df = pd.concat([new_df,b],ignore_index=True)
print("合表后：" + str(new_df.shape))
print("*"*100)

#去重
df_out = new_df.drop_duplicates(subset=['订单编号'],keep="first")
print("去重后：" + str(df_out.shape))
print("*"*100)

#vlookup标卡表
df_out['销售品编号'] = df_out['销售品编号'].map(lambda x:str(x))
biaoka['销售品编号'] = biaoka['销售品编号'].map(lambda x:str(x))
df_out = pd.merge(df_out,biaoka,how="left",on="销售品编号")
print("匹配标卡后，行列数:%s行，%s列" % (df_out.shape[0],df_out.shape[1]))
print("*"*100)
print(df_out['分类'].value_counts())

#“订单生成时间”分列
df_out['订单生成时间'] = df_out['订单生成时间'].map(lambda x:str(x))
split1 = pd.DataFrame((x.split(' ') for x in df_out['订单生成时间']), index=df_out.index, columns=['订单生成日期','订单时间'])
df_out = pd.merge(df_out,split1,left_index=True,right_index=True)
print("分列‘订单生成时间’后，{}行，{}列".format(df_out.shape[0],df_out.shape[1]))
print("*"*100)

#“交易完成时间”分列
df_out['交易完成时间'] = df_out['交易完成时间'].map(lambda x:str(x))
split3 = pd.DataFrame((x.split(' ') for x in df_out['交易完成时间']), index=df_out.index, columns=['交易完成日期','交易时间'])
df_out = pd.merge(df_out,split3,left_index=True,right_index=True)
print("分列‘交易完成时间时间’后，{}行，{}列".format(df_out.shape[0],df_out.shape[1]))
print("*"*100)

#分列号码归属地
split2 = pd.DataFrame((x.split('/') for x in df_out['号码归属地']), index=df_out.index, columns=['所属省','地区'])
df_out = pd.merge(df_out,split2,left_index=True,right_index=True)
print("分列‘号码归属地’后，{}行，{}列".format(df_out.shape[0],df_out.shape[1]))
print("*"*100)

#计算激活时效
df_out['订单生成日期'] = pd.to_datetime(df_out['订单生成日期'])
df_out['交易完成日期'] = pd.to_datetime(df_out['交易完成日期'])
df_out["激活时效"] = (df_out['交易完成日期'] - df_out['订单生成日期']).dt.days
print("准备分卡：" + str(df_out.shape))
print("*"*100)

#筛选米粉卡
print("筛选米粉卡")
df_MI = df_out[df_out["分类"].isin(['米粉卡','米粉卡日租','米粉卡体验','米粉卡会员'])]
print("米粉卡：" + str(df_MI.shape))
#筛出京东卡
print("筛出京东卡")
df_JD = df_out[df_out["分类"].isin(['京东体验卡','京粉卡','京东99VIP卡'])]
print("京东体验卡：" + str(df_JD.shape))
#筛出其他卡
print("筛出其他卡")
df_other = df_out[(True ^ df_out['分类'].isin(['京东体验卡','米粉卡','新装','京粉卡','米粉卡日租','米粉卡体验','京东99VIP卡']))]
print("其他卡：" + str(df_other.shape))
print("*"*100)

#结果输出
print(yestoday + fold + "结果输出")
#京东十日上
df_JD_up10 = df_JD[df_JD["激活时效"] > 10]
print("京东沉默用户数：%s"%df_JD_up10.shape[0])
#京东十日下
df_JD_down10 = df_JD[df_JD["激活时效"] <= 10]
print("京东非沉默用户数：%s"%df_JD_down10.shape[0])
#小米十日上
df_MI_up10 = df_MI[df_MI["激活时效"] > 10]
print("小米沉默用户数：%s"%df_MI_up10.shape[0])
#小米十日下
df_MI_down10 = df_MI[df_MI["激活时效"] <= 10]
print("小米非沉默用户数：%s"%df_MI_down10.shape[0])
#其他十日上
df_other_up10 = df_other[df_other["激活时效"] > 10]
print("非京米粉沉默用户数:%s"%df_other_up10.shape[0])
#其他十日下
df_other_down10 = df_other[df_other["激活时效"] <= 10]
print("非京米粉非沉默用户数：%s"%df_other_down10.shape[0])
print("合计：%s"%df_out.shape[0])
print("*"*20)

print("输出原是表：" + str(df_out.shape))
print("*"*20)

# 去除多余表头
df_out = df_out[df_out['入网身份证号'].str.contains('入网身份证号') == False]


df_out.to_excel(writer + out_name +"短信激活反馈初始表.xlsx" ,index = False)
# df_out = pd.read_excel(writer + out_name +"短信激活反馈初始表.xlsx" ) #错误时用
df_new = df_out[['入网身份证号', '所属省', '订单生成日期', '交易完成日期', '激活时效','分类']]


# 区分沉默用户
bins =[0,10,100] 
df_new['silence'] = pd.cut(df_new['激活时效'],bins,labels=["非沉默用户","沉默用户"])

# 区分年龄段
df_new['birthday'] = df_new['入网身份证号'].str[6:14]
df_new['birthday'] = pd.to_datetime(df_new["birthday"])
now_year =datetime.datetime.today().year #当前的年份
df_new['age']=now_year-df_new["birthday"].dt.year
bins2 = [0,18,25,35,45,55,200]
df_new['age_group'] = pd.cut(df_new['age'],bins2,labels=["18岁及以下","19-25岁",'26-35岁','36-45岁','46-55岁','56岁及以上'])



# 透视表

# 分卡品
category = pd.pivot_table(df_new,index=[u'分类',u'silence'],values=['激活时效'],
                          aggfunc=[np.mean,len],fill_value = 0,
                          margins = True,margins_name = '合计')

# 分省
province = pd.pivot_table(df_new,index=[u'所属省',u'silence'],values=['激活时效'],
                          aggfunc=[np.mean,len],fill_value = 0,
                          margins = True,margins_name = '合计')
# 分年龄段 
ages = pd.pivot_table(df_new,index=[u'age_group',u'silence'],values=['激活时效'],
                      aggfunc=[np.mean,len],fill_value = 0,
                      margins = True,margins_name = '合计')


writer=pd.ExcelWriter(r'G:\work\日报\短信反馈\分类激活\\' + today_file + fold + '各激活占比.xlsx')

ages.to_excel(writer,sheet_name='年龄段')
category.to_excel(writer,sheet_name='分品')
province.to_excel(writer,sheet_name='分省')
#必须运行writer.save()，不然不能输出到本地
writer.save()

