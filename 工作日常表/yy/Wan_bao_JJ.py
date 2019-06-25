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

data_dsc=pd.merge(data_dsc,qudao,how='left',on='写卡渠道')
data_ld=pd.merge(data_ld,qudao,how='left',on='写卡渠道')
data_dsc =pd.merge(data_dsc,biaoka,how='left',on='销售品编号')
data_ld=pd.merge(data_ld,biaoka,how='left',on='销售品编号')


data_dsc.dropna(subset=['产品分类','收货地址','所在省 / 市 / 县'],inplace=True)
data_dsc=data_dsc[~data_dsc['产品分类'].isin(['新装'])]
data_dsc=data_dsc[~data_dsc['收货地址'].str.contains('测试地址请勿发货|测试号码请勿发货|^.*测试地址不发货$|^.*测试$',regex=True)]
data_dsc=data_dsc[~data_dsc['号码归属地'].isin(['/'])]
data_dsc=data_dsc[~data_dsc['所在省 / 市 / 县'].str.contains('^//$',regex=True)]  
y=data_dsc[data_dsc['订单状态'].isin(['系统审核订单']) & data_dsc['订单挂起原因'].notnull().values==True].index.tolist()
data_dsc=data_dsc.drop(y)
data_dsc.drop_duplicates(subset=['订单编号'],keep='last',inplace=True)
data_ld.dropna(subset=['产品分类','所在省 / 市 / 县'],inplace=True)
data_ld=data_ld[~data_ld['订单状态'].str.contains('办理成功|办理中|办理失败')]
print('数据删除结束')

data_dsc_add=pd.DataFrame((x.split('/') for x in data_dsc['号码归属地']),index=data_dsc.index,columns=['号码归属省','号码归属市'])
data_dsc=data_dsc.join(data_dsc_add)
data_dsc.drop(['号码归属市'],axis=1,inplace=True)  
dsc_mingxi=data_dsc

data_dsc_16=data_dsc
dai_shengchan=data_dsc[~data_dsc['订单状态'].isin(['交易完成'])]
data_dsc_xianxia=dai_shengchan.dropna(subset=['是否线下模式'])
data_dsc_xianxia=data_dsc_xianxia[~data_dsc_xianxia['省份'].str.contains('福建')]  
data_dsc_xianshang=dai_shengchan[dai_shengchan['是否线下模式'].isnull()]
MDM_16=data_dsc_16.dropna(subset=['是否线下模式'])
MDM_16=MDM_16[~MDM_16['省份'].str.contains('福建')]
MT_16=data_dsc_16[data_dsc_16['是否线下模式'].isnull()]
xianxia_mdm=pd.pivot_table(data_dsc_xianxia,index=["写卡渠道","省份"],
                           columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
xianshang_mt=pd.pivot_table(data_dsc_xianshang,index=["写卡渠道","省份"],
                            columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
MDM_16_last=pd.pivot_table(MDM_16,index=["号码归属省"],
                           columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
MT_16_last=pd.pivot_table(MT_16,index=["省份"],
                          columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
data_ld_xianxia=data_ld.dropna(subset=['是否线下模式'])
data_ld_xianshang=data_ld[data_ld['是否线下模式'].isnull()]
mangtou_fenchan=pd.pivot_table(data_ld_xianshang,index=['产品分类'],
                               values=['订单编号'],aggfunc=[len],margins=True)
mdm_fenchan=pd.pivot_table(data_ld_xianxia,index=['产品分类'],
                           values=['订单编号'],aggfunc=[len],margins=True)
mangtou_fensheng=pd.pivot_table(data_ld_xianshang,index=['省份'],
                                values=['订单编号'],aggfunc=[len],margins=True)
mdm_fensheng=pd.pivot_table(data_ld_xianxia,index=['省份'],
                            values=['订单编号'],aggfunc=[len],margins=True)

writer1=pd.ExcelWriter(file_path_out+date+'晚待生产.xlsx')
xianxia_mdm.to_excel(writer1,sheet_name=date_out+'晚待生产-面对面')
xianshang_mt.to_excel(writer1,sheet_name=date_out+'晚待生产-盲投')
MDM_16_last.to_excel(writer1,sheet_name='16点面对面')
MT_16_last.to_excel(writer1,sheet_name='16点盲投')
writer1.save()
writer2=pd.ExcelWriter(file_path_out+date+'晚来单.xlsx')  
mangtou_fenchan.to_excel(writer2,sheet_name='盲投分产品')
mdm_fenchan.to_excel(writer2,sheet_name='面对面分产品')
mangtou_fensheng.to_excel(writer2,sheet_name='盲投分省')
mdm_fensheng.to_excel(writer2,sheet_name='面对面分省')
writer2.save()

df1=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name=date_out+'晚待生产-面对面',
              index_col=None,header=0,skiprows=[0,1,3])
df2=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name=date_out+'晚待生产-盲投',
              index_col=None,header=0,skiprows=[0,1,3])
df3=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name='16点面对面',
                  index_col=None,header=0,skiprows=[0,1,3])
df4=pd.read_excel(file_path_out+date+'晚待生产.xlsx',sheet_name='16点盲投',
                 index_col=None,header=0,skiprows=[0,1,3]) 
df5=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='盲投分产品',
              index_col=None,header=None,skiprows=3)
df6=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='面对面分产品',
              index_col=None,header=None,skiprows=3)
df7=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='盲投分省',
              index_col=None,header=None,skiprows=3)
df8=pd.read_excel(file_path_out+date+'晚来单.xlsx',sheet_name='面对面分省',
              index_col=None,header=None,skiprows=3)
df1.rename(columns={'Unnamed: 0':'写卡渠道','订单状态':'省份','All':'总计'},inplace=True)
df1.replace('All','总计',inplace=True)
df2.rename(columns={'Unnamed: 0':'写卡渠道','订单状态':'省份','All':'总计'},inplace=True)
df2.replace('All','总计',inplace=True)
df3.rename(columns={'订单状态':'省份'},inplace=True)
df3.replace('All','总计',inplace=True)
df4.rename(columns={'订单状态':'省份'},inplace=True)
df4.replace('All','总计',inplace=True)
df3.drop('All',axis=1,inplace=True)
df4.drop('All',axis=1,inplace=True)
df5.rename({0:'产品分类',1:'来单量'},axis=1,inplace=True)
df5.replace('All','总计',inplace=True)
df6.rename({0:'产品分类',1:'来单量'},axis=1,inplace=True)
df6.replace('All','总计',inplace=True)
df7.rename({0:'省份',1:'来单量'},axis=1,inplace=True)
df7.replace('All','总计',inplace=True)
df8.rename({0:'省份',1:'来单量'},axis=1,inplace=True)
df8.replace('All','总计',inplace=True)
df1['已发货']=df1['已发货'].fillna(0)
df1.eval('已发货占比=已发货/总计',inplace=True)
df1_last=df1.loc[(df1['写卡渠道']=='总计')|(df1['省份']=='北京集中')]
df1_up=df1.loc[(df1['省份']!='北京集中')&(df1['写卡渠道']!='总计')].sort_values(['已发货占比'],ascending=False)
MDM=df1_up.append(df1_last)
formater = '{:.2%}'.format
MDM['已发货占比']= MDM['已发货占比'].apply(formater)
MDM=MDM.reindex(columns=['写卡渠道','省份','已发货','开始备货','系统审核订单','总计','已发货占比'])
df2['已发货']=df2['已发货'].fillna(0)
df2.eval('已发货占比=已发货/总计',inplace=True)
df2_last=df2.loc[(df2['写卡渠道']=='总计')|(df2['省份']=='北京集中')]
MT=df2.loc[(df2['省份']!='北京集中')&(df2['写卡渠道']!='总计')].sort_values(['已发货占比'],ascending=False)
MT=MT.append(df2_last)
formater = '{:.2%}'.format
MT['已发货占比']= MT['已发货占比'].apply(formater)
columns3=df3.columns.values.tolist()
columns4=df4.columns.values.tolist()
df3=df3.fillna(0)   
df4=df4.fillna(0)   
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
df3_new=df3.loc[df3['省份']!='总计',:]
df4_SF=df4.loc[df4['省份']!='总计',:] 
for i in range(len(df4_SF['待生产'])):
    if df4_SF['待生产'][i]>df4_SF['已发货'][i]:
        df4_SF['待生产'][i],df4_SF['已发货'][i]=df4_SF['已发货'][i],df4_SF['待生产'][i]
    else:
        pass
df3_SF=df3.loc[df3['省份']!='总计',['省份']] 
df3_list_SF=df3_SF['省份'].tolist()
last_SF=[]
for each in range(len(df3_list_SF)):
    result=re.findall(u"^\w{2}",df3_list_SF[each])    
    last_SF.extend(result)

df3_left=pd.DataFrame(last_SF,index=df3_new.index,columns=['省份'])
df3_left['省份'].replace({'黑龙':'黑龙江','内蒙':'内蒙古'},inplace=True)
df3_right=df3.loc[:,['交易完成','已发货','待生产']]
df3_last=df3_left.join(df3_right)
df3_zongji=df3.loc[df3['省份']=='总计']
MDM_16=df3_last.loc[(df3_last['省份']!='北京集中')&(df3['省份']!='总计')].sort_values(['已发货'],ascending=False)
MDM_16_last=MDM_16.append(df3_zongji)
col_3=MDM_16['省份'].tolist()
df4_up=pd.DataFrame()
df4_down=pd.DataFrame()
for i in range(len(df4_SF['省份'])):
    if str(df4_SF.at[i,'省份']) in col_3:
        df4_up=df4_up.append(df4_SF.loc[i,:])
    else:
        df4_down=df4_down.append(df4_SF.loc[i,:])
col_4_up=df4_up['省份'].tolist()
for i in range(len(MDM_16['省份'])):
    if str(MDM_16.at[i,'省份']) in col_4_up:
        pass
    else:
        df4_up=df4_up.append(MDM_16.loc[i,['省份']])        
rule=MDM_16['省份'].tolist()
df4_up['省份']=df4_up['省份'].astype('category').cat.set_categories(rule)
df4_up=df4_up.sort_values(by=['省份'],ascending=True)
MT_16_last=df4_up.append(df4_down)
col_order=['省份','已发货','待生产']
MT_16_last=MT_16_last[col_order]
MT_16_last=MT_16_last.fillna(0)
MT_16_last.loc['总计']=MT_16_last.loc[:,['已发货','待生产']].apply(lambda x: x.sum())
MT_16_last.loc['总计',['省份']]='总计'  
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

#写入Excel表格
writer3=pd.ExcelWriter(file_path_out+date+'晚待生产.xlsx')
MDM.to_excel(writer3,sheet_name=date_out+'晚待生产-面对面',index=False)
MT.to_excel(writer3,sheet_name=date_out+'晚待生产-盲投',index=False)
MDM_16_last.to_excel(writer3,sheet_name='16点-面对面',index=False)
MT_16_last.to_excel(writer3,sheet_name='16点-盲投',index=False)
dsc_mingxi.to_excel(writer3,sheet_name='晚待生产明细',index=False)
writer3.save()
writer4=pd.ExcelWriter(file_path_out+date+'晚来单.xlsx')  
MTCP.to_excel(writer4,sheet_name='盲投分产品',index=False)
MDMCP.to_excel(writer4,sheet_name='面对面分产品',index=False)
MTFS.to_excel(writer4,sheet_name='盲投分省',index=False)
MDMFS.to_excel(writer4,sheet_name='面对面分省',index=False)
data_ld.to_excel(writer4,sheet_name='晚来单明细',index=False)
writer4.save()











