import pandas as pd
import numpy as np
import datetime
import time
import re
print('导入成功')

#设置显示的行、列数
pd.set_option("display.max_columns",200)
#调节参数
date=r"\0619"         #date = 当天月日
date_out='0619'
today="2019-06-19"            #today = 当天年月日
#设置文件路径
file_path_in=r'D:\000-mine\richang2019\原始数据集\0619'
fuzhu_path_in=r'D:\000-mine\richang2019\原始数据集'
file_path_out=r'D:\000-mine\richang2019\导出数据集\0619'
data_dsc='晚待生产.xlsx'
data_ld='晚来单.xlsx'
qudao=r'\集中和分省渠道号简称.xlsx'
biaoka=r'\产品标卡新.xlsx'

#数据导入
data_dsc=pd.read_excel(file_path_in+date+data_dsc,sep='\t',index_col=None,
                   usecols=['订单编号','订单类型','订单状态','订单子状态','订单挂起原因','AB类型',
                            '订单生成时间','号码归属地','收货地址','所在省 / 市 / 县','写卡渠道',
                            '销售品编号','营业厅送货方式','是否线下模式','京东不可达原因'])
data_ld=pd.read_excel(file_path_in+date+data_ld,sep='\t',index_col=None)
qudao=pd.read_excel(fuzhu_path_in+qudao,sheet_name='Sheet3',sep='\t',index_col=None)
biaoka=pd.read_excel(fuzhu_path_in+biaoka,sheet_name='Sheet1',sep='\t',index_col=None)
print('数据导入')

# 匹配渠道号简称
data_dsc=pd.merge(data_dsc,qudao,how='left',on='写卡渠道')
data_ld=pd.merge(data_ld,qudao,how='left',on='写卡渠道')
# 匹配产品标卡
data_dsc =pd.merge(data_dsc,biaoka,how='left',on='销售品编号')
data_ld=pd.merge(data_ld,biaoka,how='left',on='销售品编号')


#晚待生产表，删除‘产品分类’列、‘收货地址’列\'所在省 / 市 / 县'有缺失值的所有行
data_dsc.dropna(subset=['产品分类','收货地址','所在省 / 市 / 县'],inplace=True)
#删除“产品分类”中包含‘新装’的所有行
data_dsc=data_dsc[~data_dsc['产品分类'].isin(['新装'])]
# 删除‘收货地址’列中含有‘测试’的行
data_dsc=data_dsc[~data_dsc['收货地址'].str.contains('测试地址请勿发货|测试号码请勿发货|^.*测试地址不发货$|^.*测试$',regex=True)]
# 删除‘号码归属地’列中含有‘/’的行
data_dsc=data_dsc[~data_dsc['号码归属地'].isin(['/'])]
#删除‘所在省 / 市 / 县’列中含有‘//’的行
data_dsc=data_dsc[~data_dsc['所在省 / 市 / 县'].str.contains('^//$',regex=True)]  
#删除"订单挂起原因"列的值不为空,且'订单状态'列的值为“系统审核订单”的所有行数据
y=data_dsc[data_dsc['订单状态'].isin(['系统审核订单']) & data_dsc['订单挂起原因'].notnull().values==True].index.tolist()
data_dsc=data_dsc.drop(y)
#订单编号去重
data_dsc.drop_duplicates(subset=['订单编号'],keep='last',inplace=True)
#晚来单表，删除‘产品分类’列有缺失值的所有行和‘所在省 / 市 / 县’列为空的行
data_ld.dropna(subset=['产品分类','所在省 / 市 / 县'],inplace=True)
#删除'订单状态'为'办理成功'、'办理中'、'办理失败'的行
data_ld=data_ld[~data_ld['订单状态'].str.contains('办理成功|办理中|办理失败')]
print('数据删除结束')

#查看‘收货地址’列中是否包含有‘测试’的正常地址
print(data_dsc[data_dsc['收货地址'].str.contains('测试')])
#查看‘号码归属地’列和‘所在省 / 市 / 县’中是否包含有‘/’和‘//’的行
print(data_dsc[data_dsc['号码归属地'].isin(['/'])])
print(data_dsc[data_dsc['所在省 / 市 / 县'].str.contains('^//$',regex=True)])

#晚待生产表，添加‘号码归属省’列
data_dsc_add=pd.DataFrame((x.split('/') for x in data_dsc['号码归属地']),index=data_dsc.index,columns=['号码归属省','号码归属市'])
data_dsc=data_dsc.join(data_dsc_add)
data_dsc.drop(['号码归属市'],axis=1,inplace=True)  #删除无用的“号码归属市”列
print(data_dsc.info())
dsc_mingxi=data_dsc    #留做明细

#晚待生产，初步数据处理完成，接下来进行4张欲输出表的数据处理
#16：00“面对面”表中，“订单状态”列保留“交易完成”的行，而“晚待生产-面对面”表中，#删除订单状态为“交易完成”的行
data_dsc_16=data_dsc
print(data_dsc_16['订单状态'].value_counts())
#删除“晚待生产-面对面”表中，订单状态为“交易完成”的行
dai_shengchan=data_dsc[~data_dsc['订单状态'].isin(['交易完成'])]
print(dai_shengchan['订单状态'].value_counts())

#晚待生产表，筛选线上线下数据
#'是否线下模式'列为空值的是“线上”，非空值的为“线下”
data_dsc_xianxia=dai_shengchan.dropna(subset=['是否线下模式'])
data_dsc_xianxia=data_dsc_xianxia[~data_dsc_xianxia['省份'].str.contains('福建')]    #线下表去掉“省份”为“福建”的行数据
data_dsc_xianshang=dai_shengchan[dai_shengchan['是否线下模式'].isnull()]
#16：00面对面、盲投表
MDM_16=data_dsc_16.dropna(subset=['是否线下模式'])
MDM_16=MDM_16[~MDM_16['省份'].str.contains('福建')]
MT_16=data_dsc_16[data_dsc_16['是否线下模式'].isnull()]
#“待生产表”线下面对面透视，索引列为“写卡渠道下匹配的——省份”
xianxia_mdm=pd.pivot_table(data_dsc_xianxia,index=["写卡渠道","省份"],
                           columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
#“待生产表”线上盲投透视，索引列为“写卡渠道下匹配的——省份”
xianshang_mt=pd.pivot_table(data_dsc_xianshang,index=["写卡渠道","省份"],
                            columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
#16:00面对面透视
#16:00"面对面"表的索引列为“号码归属省”，而16：00“盲投”表的索引列仍为“写卡渠道下匹配的——省份”
MDM_16_last=pd.pivot_table(MDM_16,index=["号码归属省"],
                           columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
MT_16_last=pd.pivot_table(MT_16,index=["省份"],
                          columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
#午来单表，筛选线上线下数据
#'是否线下模式'列为空值的是“线上”，非空值的为“线下”
data_ld_xianxia=data_ld.dropna(subset=['是否线下模式'])
data_ld_xianshang=data_ld[data_ld['是否线下模式'].isnull()]
#盲投分产品   (盲投指：线上)
mangtou_fenchan=pd.pivot_table(data_ld_xianshang,index=['产品分类'],
                               values=['订单编号'],aggfunc=[len],margins=True)
#面对面分产品 (面对面：指：线下)
mdm_fenchan=pd.pivot_table(data_ld_xianxia,index=['产品分类'],
                           values=['订单编号'],aggfunc=[len],margins=True)
#盲投分省   (盲投指：线上)
mangtou_fensheng=pd.pivot_table(data_ld_xianshang,index=['省份'],
                                values=['订单编号'],aggfunc=[len],margins=True)
#面对面分省 (面对面：指：线下)
mdm_fensheng=pd.pivot_table(data_ld_xianxia,index=['省份'],
                            values=['订单编号'],aggfunc=[len],margins=True)

#晚待生产表，写入Excel表格
writer1=pd.ExcelWriter(file_path_out+date+'晚待生产.xlsx')
xianxia_mdm.to_excel(writer1,sheet_name=date_out+'晚待生产-面对面')
xianshang_mt.to_excel(writer1,sheet_name=date_out+'晚待生产-盲投')
MDM_16_last.to_excel(writer1,sheet_name='16点面对面')
MT_16_last.to_excel(writer1,sheet_name='16点盲投')
writer1.save()
#早来单表，写入表格
writer2=pd.ExcelWriter(file_path_out+date+'晚来单.xlsx')  
mangtou_fenchan.to_excel(writer2,sheet_name='盲投分产品')
mdm_fenchan.to_excel(writer2,sheet_name='面对面分产品')
mangtou_fensheng.to_excel(writer2,sheet_name='盲投分省')
mdm_fensheng.to_excel(writer2,sheet_name='面对面分省')
writer2.save()

#晚待生产，读入初步处理的数据源
df1=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name=date_out+'晚待生产-面对面',
              index_col=None,header=0,skiprows=[0,1,3])
df2=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name=date_out+'晚待生产-盲投',
              index_col=None,header=0,skiprows=[0,1,3])
df3=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name='16点面对面',
                  index_col=None,header=0,skiprows=[0,1,3])
df4=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name='16点盲投',
                 index_col=None,header=0,skiprows=[0,1,3])
#晚来单，读入初步处理的数据源 
df5=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='盲投分产品',
              index_col=None,header=None,skiprows=3)
df6=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='面对面分产品',
              index_col=None,header=None,skiprows=3)
df7=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='盲投分省',
              index_col=None,header=None,skiprows=3)
df8=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='面对面分省',
              index_col=None,header=None,skiprows=3)

#晚待生产，重命名列名和局部值替换
df1.rename(columns={'Unnamed: 0':'写卡渠道','订单状态':'省份','All':'总计'},inplace=True)
df1.replace('All','总计',inplace=True)
df2.rename(columns={'Unnamed: 0':'写卡渠道','订单状态':'省份','All':'总计'},inplace=True)
df2.replace('All','总计',inplace=True)
df3.rename(columns={'订单状态':'省份'},inplace=True)
df3.replace('All','总计',inplace=True)
df4.rename(columns={'订单状态':'省份'},inplace=True)
df4.replace('All','总计',inplace=True)
#删除df3和df4表中‘All’列
df3.drop('All',axis=1,inplace=True)
df4.drop('All',axis=1,inplace=True)
#晚来单
df5.rename({0:'产品分类',1:'来单量'},axis=1,inplace=True)
df5.replace('All','总计',inplace=True)
df6.rename({0:'产品分类',1:'来单量'},axis=1,inplace=True)
df6.replace('All','总计',inplace=True)
df7.rename({0:'省份',1:'来单量'},axis=1,inplace=True)
df7.replace('All','总计',inplace=True)
df8.rename({0:'省份',1:'来单量'},axis=1,inplace=True)
df8.replace('All','总计',inplace=True)
#晚待生产表，增加“已发货占比”
df1['已发货']=df1['已发货'].fillna(0)
df1.eval('已发货占比=已发货/总计',inplace=True)
df1_last=df1.loc[(df1['写卡渠道']=='总计')|(df1['省份']=='北京集中')]
#面对面sheet排序
df1_up=df1.loc[(df1['省份']!='北京集中')&(df1['写卡渠道']!='总计')].sort_values(['已发货占比'],ascending=False)
MDM=df1_up.append(df1_last)
#对'已发货占比'调整数据格式为保留两位小数的%格式
formater = '{:.2%}'.format
MDM['已发货占比']= MDM['已发货占比'].apply(formater)
#增加'开始备货'列
MDM=MDM.reindex(columns=['写卡渠道','省份','已发货','开始备货','系统审核订单','总计','已发货占比'])
df2['已发货']=df2['已发货'].fillna(0)
df2.eval('已发货占比=已发货/总计',inplace=True)
#盲投sheet排序
df2_last=df2.loc[(df2['写卡渠道']=='总计')|(df2['省份']=='北京集中')]
MT=df2.loc[(df2['省份']!='北京集中')&(df2['写卡渠道']!='总计')].sort_values(['已发货占比'],ascending=False)
MT=MT.append(df2_last)
#对'已发货占比'调整数据格式为保留两位小数的%格式
formater = '{:.2%}'.format
MT['已发货占比']= MT['已发货占比'].apply(formater)

#晚待生产sheet排序
#16点“面对面”和“盲投”表处理
#增加“待生产”列，同时删除“系统审核订单”、“开始备货”列，
columns3=df3.columns.values.tolist()
columns4=df4.columns.values.tolist()
df3=df3.fillna(0)   #将df3的空值项填充为0
df4=df4.fillna(0)   #将df4的空值项填充为0
if '开始备货' in columns3:
    df3.eval('待生产=系统审核订单+开始备货',inplace=True)
    df3.drop(['开始备货','系统审核订单'],axis=1,inplace=True)
else:
    df3.eval('待生产=系统审核订单',inplace=True)
    df3.drop('系统审核订单',axis=1,inplace=True)
if '开始备货' in columns4:
    df4.eval('待生产=系统审核订单+开始备货',inplace=True)
    df4.drop(['开始备货','系统审核订单'],axis=1,inplace=True)
else:
    df4.eval('待生产=系统审核订单',inplace=True)
    df4.drop('系统审核订单',axis=1,inplace=True)
#筛选df3和df4['省份']!='总计'的行
df3_new=df3.loc[df3['省份']!='总计',:]
df4_SF=df4.loc[df4['省份']!='总计',:] 
#对df4_SF表中“待生产”>"已发货"的项，进行两列的值互换
for i in range(len(df4_SF['待生产'])):
    if df4_SF['待生产'][i]>df4_SF['已发货'][i]:
        df4_SF['待生产'][i],df4_SF['已发货'][i]=df4_SF['已发货'][i],df4_SF['待生产'][i]
    else:
        pass
#正则表达式提取“面对面”表的省份前有效字段
#正则前准备，将“省份”列转为字符串列表
df3_SF=df3.loc[df3['省份']!='总计',['省份']] 
df3_list_SF=df3_SF['省份'].tolist()
print(df3_list_SF)
#正则表达式提取有效字段
import re
last_SF=[]
for each in range(len(df3_list_SF)):
    result=re.findall(u"^\w{2}",df3_list_SF[each])     #提取字符串中前两个字符
    last_SF.extend(result)
   
#将处理好的字段重新还原为DataFrame
df3_left=pd.DataFrame(last_SF,index=df3_new.index,columns=['省份'])
df3_left['省份'].replace({'黑龙':'黑龙江','内蒙':'内蒙古'},inplace=True)
#提取df3除“省份”之外的列
df3_right=df3.loc[:,['交易完成','已发货','待生产']]
df3_last=df3_left.join(df3_right)
#"面对面"表按照“已发货”降序排列,“总计”行不参与排序
df3_zongji=df3.loc[df3['省份']=='总计']
MDM_16=df3_last.loc[(df3_last['省份']!='北京集中')&(df3['省份']!='总计')].sort_values(['已发货'],ascending=False)
MDM_16_last=MDM_16.append(df3_zongji)
#“盲投”表按照“面对面”表的省份进行对应排序
#先将df4_SF根据是否在df3的省份列表中拆为上、下两部分，上部分的数据在df3中，下部的数据不在df3中
col_3=MDM_16['省份'].tolist()
print(col_3)
#先将df4_SF根据是否在df3的省份列表中拆为上、下两部分，上部分的数据在df3中，下部的数据不在df3中
df4_up=pd.DataFrame()
df4_down=pd.DataFrame()
for i in range(len(df4_SF['省份'])):
    if str(df4_SF.at[i,'省份']) in col_3:
        df4_up=df4_up.append(df4_SF.loc[i,:])
#         print(str(df4_SF.at[i,'省份']))
    else:
        df4_down=df4_down.append(df4_SF.loc[i,:])
#在df4_up中插入缺失的df3的"省份"项
col_4_up=df4_up['省份'].tolist()
print(col_4_up)
for i in range(len(MDM_16['省份'])):
    if str(MDM_16.at[i,'省份']) in col_4_up:
        pass
#         print(str(MDM_16.at[i,'省份']))
    else:
        df4_up=df4_up.append(MDM_16.loc[i,['省份']])        
#自定义排序顺序
rule=MDM_16['省份'].tolist()
print(rule)
#对相关列进行自定义排序
df4_up['省份']=df4_up['省份'].astype('category').cat.set_categories(rule)
#结果
df4_up=df4_up.sort_values(by=['省份'],ascending=True)
#将df4_up和df4_down合成为新的MT_16表
MT_16_last=df4_up.append(df4_down)
#MT_16_last表重新修改列名顺序
col_order=['省份','已发货','待生产']
MT_16_last=MT_16_last[col_order]
MT_16_last=MT_16_last.fillna(0)
#计算各行数据总和并作为新行添加到末尾
MT_16_last.loc['总计']=MT_16_last.loc[:,['已发货','待生产']].apply(lambda x: x.sum())
MT_16_last.loc['总计',['省份']]='总计'  #补全“省份”最后一行的“总计”名称

#晚来单，排序
df5_last=df5.loc[df5['产品分类']=='总计']
MTCP=df5.loc[df5['产品分类']!='总计'].sort_values(['来单量'],ascending=False)
MTCP=MTCP.append(df5_last)
df6_last=df6.loc[df6['产品分类']=='总计']
MDMCP=df6.loc[df6['产品分类']!='总计'].sort_values(['来单量'],ascending=False)
MDMCP=MDMCP.append(df6_last)
df7_last=df7.loc[(df7['省份']=='总计')|(df7['省份']=='北京集中')]
MTFS=df7.loc[(df7['省份']!='北京集中')&(df7['省份']!='总计')].sort_values(['来单量'],ascending=False)
MTFS=MTFS.append(df7_last)
df8_last=df8.loc[(df8['省份']=='总计')|(df8['省份']=='北京集中')]
MDMFS=df8.loc[(df8['省份']!='北京集中')&(df8['省份']!='总计')].sort_values(['来单量'],ascending=False)
MDMFS=MDMFS.append(df8_last)

#晚待生产写入Excel表格
writer3=pd.ExcelWriter(file_path_out+date+'晚待生产.xlsx')
MDM.to_excel(writer3,sheet_name=date_out+'晚待生产-面对面',index=False)
MT.to_excel(writer3,sheet_name=date_out+'晚待生产-盲投',index=False)
MDM_16_last.to_excel(writer3,sheet_name='16点-面对面',index=False)
MT_16_last.to_excel(writer3,sheet_name='16点-盲投',index=False)
dsc_mingxi.to_excel(writer3,sheet_name='晚待生产明细',index=False)
writer3.save()
#晚来单写入表格
writer4=pd.ExcelWriter(file_path_out+date+'晚来单.xlsx')  
MTCP.to_excel(writer4,sheet_name='盲投分产品',index=False)
MDMCP.to_excel(writer4,sheet_name='面对面分产品',index=False)
MTFS.to_excel(writer4,sheet_name='盲投分省',index=False)
MDMFS.to_excel(writer4,sheet_name='面对面分省',index=False)
data_ld.to_excel(writer4,sheet_name='晚来单明细',index=False)
writer4.save()











