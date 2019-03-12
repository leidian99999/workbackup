use 整月数据更新



alter table dbo.[3.8] add 发货量  int
alter table dbo.[3.8] add 签收量 int
alter table dbo.[3.8] add 激活量 int
alter table dbo.[3.8] add 月拦截量 int

alter table dbo.[3.8] add 所属省 varchar(255)
alter table dbo.[3.8] add 所属市 varchar(255)
alter table dbo.[3.8] add 产品分类 varchar(255)
alter table dbo.[3.8] add 激活时效 varchar(255)
alter table dbo.[3.8] add 性别  varchar(255)

alter table dbo.[3.8] add 签收时效 varchar(255)
alter table dbo.[3.8] add 交付时效 varchar(255)
alter table dbo.[3.8] add 年龄  int
alter table dbo.[3.8] add 配送时效 varchar(255)

alter table dbo.[2.1-2.15数据-2.16取] add 订单号码 varchar(255)

alter table dbo.[3.8] add 线下激活量 int
alter table dbo.[3.8] add 线上激活量 int


alter table dbo.[7月数据-8月23日取] add 快递员 varchar(255)
alter table dbo.[7月数据-8月23日取] add 快递员电话 varchar(255)


alter table dbo.[3.8] add 8月运营商 varchar(255)
alter table dbo.[3.8] add 号段 varchar(255)

alter table dbo.[匹配承运商] add 十月承运商 varchar(255)
alter table dbo.[通讯信息诈骗号码] add 七月订单编号 varchar(255)
alter table dbo.[通讯信息诈骗号码] add 七月订单来源 varchar(255)
alter table dbo.[通讯信息诈骗号码] add 八月收货地址 varchar(255)
alter table dbo.[通讯信息诈骗号码] add 十月收货地址 varchar(255)

alter table  dbo.[10.1-10.22当月激活订单] add 激活时效 varchar(255)
alter table dbo.[11月数据-12.24取] add 城市等级 varchar(255)

alter table dbo.[规则ID充值成功明细] add 七月 varchar(255)
alter table dbo.[规则ID充值成功明细] add 八月 varchar(255)
alter table dbo.[规则ID充值成功明细] add 九月 varchar(255)

alter table dbo.[规则ID充值成功明细] add 七月 varchar(255)
alter table dbo.[规则ID充值成功明细] add 八月 varchar(255)
alter table dbo.[规则ID充值成功明细] add 九月 varchar(255)

alter table dbo.[规则ID充值成功明细] add 七月 varchar(255)
alter table dbo.[规则ID充值成功明细] add 八月 varchar(255)
alter table dbo.[规则ID充值成功明细] add 九月 varchar(255)



update dbo.[3.8]
set 发货量=
case 
when 物流单号!='' then 1
when 物流单号='' and 订单状态='交易完成' then 1
when 物流单号='' and 物流签收时间!='' then 1
else 0
end
/*发货量*/

update dbo.[3.8]
set 签收量=
case 
when 物流签收时间!='' then 1
when 物流签收时间='' and 订单状态='交易完成' then 1
else 0
end
/*签收量*/

update dbo.[3.8]
set 激活量=
case 
when 订单状态='交易完成' then 1
else 0
end
/*激活量*/

update dbo.[3.8]
set 月拦截量=
case 
when 发货量=0 and 是否线下转线上!='是'  AND 订单备注 not like '%不要%' and 订单备注 not like '%不需要%' and 订单状态='订单信息审核失败'  then 1
when 发货量=0 and 是否线下转线上!='是'  AND 订单备注 not like '%不要%' and 订单备注 not like '%不需要%' and 订单状态='订单关闭' and 订单挂起原因!='' then 1
when 发货量=0 and 是否线下转线上!='是'  AND 订单备注 not like '%不要%' and 订单备注 not like '%不需要%' and 订单状态='订单关闭' and 订单挂起原因='' and 订单备注!='' and 订单备注 not like '%下发%' then 1
when 发货量=0 and 是否线下转线上!='是'  AND 订单备注 not like '%不要%' and 订单备注 not like '%不需要%' and 订单状态='系统审核订单' and 订单挂起原因!='' then 1
else 0
end
/*月拦截量*/

update dbo.[3.8]
set 日拦截量=
case 
when 发货量=0 and 订单挂起原因='' and 订单状态='订单信息审核失败' then 1
when 发货量=0 and 订单挂起原因!='' then 1
when 发货量=0 and 订单挂起原因='' and 订单状态='身份初审失败' then 1
else 0
end
/*日拦截量*/

update dbo.[3.8]
set 所属省=SUBSTRING(号码归属地,1,(CHARINDEX('/',号码归属地)-1)) 
/*所属省*/
update dbo.[3.8]
set 所属市=SUBSTRING(号码归属地,(CHARINDEX('/',号码归属地)+1),100) 
/*所属市*/


update dbo.[2.1-2.15数据-2.16取]
set 订单号码='A'+订单编号
/*订单号码*/


update dbo.[3.8]
set 产品分类=dbo.[标卡表].分类 from dbo.[标卡表] where dbo.[标卡表].销售品编号=dbo.[3.8].销售品编号
/*产品分类*/




update dbo.[3.8]
set 线下激活量=
case 
when 是否线下模式='是' AND 订单状态='交易完成' AND 是否线下转线上!='是' then 1
else 0
end
/*线下激活量*/

update dbo.[3.8]
set 线上激活量=
case 
when 是否线下模式='是' AND 订单状态='交易完成' AND 是否线下转线上='是' then 1
WHEN 是否线下模式!='是' AND 订单状态='交易完成' then 1
else 0
end
/*线上激活量*/





update dbo.[3.8]
set 激活时效=DATEDIFF(DD, 订单生成时间, 交易完成时间)
/*激活时效*/

update dbo.[3.8]
set 签收时效=DATEDIFF(DD, 订单生成时间, 物流签收时间)
/*签收时效*/

update dbo.[3.8]
set 交付时效=DATEDIFF(DD, 订单生成时间,发货时间)
/*交付时效*/

update dbo.[3.8]
set 配送时效=DATEDIFF(DD, 发货时间, 物流签收时间)
/*配送时效*/


update dbo.[3.8]
set 订单生成日期=substring(订单生成时间,1,10)
/*订单生成日期*/

update dbo.[3.8]
set 订单生成时点=substring (订单生成时间,12,2)
/*订单生成时点*/

update dbo.[3.8]
set 订单生成月份=substring (订单生成时间,6,2)
/*订单生成月份*/

update dbo.[3.8]
set 订单生成年份=substring (订单生成时间,1,4)
/*订单生成年份*/


update dbo.[7月数据-8月23日取]
set 快递员=dbo.[7月物流轨迹].派件人姓名 from dbo.[7月物流轨迹] where dbo.[7月物流轨迹].订单编号=dbo.[7月数据-8月23日取].订单编号
/*快递员*/


update dbo.[7月数据-8月23日取]
set 快递员电话=dbo.[7月物流轨迹].派件人电话 from dbo.[7月物流轨迹] where dbo.[7月物流轨迹].订单编号=dbo.[7月数据-8月23日取].订单编号
/*快递员电话*/