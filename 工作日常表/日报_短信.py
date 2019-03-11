import pandas as pd
from datetime import datetime,timedelta
import zipfile
import os
import time
pd.set_option("display.max_columns",200)



today = "190213"
file = "02.13"
jintian = datetime(2019,2,13)
disk = "G"
month = "19年2月"

data     = pd.read_excel(disk + ":/work/日报/短信/汇总/原表/" + today +"短信导出.xlsx")
biaoka   = pd.read_excel(disk + ":/work/日报/功能列表/产品标卡.xlsx")
haoduan  = pd.read_excel(disk +":/work/日报/功能列表/运营商号段.xlsx")
outpath  = disk + ":\\work\\日报\\短信\\汇总\\原表简表1\\"+today+"短信导出_字段.xlsx"
outpath1 = disk + ":\\work\\日报\\短信\\输出\\异网全表\\"+month+"\\异网签收未激活去新装去重-"+file+"取数.xlsx"
outpath2 = disk + ":\\work\\日报\\短信\\输出\\本网全表\\"+month+"\\本网签收未激活去新装去重-"+file+"取数.xlsx" #分省前备份

outpath_ben10up   = disk + ":\\work\\日报\\短信\\输出\\本网沉默\\"+month+"\\"+today+"本网沉默用户.xlsx"
outpath_ben10down = disk + ":\\work\\日报\\短信\\输出\\本网非沉默\\"+month+"\\"+today+"本网非沉默用户.xlsx"
outpath_yi10up    = disk + ":\\work\\日报\\短信\\输出\\异网沉默\\"+month+"\\"+today+"异网沉默用户.xlsx"
outpath_yi10down  = disk + ":\\work\\日报\\短信\\输出\\异网非沉默\\"+month+"\\"+today+"异网非沉默用户.xlsx"

writer10up   = disk + ':\\work\\日报\\短信\\'+today+'\\本网\\本10上\\'  #分省分表输出目录

writer10down = disk + ':\\work\\日报\\短信\\'+today+'\\本网\\本10下\\'  #分省分表输出目录

# get_files_path = "G:\\work\\日报\\短信\\"+today+"\\本网\\输出test\\"  # 需要压缩的文件夹
set_files_path_10up   = disk + ":\\work\\日报\\短信\\"+today+"\\本网签收未激活去新装去重沉默-"+file+"取数.zip"  # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样
set_files_path_10down = disk + ":\\work\\日报\\短信\\"+today+"\\本网签收未激活去新装去重非沉默-"+file+"取数.zip"  # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样))

# df =   pd.read_excel(outpath) #报错时用


# 去除多余表头
data = data[data['入网身份证号'].str.contains('入网身份证号') == False]


print("表格读取完毕。。。")

df = data[["订单生成时间",'订单编号','收货人电话号码','收货人姓名',
           '收货地址','物流签收时间','入网手机号','销售品名称','套餐',
           '号码归属地','销售品编号','是否线下模式','是否线下转线上','订单来源','入网身份证号']]


df.to_excel(outpath,index=False)
print("表格保存完毕")



print("表格行列数：" + str(df.shape))


# 区别性别

def get_sex(str1):
    #查看性别
    if str1 % 2 ==0:
        return '女'
    else:
        return '男'

df['性别'] = df["入网身份证号"].str.slice(16,17).map(lambda x:int(x)).apply(get_sex)





# 区分年龄段
df['生日'] = pd.to_datetime(df['入网身份证号'].str[6:14])
now_year =datetime.today().year #当前的年份
df['年龄']=now_year-df["生日"].dt.year


#筛选是否线下模式
df['是否线下转线上'] = df['是否线下转线上'].fillna("空")
df['是否线下模式'] = df['是否线下模式'].fillna("空")
ex_list = ['空','是否线下转线上']
df1=df[(df['是否线下模式']=="是")&(df['是否线下转线上'].isin(ex_list))]
df = df.drop(df1.index)
print("去掉线下后：" + str(df.shape))

# 删除无签收时间
df["物流签收时间"] = df["物流签收时间"].fillna("无签收时间")
df['物流签收时间'] = df['物流签收时间'].map(lambda x:str(x))
df = df[~df['物流签收时间'].str.contains('无签收时间')]
print("删除物流签收时间后，{}行，{}列".format(df.shape[0],df.shape[1]))
print("*"*100)

#分列号码归属地
split = pd.DataFrame((x.split('/') for x in df['号码归属地']), index=df.index, columns=['所属省','地区'])
df = pd.merge(df,split,left_index=True,right_index=True)
print("分列‘号码归属地’后，{}行，{}列".format(df.shape[0],df.shape[1]))
print("*"*100)

# 订单生成时间分列
df['订单生成时间'] = df['订单生成时间'].map(lambda x:str(x))
split2 = pd.DataFrame((x.split(' ') for x in df['订单生成时间']), index=df.index, columns=['日期','订单时间'])
df = pd.merge(df,split2,left_index=True,right_index=True)
print("分列‘订单生成时间’后，{}行，{}列".format(df.shape[0],df.shape[1]))
print("*"*100)

#vlookup产品标卡
df['销售品编号'] = df['销售品编号'].map(lambda x:str(x))
biaoka['销售品编号'] = biaoka['销售品编号'].map(lambda x:str(x))
df = pd.merge(df,biaoka,how="left",on="销售品编号")
print("匹配标卡后，行列数:%s行，%s列" % (df.shape[0],df.shape[1]))
print("*"*100)

#去重：收货人电话号码，分类
df = df.drop_duplicates(["分类","收货人电话号码"])
print("去重：")
print(df.shape)
print("*"*100)

#vlookup号码段
haoduan['号段'] = haoduan['号段'].map(lambda x:str(x))
df["收货人电话号码"] = df["收货人电话号码"].map(lambda x:str(x))
df["号段"] = df["收货人电话号码"].str[0:3]
df = pd.merge(df,haoduan,how="left",on="号段")
print("匹号段后：{}行，{}列".format(df.shape[0],df.shape[1]))
print("*"*100)

#去新装
df['分类'] = df['分类'].map(lambda x:str(x))
df = df[df["分类"].str.contains('新装') == False]

#区分本异网
df["运营商"] = df["运营商"].fillna('miss')
df_ben = df[df['运营商'].str.contains('中国电信')]
df_yi  = df[~df['运营商'].str.contains('中国电信')]

# 本网区分十日上下
df_ben['日期'] = pd.to_datetime(df_ben['日期'],errors='coerce')
df_ben = df_ben[df_ben['日期'].notnull()]
df_ben["天数"] = jintian - df_ben["日期"]
df_ben["天数"] = df_ben["天数"].map(lambda x:x.days)
df_ben["天数"] = df_ben["天数"].map(lambda x:int(x))

df_ben_up10 = df_ben[df_ben["天数"] > 10]
df_ben_down10 = df_ben[df_ben["天数"] <= 10]

# 异网区分十日上下
df_yi['日期'] = pd.to_datetime(df_yi['日期'],errors='coerce')
df_yi = df_yi[df_yi['日期'].notnull()]
df_yi["天数"] = jintian - df_yi["日期"]
df_yi["天数"] = df_yi["天数"].map(lambda x:x.days)


df_yi_up10 = df_yi[df_yi["天数"] > 10]
df_yi_down10 = df_yi[df_yi["天数"] <= 10]

#输出表格并记录
print("输出表单(异网)：{}行，{}列".format(df_yi.shape[0],df_yi.shape[1]))
print("输出表单(本网)：{}行，{}列".format(df_ben.shape[0],df_ben.shape[1]))
print("输出表单(异网沉默)：{}行，{}列".format(df_yi_up10.shape[0],df_yi_up10.shape[1]))
print("输出表单(异网非沉默)：{}行，{}列".format(df_yi_down10.shape[0],df_yi_down10.shape[1]))
print("输出表单(本网沉默)：{}行，{}列".format(df_ben_up10.shape[0],df_ben_up10.shape[1]))
print("输出表单(本网非沉默)：{}行，{}列".format(df_ben_down10.shape[0],df_ben_down10.shape[1]))
print("开始写表")

df_yi.to_excel(outpath1,index=False)
print("异网全表已完成")
df_ben.to_excel(outpath2,index=False)
print("本网全表已完成")
df_yi_up10.to_excel(outpath_yi10up,index=False)
print("异网沉默已完成")
df_yi_down10.to_excel(outpath_yi10down,index=False)
print("异网非沉默已完成")
df_ben_up10.to_excel(outpath_ben10up,index=False)
print("本网沉默已完成")
df_ben_down10.to_excel(outpath_ben10down,index=False)
print("本网非沉默已完成")

#开始分省
def FenSheng(df,col,writer,name):
    print("开始分省")
    print(df[col].value_counts())
    sheng_list = df[col].unique()
    print("*"*100)
    print(sheng_list)

    for sheng in sheng_list:
        df_new = df[df[col] == sheng]
        df_new.to_excel(writer + str(time.strftime("%Y-%m-%d", time.localtime())) +  sheng + name +'.xlsx', index=False)
    print('拆分完成！')
    
#打包起来
def compress(get_files_path, set_files_path):
    f = zipfile.ZipFile(set_files_path , 'w', zipfile.ZIP_DEFLATED )
    for dirpath, dirnames, filenames in os.walk( get_files_path ):
        fpath = dirpath.replace(get_files_path,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            f.write(os.path.join(dirpath,filename), fpath+filename)
    f.close()    
    
# 分省10日上
FenSheng(df_ben_up10,'所属省',writer10up,"本网十日以上沉默用户")
# 分省10日下
FenSheng(df_ben_down10,'所属省',writer10down,"本网十日内非沉默用户")


# 压缩10日上
compress(writer10up, set_files_path_10up)
# 压缩10日下
compress(writer10down, set_files_path_10down)