import pandas as pd
from datetime import datetime,timedelta
import zipfile
import os
import time
pd.set_option("display.max_columns",200)


# 批量选择含某文字的列
def get_del_list(n,colname):
    '''

    :param n: 选择列最大个数
    :param colname: 要选择的共同列名
    :return:
    '''
    dayslist = []
    for i in range(1, n + 1)[::-1]: # 倒序
        route_time = colname + str(i)
        dayslist.append(route_time)
    return dayslist



# 将DataFrame每行行转换为list
def get_carrier_list(carrier):
    a = []
    for indexs in carrier.index:
        b = carrier.loc[indexs].values[0:-1]
        c = ' '.join('%s' %id for id in b)
        a.append(c)
    return a

# 去除合表后多余表头
def delcolname(data,colname):
    '''
    删除
    :param data:
    :param colname:
    :return:
    '''
    data = data[data[colname].str.contains(colname) == False]
    return data



# 按指定列分类分成不同表格
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


# 文件压缩
def compress(get_files_path, set_files_path):
    f = zipfile.ZipFile(set_files_path , 'w', zipfile.ZIP_DEFLATED )
    for dirpath, dirnames, filenames in os.walk( get_files_path ):
        fpath = dirpath.replace(get_files_path,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            f.write(os.path.join(dirpath,filename), fpath+filename)
    f.close()  


# 身份证获取性别、生日、年龄

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


# 获取前n日日期
def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:
        result_date = today - datetime.timedelta(days=i)
        d = result_date.strftime('%m.%d')
        before_n_days.append(d)
    return before_n_days

# import numpy as np
a=[1,2,3.4,5]
print(a)
[ 1 2 3 4 5 ]
 
print(a[-1]) ###取最后一个元素
[5]
 
print(a[:-1])  ### 除了最后一个取全部
[ 1 2 3 4 ]
 
print(a[::-1]) ### 取从后向前（相反）的元素
[ 5 4 3 2 1 ]
 
print(a[2::-1]) ### 取从下标为2的元素翻转读取
[ 3 2 1 ]





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




# 指定列变换数据类型
df['订单生成时间'] = df['订单生成时间'].map(lambda x:str(x))
df2['入网手机号'] = df2['入网手机号'].astype("str")
# 删除无签收时间
df["物流签收时间"] = df["物流签收时间"].fillna("无签收时间")

# or
data = data[data[colname].str.contains(colname) == False]
# or
df = df.dropna(column=colname)
df = df[df["所在省 / 市 / 县"].str.contains("^//$",regex=True)]

#去重：收货人电话号码，分类
df = df.drop_duplicates(["分类","收货人电话号码"])
df4 = dft.drop_duplicates(subset=['收货人电话号码'],keep='first')


df_ben['日期'] = pd.to_datetime(df_ben['日期'],errors='coerce')

# 按多列多条件选取行
df['是否线下转线上'] = df['是否线下转线上'].fillna("空")
df['是否线下模式'] = df['是否线下模式'].fillna("空")
ex_list = ['空','是否线下转线上']
df1=df[(df['是否线下模式']=="是")&(df['是否线下转线上'].isin(ex_list))]
df = df.drop(df1.index)

# 数据分组
bins =[-1,10,100] 
df5a['silence'] = pd.cut(df5a['激活时效'],bins,labels=["非沉默用户","沉默用户"])

df_new['age']=now_year-df_new["birthday"].dt.year
bins2 = [0,18,25,35,45,55,200]
df_new['age_group'] = pd.cut(df_new['age'],bins2,
    labels=["18岁及以下","19-25岁",'26-35岁','36-45岁','46-55岁','56岁及以上'])



# groupby小应用
# 分是否激活数据集
dfa = dft[dft["is_null"].str.contains('False')] #激活
dfb = dft[dft["is_null"].str.contains('True')]  #未激活
a_MsgNum = dfa.groupby(by=["收货人电话号码",'分类_x']).agg({"收货人电话号码":"count"})
a_MsgNum = a_MsgNum.rename(columns={'收货人电话号码':"发短信数"})
print(a_MsgNum.shape)
a_MsgNum = a_MsgNum.reset_index()


# 打印空白行
data_kong = data_evening[data_evening['分类'].isnull()]
print('*'*100)
print(data_kong.columns)
print("*"*100)
print("打印为空行{}".format(data_kong[["销售品名称_x","销售品编号"]]))

# #筛选"订单生成日期"中指定日期
data = data.loc[data["订单生成日期"] == yesterday] #改前一日期


# 筛选时间
data["订单生成时间"] = pd.to_datetime(data["订单生成时间"])
data["小时"] = data["订单生成时间"].dt.hour
data["日期"] = data["订单生成时间"].dt.date

data["日期"] = data["日期"].map(lambda x : str(x))
data = data[data["日期"].str.contains(today) == False]
df1 = data[(data["日期"] == yestoday) & (data["小时"] >= 16)]
data = data.drop(df1.index)

# 修正命名
dict = {'焦作市':'河南','河南省':'河南','河北省':'河北','贵州省':'贵州','湖南省':'湖南','广东省':'广东','江苏省':'江苏','山西省':'山西',
        '吉林省':'吉林','山东省':'山东','广西壮族自治区':'广西','湖北省':'湖北','陕西省':'陕西','浙江省':'浙江','福建省':'福建',
        '内蒙古自治区':'内蒙古','云南省':'云南','辽宁省':'辽宁','江西省':'江西','四川省':'四川','黑龙江省':'黑龙江','安徽省':'安徽',
        '甘肃省':'甘肃','西藏自治区':'西藏','青海省':'青海','宁夏回族自治区':'宁夏',
        '海南省':'海南','六安市':'安徽','东莞市':'广东','新疆维吾尔自治区':'新疆'}

df1 = df.replace(dict)

# 保留重复项
df1["重复行"] = df1.duplicated(subset=['配送省份名称','入网用户姓名'],keep=False)
df1.shape
df1["重复行"].value_counts()
df2 = df1[df1["重复行"]==True]
df2.shape

# 去重技巧
df1.shape
df2 = df1.drop_duplicates(subset=['配送省份名称','入网用户姓名'],keep='first')
df2.shape
df3 = df1.drop_duplicates(subset=['配送省份名称','入网用户姓名'],keep=False)
df3.shape
df4 = df2.append(df3).drop_duplicates(subset=['配送省份名称','入网用户姓名'],keep=False)
df4.shape

# 选取数据类型为int和float的列
numeric_features = [c for c in features_data if features_data[c].dtype.kind in ('i', 'f')] # 提取数值类型为整数或浮点数的变量


# dataframe 删除某列中为空的行
1.data["a"] = data["a"].fillna('999') # 先附一个值
droplist = data[data["a"] == '999'].index.tolist() # 找出所在index
data = data.drop(droplist)

2.df1=df1[~df1['a'].isin(['999'])]

3. indexs = list(df[np.isnan(df['just my luck'])].index)
    df = df.drop(indexs)

4.df = df[np.isnan(df['just my luck']) == False]

5.df = df[pd.notnull(df['JD_siteName'])]


# 复杂点的判断语句（发货，签收，激活）
def jihuo(x):
    if x == "交易完成":
        return 1
    else:
        return 0

def qianshou(a,b):
    if a is not np.nan:
        return 1
    elif a is np.nan and b == "交易完成":
        return 1
    else:
        return 0

def fahuo(a,b,c):
    if a is not np.nan:
        return 1
    elif a is np.nan and b == "交易完成":
        return 1
    elif a is np.nan and c is not np.nan:
        return 1
    else:
        return 0
        
data['签收量'] = data.apply(lambda x: qianshou(x["物流签收时间"], x["订单状态"]), axis = 1)

# 合表
import pandas as pd
from os import walk
for root,dirs,files in walk(r'c:\Users\datas',topdown=False):#这里我们的数据都存储在'c:\Users\datas'文件夹下
    print(files)#这里我们可以得到所有的文件名称，files是个list
num = len(files)#改文件夹下所有文件的总数量
alldata = pd.DataFrame() #建立一个空的dataframe
for i in range(num):
    newdata = pd.read_excel(r'c:\Users\datas\%s'%files[i])#读取每个excel文件中的数据
    alldata = alldata.append(newdata)#将每个excel中的数据存储到之前建好的空的dataframe中
writer = pd.ExcelWriter(r'C:\Users\output.xlsx')
alldata.to_excel(writer,'AllData')#这里“AllData”是sheet的名字
writer.save()#执行完这一步之后，合并后的表格就保存在了C:\Users\output.xls中

# 正则省市名称
data["dai"] = data["re_formatted_address_gaode"].str.contains("^.*省\w{1,4}市$",regex=True)

# 分列
split1 = pd.DataFrame((x.split('/') for x in df1['号码归属地']),index=df1.index,columns=['所属省','所属市'])
df1 = pd.merge(df1, split1, left_index=True, right_index=True)

df['key'].apply(lambda x:x[:4]).tolist()

# 计算各列数据总和并作为新列添加到末尾
df['Col_sum'] = df.apply(lambda x: x.sum(), axis=1)
# 计算各行数据总和并作为新行添加到末尾
df.loc['Row_sum'] = df.apply(lambda x: x.sum())
# list转为dataframe
df["randomNum"] = pd.DataFrame(list_random_num)

# 生成随机总数
list_random_num = np.random.randint(0,10000,df.shape[0])

# 查看指定列含空值的行
df[df["submit_time"].isnull().values==True]


# pandas将dataframe里含有空值的行打印出来
df[df.isnull().values==True]

##将周一至周日改为1-7数字
weekDict={'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6,'Sun':7}
data_train["datetime_W"]= data_train["datetime_W"].map(weekDict)