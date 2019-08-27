from impala.dbapi import connect
import pandas as pd

# 查询所有字段
def list_col(localhost,database, port,tabls_name):
    db = connect(localhost,port,database)
    cursor = db.cursor()
    cursor.execute("select * from %s" % tabls_name)
    col_name_list = [tuple[0] for tuple in cursor.description]
    db.close()
    return col_name_list

# 列出所有的表
def list_table(localhost,database,port):
    db = connect(localhost,database,port)
    cursor = db.cursor()
    cursor.execute("show tables")
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    db.close()
    return table_list

# 数据库信息
port = 21050 # 端口号
host = "172.22.210.29" # 连接地址
database = "bigtables" # 数据库名
tabls_name = "shop_order" # 表名

table_names = list_table(host,port,database) 
# print('库中所有表名:',*table_names,sep = '\n  ')
column_names = list_col(host,database, port,tabls_name)
# print('表中所有字段名:',*column_names,sep = '\n  ')

conn = connect(host=host,port =port , database = database,timeout=3600 )
cur_data = conn.cursor()
cur_data.execute('''SELECT * from shop_order;''')
data=cur_data.fetchall()
data = pd.DataFrame(data,columns=column_names)
print(data.shape)
data.to_csv("D:/GitHub/datasets/shop_order_190822.csv",index=False)
