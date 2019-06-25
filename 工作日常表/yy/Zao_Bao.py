import pandas as pd
import numpy as np
import datetime
import time
print('导入成功')

#设置显示的行、列数
pd.set_option("display.max_columns",200)
#调节参数
date=r"\0619"         #date = 当天月日
date_out='0619'
today="2019-06-19"            #today = 当天年月日
zaoyiliu='2019-06-18 16:00:00'        #yesterday = 昨天年月日,16:00:00
#设置文件路径
file_path_in=r'D:\000-mine\richang2019\原始数据集\0619'
fuzhu_path_in=r'D:\000-mine\richang2019\原始数据集'
file_path_out=r'D:\000-mine\richang2019\导出数据集\0619'
data_dsc='早待生产.xlsx'
data_ld='早来单.xlsx'
qudao=r'\集中和分省渠道号简称.xlsx'
biaoka=r'\产品标卡新.xlsx'

#导入数据
data_dsc=pd.read_excel(file_path_in+date+data_dsc,sep='\t',index_col=None)
data_ld=pd.read_excel(file_path_in+date+data_ld,sep='\t',index_col=None)
qudao=pd.read_excel(fuzhu_path_in+qudao,sheet_name='Sheet3',sep='\t',index_col=None)
biaoka=pd.read_excel(fuzhu_path_in+biaoka,sheet_name='Sheet1',sep='\t',index_col=None)
print('导入成功')


# 删除早待生产表中无用和敏感数据列
data_dsc.drop(["原始订单","取消原因","订单来源","结算状态","支付平台",
           "机价款","店铺","拆单类型","制式类型","订单金额","支付方式",
           "支付流水号","收取卡密号码","支付完成时间","发货时间","物流单回填时间",
           "用户名","QQ号","入网用户姓名","入网身份证号","入网手机号",
           "ICCID","收货人姓名","收货人电话号码","收货人邮箱","邮编",
           "配送方式","营业厅地址","配送时间","优惠劵",
           "优惠券编码","F码","F码名称","产品推荐人","CPS推荐人","订单备注","物流单号",
           "承运商","是否上传签收证明项","预存款发票类别",
           "物品费发票抬头","物品费抬头名称","发票内容","企业税号","用户留言",
           "大小卡类型","卡号","串号","销售品类型","销售品数量","销售品价格","合作商",
           "实际分账金额","套餐","主号码","副号码","现金预存款","可选包","合约补贴",
           "其他","靓号低消","靓号等级","靓号预存款","是否线下转线上","线下转线上原因",
           "营业厅送货iccid","身份证图片1","身份证图片2","身份证图片3","身份证图片4",
           "销售品文本步骤名称","用户选择的步骤内容","销售品名称","安装失败原因",
           "交易完成时间","联系人电话号码","入网人所在省/市/县","物流签收时间",
           "实名信息复核中时间"],axis=1, inplace=True) #,"销售品名称_y"
#,"安装失败原因","交易完成时间","联系人电话号码","入网人所在省/市/县","物流签收时间","实名信息复核中时间",
print("删除完成")

# 匹配渠道号简称
data_dsc=pd.merge(data_dsc,qudao,how='left',on='写卡渠道')
data_ld=pd.merge(data_ld,qudao,how='left',on='写卡渠道')
# 匹配产品标卡
data_dsc =pd.merge(data_dsc,biaoka,how='left',on='销售品编号')
data_ld=pd.merge(data_ld,biaoka,how='left',on='销售品编号')

#早待生产表，删除‘产品分类’列、‘收货地址’列\'所在省 / 市 / 县'有缺失值的所有行
data_dsc.dropna(subset=['产品分类','收货地址','所在省 / 市 / 县'],inplace=True)
#删除“产品分类”中包含‘新装’的所有行
data_dsc=data_dsc[~data_dsc['产品分类'].isin(['新装'])]
# 删除‘收货地址’列中含有‘测试’的行
data_dsc=data_dsc[~data_dsc['收货地址'].str.contains('测试地址请勿发货|测试号码请勿发货|^.*测试地址不发货$',regex=True)]
# 删除‘号码归属地’列中含有‘/’的行
data_dsc=data_dsc[~data_dsc['号码归属地'].isin(['/'])]
#删除‘所在省 / 市 / 县’列中含有‘//’的行
data_dsc=data_dsc[~data_dsc['所在省 / 市 / 县'].str.contains('^//$',regex=True)]  
#删除"订单挂起原因"列的值不为空,且'订单状态'列的值为“系统审核订单”的所有行数据
y=data_dsc[data_dsc['订单状态'].isin(['系统审核订单']) & data_dsc['订单挂起原因'].notnull().values==True].index.tolist()
data_dsc=data_dsc.drop(y)
#订单编号去重
data_dsc.drop_duplicates(subset=['订单编号'],keep='last',inplace=True)
#早来单表，删除‘产品分类’列有缺失值的所有行和‘所在省 / 市 / 县’列为空的行
data_ld.dropna(subset=['产品分类','所在省 / 市 / 县'],inplace=True)
#删除'订单状态'为'办理成功'、'办理中'、'办理失败'的行
data_ld=data_ld[~data_ld['订单状态'].str.contains('办理成功|办理中|办理失败')]
print('数据删除结束')

#早待生产表，透视
ZDSC=pd.pivot_table(data_dsc,index=['写卡渠道','省份'],columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
print("早待生产透视完成")
#早遗留透视表创建
#筛选时间
data_dsc_cp=data_dsc.copy()
data_dsc_cp['订单生成时间']=pd.to_datetime(data_dsc_cp['订单生成时间'])  #修改“订单生成时间”的数据类型
#早报时间节点：7日前至今天9：00，早遗留时间节点：7日前至昨天16：00
data_dsc_cp.sort_values('订单生成时间',inplace=True)
data_dsc_cp.set_index('订单生成时间',inplace=True)   #将'订单生成时间'列设置为索引列
data_dsc_cp=data_dsc_cp.truncate(after=zaoyiliu)    #截取早遗留时间段内的订单
print(data_dsc_cp.tail())   #验证数据筛选无误
#将'订单生成时间'列重置为普通列
data_dsc_cp.reset_index('订单生成时间',inplace=True)
print(data_dsc_cp.info())
ZYL=pd.pivot_table(data_dsc_cp,index=['写卡渠道','省份'],columns=['订单状态'],values=['订单编号'],aggfunc=[len],margins=True)
print("早遗留透视完成")

#早来单表，筛选线上线下数据
#'是否线下模式'列为空值的是“线上”，非空值的为“线下”
data_ld_xianxia=data_ld.dropna(subset=['是否线下模式'])
data_ld_xianshang=data_ld[data_ld['是否线下模式'].isnull()]
#盲投分产品   (盲投指：线上)
mangtou_fenchan=pd.pivot_table(data_ld_xianshang,index=['产品分类'],values=['订单编号'],aggfunc=[len],margins=True)
#面对面分产品 (面对面：指：线下)
mdm_fenchan=pd.pivot_table(data_ld_xianxia,index=['产品分类'],values=['订单编号'],aggfunc=[len],margins=True)
#盲投分省   (盲投指：线上)
mangtou_fensheng=pd.pivot_table(data_ld_xianshang,index=['省份'],values=['订单编号'],aggfunc=[len],margins=True)
#面对面分省 (面对面：指：线下)
mdm_fensheng=pd.pivot_table(data_ld_xianxia,index=['省份'],values=['订单编号'],aggfunc=[len],margins=True)

#早待生产表，写入Excel表格
writer1=pd.ExcelWriter(file_path_out+date+'早待生产.xlsx')
ZDSC.to_excel(writer1,sheet_name=date_out+'早待生产')
ZYL.to_excel(writer1,sheet_name=date_out+'早遗留')
writer1.save()
#早来单表，写入表格
writer2=pd.ExcelWriter(file_path_out+date+'早来单.xlsx')  
mangtou_fenchan.to_excel(writer2,sheet_name='盲投分产品')
mdm_fenchan.to_excel(writer2,sheet_name='面对面分产品')
mangtou_fensheng.to_excel(writer2,sheet_name='盲投分省')
mdm_fensheng.to_excel(writer2,sheet_name='面对面分省')
writer2.save()
#早待生产，读入初步处理的数据源
df1=pd.read_excel(file_path_out+date+'早待生产.xlsx',sheet_name=date_out+'早待生产',
              index_col=None,header=0,skiprows=[0,1,3])
df2=pd.read_excel(file_path_out+date+'早待生产.xlsx',sheet_name=date_out+'早遗留',
              index_col=None,header=0,skiprows=[0,1,3])
#早来单，读入初步处理的数据源 
df3=pd.read_excel(file_path_out+date+'早来单.xlsx',sheet_name='盲投分产品',
              index_col=None,header=None,skiprows=3)
df4=pd.read_excel(file_path_out+date+'早来单.xlsx',sheet_name='面对面分产品',
              index_col=None,header=None,skiprows=3)
df5=pd.read_excel(file_path_out+date+'早来单.xlsx',sheet_name='盲投分省',
              index_col=None,header=None,skiprows=3)
df6=pd.read_excel(file_path_out+date+'早来单.xlsx',sheet_name='面对面分省',
              index_col=None,header=None,skiprows=3)
#重命名列名和局部值替换
df1.rename(columns={'Unnamed: 0':'写卡渠道','订单状态':'省份','All':'总计'},inplace=True)
df1.replace('All','总计',inplace=True)
df2.rename(columns={'Unnamed: 0':'写卡渠道','订单状态':'省份','All':'总计'},inplace=True)
df2.replace('All','总计',inplace=True)
#早来单
df3.rename({0:'产品分类',1:'来单量'},axis=1,inplace=True)
df3.replace('All','总计',inplace=True)
df4.rename({0:'产品分类',1:'来单量'},axis=1,inplace=True)
df4.replace('All','总计',inplace=True)
df5.rename({0:'省份',1:'来单量'},axis=1,inplace=True)
df5.replace('All','总计',inplace=True)
df6.rename({0:'省份',1:'来单量'},axis=1,inplace=True)
df6.replace('All','总计',inplace=True)
#早待生产sheet排序
df1['系统审核订单']=df1['系统审核订单'].fillna(0)
df1_last=df1.loc[(df1['写卡渠道']=='总计')|(df1['省份']=='北京集中')]
zao_dsc=df1.loc[(df1['省份']!='北京集中')&(df1['写卡渠道']!='总计')].sort_values(['系统审核订单'],ascending=False)
zao_dsc=zao_dsc.append(df1_last)
#早遗留sheet排序
df2['系统审核订单']=df2['系统审核订单'].fillna(0)
df2_last=df2.loc[(df2['写卡渠道']=='总计')|(df2['省份']=='北京集中')]
zao_yl=df2.loc[(df2['省份']!='北京集中')&(df2['写卡渠道']!='总计')].sort_values(['系统审核订单'],ascending=False)
zao_yl=zao_yl.append(df2_last)
#早来单，排序
df3_last=df3.loc[df3['产品分类']=='总计']
MTCP=df3.loc[df3['产品分类']!='总计'].sort_values(['来单量'],ascending=False)
MTCP=MTCP.append(df3_last)
df4_last=df4.loc[df4['产品分类']=='总计']
MDMCP=df4.loc[df4['产品分类']!='总计'].sort_values(['来单量'],ascending=False)
MDMCP=MDMCP.append(df4_last)
df5_last=df5.loc[(df5['省份']=='总计')|(df5['省份']=='北京集中')]
MTFS=df5.loc[(df5['省份']!='北京集中')&(df5['省份']!='总计')].sort_values(['来单量'],ascending=False)
MTFS=MTFS.append(df5_last)
df6_last=df6.loc[(df6['省份']=='总计')|(df6['省份']=='北京集中')]
MDMFS=df6.loc[(df6['省份']!='北京集中')&(df6['省份']!='总计')].sort_values(['来单量'],ascending=False)
MDMFS=MDMFS.append(df6_last)
#早待生产写入Excel表格
writer3=pd.ExcelWriter(file_path_out+date+'早待生产.xlsx')
zao_dsc.to_excel(writer3,sheet_name=date_out+'早待生产',index=False)
zao_yl.to_excel(writer3,sheet_name=date_out+'早遗留',index=False)
data_dsc.to_excel(writer3,sheet_name='早待生产明细',index=False)
data_dsc_cp.to_excel(writer3,sheet_name='早遗留明细',index=False)
writer3.save()
#早来单写入表格
writer4=pd.ExcelWriter(file_path_out+date+'早来单.xlsx')  
MTCP.to_excel(writer4,sheet_name='盲投分产品',index=False)
MDMCP.to_excel(writer4,sheet_name='面对面分产品',index=False)
MTFS.to_excel(writer4,sheet_name='盲投分省',index=False)
MDMFS.to_excel(writer4,sheet_name='面对面分省',index=False)
data_ld.to_excel(writer4,sheet_name='早来单明细',index=False)
writer4.save()



