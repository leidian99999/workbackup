use 整月数据更新

--按省份统计
select 所属省,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取]  WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类 !='新装' group by  所属省 order by  所属省



select 所属省,substring(订单生成时间,1,10),产品分类,
SUM(激活量) 激活量
from dbo.[9月数据-10.26取]  WHERE  产品分类 !='' AND 是否线下模式!='是' group by  所属省,substring(订单生成时间,1,10),产品分类 order by  所属省,substring(订单生成时间,1,10),产品分类





select [所在省 / 市 / 县],substring(订单生成时间,1,10),产品分类,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取]  WHERE 承运商 in ('京东物流','韵达') and 写卡渠道 IN ('100000220','100000155') AND 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !=''  group by  [所在省 / 市 / 县],substring(订单生成时间,1,10),产品分类 order by  [所在省 / 市 / 县],substring(订单生成时间,1,10),产品分类


select *
from dbo.[19年1月数据-2.10取]  WHERE 承运商 in ('京东物流','韵达') and 写卡渠道 IN ('100000220','100000155') AND 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !=''  group by  [所在省 / 市 / 县],substring(订单生成时间,1,10),产品分类 order by  [所在省 / 市 / 县],substring(订单生成时间,1,10),产品分类


--按写卡渠道统计
select 写卡渠道,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取]  WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类 !='新装' group by  写卡渠道 order by  写卡渠道




--按产品分类统计
select 产品分类,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !=''  and 产品分类 !='新装' group by  产品分类 order by  产品分类



--截取时间格式按照日期
select 所属省,
substring(订单生成时间,1,10),
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
 from dbo.[19年1月数据-2.10取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !=''  and 产品分类 !='新装'  group by 所属省,substring(订单生成时间,1,10) order by 所属省,substring(订单生成时间,1,10) 

select 
substring(订单生成时间,1,10),
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
 from dbo.[19年1月数据-2.10取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !=''  and 产品分类 !='新装'    group by substring(订单生成时间,1,10) order by substring(订单生成时间,1,10) 




select 
substring(订单生成时间,1,10),
COUNT(订单编号) 订单量
 from dbo.[10上激活量2]  group by substring(订单生成时间,1,10) order by substring(订单生成时间,1,10) 


--截取订单生成时间格式按照小时
select 所属省,
substring (订单生成时间,12,2),
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
 from dbo.[19年1月数据-2.10取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  group by 所属省,substring(订单生成时间,12,2) order by 所属省,substring(订单生成时间,12,2)

select 
substring (订单生成时间,12,2),
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
 from dbo.[19年1月数据-2.10取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  group by substring(订单生成时间,12,2) order by substring(订单生成时间,12,2)



--截取物流签收时间格式按照小时
select 所属省,
substring(物流签收时间,12,2),
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
 from dbo.[19年1月数据-2.10取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  and 物流签收时间!='' group by 所属省,substring(物流签收时间,12,2) order by 所属省,substring(物流签收时间,12,2)

select 
substring(物流签收时间,12,2),
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
 from dbo.[19年1月数据-2.10取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  and 物流签收时间!='' group by substring(物流签收时间,12,2) order by substring(物流签收时间,12,2)



--按省地市统计
select 
所属省,所属市,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
 from dbo.[19年1月数据-2.10取] WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'   group by 所属省,所属市 order by 所属省,所属市


select 
所属省,所属市,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量,
SUM(月拦截量) 拦截量
 from dbo.[19年1月数据-2.10取] WHERE 订单生成时间  between '2018-10-01 00:00:00' and '2018-11-01 00:00:00' and  产品分类!=''  and 产品分类!='新装'  group by 所属省,所属市 order by 所属省,所属市


--按省产品统计
select 
所属省,产品分类,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  group by 所属省,产品分类 order by 所属省,产品分类

--按所在省市县统计
select [所在省 / 市 / 县],
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  group by  [所在省 / 市 / 县] order by  [所在省 / 市 / 县]

select [所在省 / 市 / 县],写卡渠道,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE   订单生成时间  between '2018-09-01 00:00:00' and '2018-10-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  group by  [所在省 / 市 / 县], 写卡渠道 order by  [所在省 / 市 / 县],写卡渠道




--按写卡渠道
select 写卡渠道,[所在省 / 市 / 县],
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE   订单生成时间  between '2018-09-01 00:00:00' and '2018-10-01 00:00:00' and 产品分类 !='' and 产品分类!='新装'  group by  写卡渠道,[所在省 / 市 / 县] order by 写卡渠道,[所在省 / 市 / 县]


select 写卡渠道,[所在省 / 市 / 县],
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[10月数据-12.2取数] WHERE   订单生成时间  between '2018-10-01 00:00:00' and '2018-11-01 00:00:00' and 产品分类 !=''  group by  写卡渠道,[所在省 / 市 / 县] order by 写卡渠道,[所在省 / 市 / 县]

select 所属省,写卡渠道,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE   订单生成时间  between '2018-12-01 00:00:00' and '2019-11-01 00:00:00' and 产品分类 !=''  and 产品分类!='新装'  group by  所属省,写卡渠道 order by 所属省,写卡渠道



--按省写卡渠道
select 所属省,写卡渠道,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and 产品分类!='新装' group by 所属省, 写卡渠道 order by 所属省,写卡渠道


select 写卡渠道,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00'  and 产品分类 !=''  and 产品分类!='新装' group by 写卡渠道 order by 写卡渠道


select 写卡渠道,所属省,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取] WHERE 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !=''  and 产品分类!='新装' group by  写卡渠道 ,所属省 order by 写卡渠道,所属省







 ---运营商
select 运营商,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取]  WHERE 订单生成时间  between '2018-09-01 00:00:00' and '2018-10-01 00:00:00' and 产品分类 !=''  group by  运营商 order by  运营商

 ---V4
SELECT 产品分类,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量 FROM dbo.[19年1月数据-2.10取] 
WHERE 产品分类 in ('斗鱼卡','翼视卡','花粉卡','光芒卡','欢聚卡','聚力卡','农行卡','荣耀体验卡','新装','雅听卡','小乐卡','阿里宝卡')
GROUP BY 产品分类
ORDER BY 产品分类

SELECT 产品分类,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量 FROM dbo.[19年1月数据-2.10取] 
WHERE 产品分类 in ('斗鱼卡','翼视卡','花粉卡','光芒卡','欢聚卡','聚力卡','农行卡','荣耀体验卡','新装','雅听卡','小乐卡','阿里宝卡') OR 销售品名称 like '%潮玩%'
GROUP BY 产品分类
ORDER BY 产品分类

SELECT 产品分类,substring(订单生成时间,1,10),
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量 FROM dbo.[19年1月数据-2.10取] 
WHERE 产品分类 in ('斗鱼卡','翼视卡','花粉卡','光芒卡','欢聚卡','聚力卡','农行卡','荣耀体验卡','新装','雅听卡','小乐卡')
GROUP BY 产品分类,substring(订单生成时间,1,10)
ORDER BY 产品分类,substring(订单生成时间,1,10)


SELECT 所属市,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量 FROM dbo.[19年1月数据-2.10取] 
WHERE 所属省='吉林省' and 写卡渠道='100000155' AND 产品分类='米粉卡体验' AND 订单生成时间 between '2018-09-03 00:00:00' and '2018-09-04 00:00:00'  
GROUP BY 所属市
ORDER BY 所属市


SELECT [所在省 / 市 / 县],
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量 FROM dbo.[19年1月数据-2.10取] 
WHERE 所属省='吉林省' and 产品分类='米粉卡体验' and 写卡渠道='100000155' AND 订单生成时间 between '2018-09-03 00:00:00' and '2018-09-04 00:00:00'  
GROUP BY [所在省 / 市 / 县]
ORDER BY [所在省 / 市 / 县]

SELECT *  FROM dbo.[19年1月数据-2.10取] 
WHERE 产品分类 in ('斗鱼卡','翼视卡','花粉卡','光芒卡','欢聚卡','聚力卡','农行卡','荣耀体验卡','新装','雅听卡','小乐卡')

SELECT * FROM dbo.[19年1月数据-2.10取] 
WHERE 所属省='吉林省'  AND 产品分类='米粉卡体验' AND 订单生成时间 between '2018-09-03 00:00:00' and '2018-09-04 00:00:00'  
GROUP BY 所属市
ORDER BY 所属市


select  substring(订单生成时间,1,10),COUNT(订单编号) 订单量
 from dbo.[10.1-10.22当月激活订单] GROUP BY substring(订单生成时间,1,10) ORDER BY substring(订单生成时间,1,10)
 
 select  substring(交易完成时间,1,10),COUNT(订单编号) 订单量
 from dbo.[10.1-10.22当月激活订单] GROUP BY substring(交易完成时间,1,10) ORDER BY substring(交易完成时间,1,10)
 
 SELECT 销售品名称,COUNT(订单编号) 订单量 FROM dbo.[10.1-10.22当月激活订单] WHERE 产品分类 IS NULL AND AB类型='A1' GROUP BY 销售品名称
 
  SELECT * FROM dbo.[10.1-10.22当月激活订单] WHERE 产品分类 IS NULL AND AB类型='A1'
  
  select 激活时效,COUNT(订单编号) 订单量
from dbo.[10.1-10.22当月激活订单]  where 交易完成时间!='' and DATEDIFF(DD, 订单生成时间, 交易完成时间)>=0 and 订单状态='交易完成' and AB类型='A1' and 
 产品分类 !='' and 产品分类!='新装' and 订单生成时间  between '2018-09-15 00:00:00' and '2018-10-01 00:00:00' and 交易完成时间  between '2018-10-10 00:00:00' and '2018-10-23 00:00:00' group by 激活时效
 ORDER BY 激活时效
 
 select 激活时效,SUM(激活量) 激活量
from dbo.[19年1月数据-2.10取]  where 交易完成时间!='' and DATEDIFF(DD, 订单生成时间, 交易完成时间)>=0 and 
 产品分类 !='' and 产品分类!='新装' AND 产品分类 IN ('米粉卡日租','米粉卡体验')  and 订单生成时间  between '2018-09-15 00:00:00' and '2018-10-01 00:00:00' and 交易完成时间  between '2018-09-01 00:00:00' and '2018-10-10 00:00:00' group by 激活时效
 ORDER BY 激活时效
 
 
 select * FROM dbo.[19年1月数据-2.10取原表] WHERE 订单编号='609903837000008318103190155489'
 
 use [11月数据]
select  所属省,SUM(激活量) 激活量 FROM dbo.[11.1-11.29数据-11.29取] WHERE 产品分类 in ('米粉卡会员','米粉卡日租','米粉卡体验') and 激活时效, group by 所属省

 ---城市等级
select 所属省,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[11月数据-12.24取]   WHERE 所属市='市辖区' and 订单生成时间  between '2018-11-01 00:00:00' and '2019-12-01 00:00:00' and 产品分类 !=''  group by 所属省 order by  所属省

select * from dbo.[11月数据-12.24取] where 发货量=0 and 月拦截量=0 

select 城市等级,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[11月数据-12.24取]   WHERE 订单生成时间  between '2018-11-01 00:00:00' and '2019-12-01 00:00:00' and 产品分类 !=''  group by 城市等级 order by  城市等级


S



select COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(签收量) 签收量,
SUM(激活量) 激活量 from dbo.[19年1月数据-2.10取] 
where 收货地址 not like '%街%' 
and 收货地址 not like '%路%' 
and 收货地址 not like '%镇%'
and 收货地址 not like '%乡%' 
and 收货地址 not like '%村%'
and 收货地址 not like '%店%' 
and 收货地址 not like '%城%'
and 收货地址 not like '%学%' 
and 收货地址 not like '%楼%'
and 收货地址 not like '%栋%'
and 收货地址 not like '%厦%' 
and 收货地址 not like '%区%'
and 收货地址 not like '%局%'
and 收货地址 not like '%院%' 
and 收货地址 not like '%园%'
and 收货地址 not like '%道%' 
and 收货地址 not like '%公司%'
and 收货地址 not like '%县%' 
and 收货地址 not like '%超市%'
and 收货地址 not like '%厂%'
and 收货地址 not like '%场%'
and 收货地址 not like '%站%'
and 收货地址 not like '%局%'
and 收货地址 not like '%馆%'
and 收货地址 not like '%中心%'
and 收货地址 not like '%庄%'
and 收货地址 not like '%市%'
and 收货地址 not like '%队%'
and 收货地址 not like '%苑%'
and 收货地址 not like '%所%'
and 收货地址 not like '%银行%'
and 收货地址 not like '%基地%'
and 收货地址 not like '%公寓%'
and 收货地址 not like '%宿舍%'
and 收货地址 not like '%巷%'
and 收货地址 not like '%快递%'
and 收货地址 not like '%中%'
and 收货地址 not like '%期%'
and 收货地址 not like '%居%'
and 收货地址 not like '%座%'
and 收货地址 not like '%集团%'
and 收货地址 not like '%湾%'
and 收货地址 not like '%滩%'
and 收货地址 not like '%单元%'
and 收货地址 not like '%室%'
and 收货地址 not like '%吧%'
and 收货地址 not like '%号%'
and 收货地址 not like '%校%'
and 收货地址 not like '%门%'
and 收货地址 not like '%家%'
and 收货地址 not like '%里%'
and 收货地址 not like '%测试%'
and 收货地址 not like '%府%'
and 收货地址 not like '%幢%'
and 收货地址 not like '%社%'
and 收货地址 not like '%坝%'
and 收货地址 not like '%郡%'
and 收货地址 not like '%铺%'
and 收货地址 not like '%谷%'
and 收货地址 not like '%洲%'
and 收货地址 not like '%堂%'
and 收货地址 not like '%岭%'
and 收货地址 not like '%坊%'
and 收货地址 not like '%屯%'
and 收货地址 not like '%庭%'


select 承运商,快递员,快递员电话,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[7月数据-8月23日取]  WHERE  产品分类 !=''  group by  承运商,快递员,快递员电话 order by  承运商,快递员,快递员电话

select 承运商,快递员,快递员电话,收货地址,
COUNT(订单编号) 订单量,
SUM(发货量) 发货量,
SUM(月拦截量) 拦截量,
SUM(签收量) 签收量,
SUM(激活量) 激活量
from dbo.[11月数据-12.24取]  WHERE  产品分类 !=''  group by  承运商,快递员,快递员电话,收货地址 order by  承运商,快递员,快递员电话,收货地址


select 写卡渠道,
SUM(激活量) 激活量
 from dbo.[12月数据-1.21取] WHERE  交易完成时间!='' and DATEDIFF(DD, 订单生成时间, 交易完成时间)>=0 and 激活时效<=15
and 订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and  产品分类 !='新装' and 是否线下模式!='是'  AND 写卡渠道 in ('100000155','100000693')  group by 写卡渠道 order by 写卡渠道


select 写卡渠道,
SUM(发货量) 发货量,
SUM(激活量) 激活量
 from dbo.[12月数据-1.21取] WHERE  订单生成时间  between '2019-01-01 00:00:00' and '2019-02-01 00:00:00' and 产品分类 !='' and   写卡渠道 in ('100000155','100000693')  group by 写卡渠道 order by 写卡渠道
