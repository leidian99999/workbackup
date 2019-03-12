USE   整月数据更新

GO    
EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'AllowInProcess', 1    
GO    
EXEC master.dbo.sp_MSset_oledb_prop N'Microsoft.ACE.OLEDB.12.0', N'DynamicParameters', 1    
GO   

exec sp_configure "show advanced options",1
reconfigure
exec sp_configure "Ad Hoc Distributed Queries",1
reconfigure
/*开启相关支持选项*/


select * into [1] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [2] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(1).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [3] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(2).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [4] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(3).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [5] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(4).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [6] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(5).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [7] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(6).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [8] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(7).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [9] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(8).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [10] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(9).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [11] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(10).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [12] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(11).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [13] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(12).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [14] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(13).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [15] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(14).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [16] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(15).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [17] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(16).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [18] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(17).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [19] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(18).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [20] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(19).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [21] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(20).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [22] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(21).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [23] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(22).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [24] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(23).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [25] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(24).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [26] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(25).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [27] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(26).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [28] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(27).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [29] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(28).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [30] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(29).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [31] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(30).xls";Extended properties=Excel 12.0' )...Sheet0$




select * into [41] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [42] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(1).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [43] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(2).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [44] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(3).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [45] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(4).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [46] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(5).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [47] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(6).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [48] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(7).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [49] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(8).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [50] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(9).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [51] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(10).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [52] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(11).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [53] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(12).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [54] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(13).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [55] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(14).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [56] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(15).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [57] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(16).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [58] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(17).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [59] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(18).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [60] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(19).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [61] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(20).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [62] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(21).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [63] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(22).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [64] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(23).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [65] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(24).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [66] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(25).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [67] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(26).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [68] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(27).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [69] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(28).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [70] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(29).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [71] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(30).xls";Extended properties=Excel 12.0' )...Sheet0$


select * into [72] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(31).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [73] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(32).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [74] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(33).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [75] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1)(34).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [32] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(31).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [33] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(32).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [34] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(33).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [35] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0)(34).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [1] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [2] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [3] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(2).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [4] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(3).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [5] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(4).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [6] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(5).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [7] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(6).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [8] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(7).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [9] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(8).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [10] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(9).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [11] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(10).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [12] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(11).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [13] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(12).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [14] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(13).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [15] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(14).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [16] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(15).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [17] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(16).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [18] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(17).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [19] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(18).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [20] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(19).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [21] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(20).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [22] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(21).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [23] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(22).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [24] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(23).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [25] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(24).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [26] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(25).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [27] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(26).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [28] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(27).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [29] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(28).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [30] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(29).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [31] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(30).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [32] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(31).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [33] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(32).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [34] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(33).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [35] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(34).xls";Extended properties=Excel 12.0' )...Sheet0$


select * into [36] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(35).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [37] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(36).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [38] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(37).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [39] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(38).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [40] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(39).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [41] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(40).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [42] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(41).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [43] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(42).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [44] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(43).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [45] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(44).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [46] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(45).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [47] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(46).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [48] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(47).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [49] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(48).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [50] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(49).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [51] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(50).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [52] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(51).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [53] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(52).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [54] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(53).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [55] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(54).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [56] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(55).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [57] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(56).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [58] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(57).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [59] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(58).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [60] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(59).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [61] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(60).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [62] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(61).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [63] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(62).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [64] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(63).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [65] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(64).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [66] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(65).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [67] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(66).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [68] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(67).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [69] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(68).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [70] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(69).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [71] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(70).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [72] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(71).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [73] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(72).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [74] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(73).xls";Extended properties=Excel 12.0' )...Sheet0$
select * into [75] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(74).xls";Extended properties=Excel 12.0' )...Sheet0$

select * into [76] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(75).xls";Extended properties=Excel 12.0' )...Sheet0$




select * into [1] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [2] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [3] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(2).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [4] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(3).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [5] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(4).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [6] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(5).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [7] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(6).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [8] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(7).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [9] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(8).xlsx";Extended properties=Excel 12.0' )...Sheet0$

select * into [10] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(9).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [11] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(10).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [12] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(11).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [13] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(12).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [14] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(13).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [15] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(14).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [16] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(15).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [17] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(16).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [18] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(17).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [19] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(18).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [20] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(19).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [21] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(20).xlsx";Extended properties=Excel 12.0' )...Sheet0$

select * into [22] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(21).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [23] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(22).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [24] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(23).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [25] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(24).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [26] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(25).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [27] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(26).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [28] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(27).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [29] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(28).xlsx";Extended properties=Excel 12.0' )...Sheet0$

select * into [30] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(29).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [31] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(30).xlsx";Extended properties=Excel 12.0' )...Sheet0$

select * into [32] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(31).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [33] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(32).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [34] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(33).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [35] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(34).xlsx";Extended properties=Excel 12.0' )...Sheet0$


select * into [36] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(35).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [37] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(36).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [38] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(37).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [39] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(38).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [40] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(39).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [41] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(40).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [42] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(41).xlsx";Extended properties=Excel 12.0' )...Sheet0$
select * into [43] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(42).xlsx";Extended properties=Excel 12.0' )...Sheet0$



select * into [1] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(0).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [2] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(1).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [3] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(2).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [4] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(3).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [5] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(4).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [6] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(5).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [7] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(6).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [8] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(7).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [9] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(8).xlsx";Extended properties=Excel 12.0' )...Sheet1$

select * into [10] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(9).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [11] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(10).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [12] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(11).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [13] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(12).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [14] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(13).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [15] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(14).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [16] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(15).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [17] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(16).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [18] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(17).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [19] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(18).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [20] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(19).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [21] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(20).xlsx";Extended properties=Excel 12.0' )...Sheet1$

select * into [22] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(21).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [23] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(22).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [24] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(23).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [25] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(24).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [26] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(25).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [27] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(26).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [28] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(27).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [29] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(28).xlsx";Extended properties=Excel 12.0' )...Sheet1$

select * into [30] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(29).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [31] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(30).xlsx";Extended properties=Excel 12.0' )...Sheet1$

select * into [32] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(31).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [33] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(32).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [34] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(33).xlsx";Extended properties=Excel 12.0' )...Sheet1$
select * into [35] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(34).xlsx";Extended properties=Excel 12.0' )...Sheet1$


select * into [36] FROM OPENDATASOURCE ('Microsoft.ACE.OLEDB.12.0', 'Data Source="C:\Users\wkw\Desktop\1月份物流2\订单列表（新）(35).xlsx";Extended properties=Excel 12.0' )...Sheet1$


/*关闭相关支持选项*/



insert into[1]
select * from [2]
insert into[1]
select * from [3]
insert into[1]
select * from [4]
insert into[1]
select * from [5]
insert into[1]
select * from [6]
insert into[1]
select * from [7]
insert into[1]
select * from [8]
insert into[1]
select * from [9]
insert into[1]
select * from [10]
insert into[1]
select * from [11]
insert into[1]
select * from [12]
insert into[1]
select * from [13]
insert into[1]
select * from [14]
insert into[1]
select * from [15]
insert into[1]
select * from [16]
insert into[1]
select * from [17]
insert into[1]
select * from [18]
insert into[1]
select * from [19]
insert into[1]
select * from [20]
insert into[1]
select * from [21]
insert into[1]
select * from [22]
insert into[1]
select * from [23]
insert into[1]
select * from [24]
insert into[1]
select * from [25]
insert into[1]
select * from [26]
insert into[1]
select * from [27]
insert into[1]
select * from [28]
insert into[1]
select * from [29]
insert into[1]
select * from [30]
insert into[1]
select * from [31]

insert into[1]
select * from [32]
insert into[1]
select * from [33]
insert into[1]
select * from [34]
insert into[1]
select * from [35]

insert into[1]
select * from [36]
insert into[1]
select * from [37]
insert into[1]
select * from [38]
insert into[1]
select * from [39]
insert into[1]
select * from [40]




insert into[1]
select * from [41]
insert into[1]
select * from [42]
insert into[1]
select * from [43]
insert into[1]
select * from [44]
insert into[1]
select * from [45]
insert into[1]
select * from [46]
insert into[1]
select * from [47]
insert into[1]
select * from [48]
insert into[1]
select * from [49]
insert into[1]
select * from [50]
insert into[1]
select * from [51]
insert into[1]
select * from [52]
insert into[1]
select * from [53]
insert into[1]
select * from [54]
insert into[1]
select * from [55]
insert into[1]
select * from [56]
insert into[1]
select * from [57]
insert into[1]
select * from [58]
insert into[1]
select * from [59]
insert into[1]
select * from [60]
insert into[1]
select * from [61]
insert into[1]
select * from [62]
insert into[1]
select * from [63]
insert into[1]
select * from [64]
insert into[1]
select * from [65]
insert into[1]
select * from [66]
insert into[1]
select * from [67]
insert into[1]
select * from [68]
insert into[1]
select * from [69]
insert into[1]
select * from [70]
insert into[1]
select * from [71]

insert into[1]
select * from [72]
insert into[1]
select * from [73]
insert into[1]
select * from [74]
insert into[1]
select * from [75]



drop table [1]

drop table [2]
drop table [3]
drop table [4]
drop table [5]
drop table [6]
drop table [7]
drop table [8]
drop table [9]
drop table [10]
drop table [11]
drop table [12]
drop table [13]
drop table [14]
drop table [15]
drop table [16]
drop table [17]
drop table [18]
drop table [19]
drop table [20]
drop table [21]
drop table [22]
drop table [23]
drop table [24]
drop table [25]
drop table [26]
drop table [27]
drop table [28]
drop table [29]
drop table [30]
drop table [31]
drop table [32]
drop table [33]
drop table [34]
drop table [35]


drop table [36]
drop table [37]
drop table [38]
drop table [39]
drop table [40]

drop table [41]
drop table [42]
drop table [43]
drop table [44]
drop table [45]
drop table [46]
drop table [47]
drop table [48]
drop table [49]
drop table [50]

drop table [51]
drop table [52]
drop table [53]
drop table [54]
drop table [55]

drop table [56]
drop table [57]
drop table [58]
drop table [59]
drop table [60]
drop table [61]
drop table [62]
drop table [63]
drop table [64]
drop table [65]
drop table [66]
drop table [67]
drop table [68]
drop table [69]
drop table [70]
drop table [71]

drop table [72]
drop table [73]
drop table [74]
drop table [75]











