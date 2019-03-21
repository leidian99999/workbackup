# coding=utf-8

import pymysql
import csv

# 数据库连接
connection=pymysql.connect(
    host='172.16.147.177',
    user='admin',
    passwd='Monster3~',
    # db='JD_Stations',
    port=3306,
    charset='utf8'
)

#使用cursor()方法创建一个游标对象cursor
db_cursor=connection.cursor()

'''
#使用execute()方法执行sql查询
db_cursor.execute("select version()") 
#使用fetchone()方法获取单条数据
data=db_cursor.fetchone() 
print("数据库版本:%s" %data)
#关闭数据库连接
connection.close() 

'''


# 建表与插入
'''
# 使用预处理语句创建表
sqlOder="""CREATE TABLE contact(NAME VARCHAR(20),email VARCHAR(20),address VARCHAR(20),age INT)"""
db_cursor.execute(sqlOder)
# 关闭数据库连接
connection.close()
'''

#选择要操作的数据库
connection.select_db("JD_Stations")

db_cursor.execute("delete from contact")
sql="""insert into contact(name,email,address,mobile) values('%s','%s','%s','%s')"""
try:
  with open("test02.csv","r") as f:    #将csv文件里的数据插入到表contact
    result=csv.DictReader(f)
    for i in result:   #逐条执行插入
        db_cursor.execute(sql %(i['name'],i['email'],i["address"],i['mobile']))
    connection.commit()
except Exception as e:
    print("error to insert data:",e)
    connection.rollback()   #若发生错误则回滚
print("insert rowcount:",db_cursor.rowcount)  #返回影响行数
connection.close()