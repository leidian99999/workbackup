import importlib,sys
importlib.reload(sys)
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_CONNECT_STRING = 'mysql+pymysql://admin:Monster3~@172.16.147.177/Log_info?charset=utf8'

date = "1812"
carrier = "JDWL"
charactor = "LS"
LogAPI = "cha"
fileName ="20" + date + "_" + carrier + "_" + charactor + "_" + LogAPI + ".csv"
tableName = date + "_" + carrier + "_" + charactor + "_" + LogAPI
inputpath = "G:\\work\\logistica\\info\\output\\CHA\\CSV\\"

engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

# 读取csv文件
csv_data = pd.read_csv(inputpath + fileName,encoding='utf-8')
print(csv_data.shape)
pd.io.sql.to_sql(frame=csv_data,name=tableName,con=engine,index=False,if_exists='append')

# 读取xlsx文件
# xlsx_data = pd.read_excel(inputpath + fileName,encoding='utf-8')
# print(xlsx_data.shape)
# pd.io.sql.to_sql(frame=xlsx_data,name=tableName,con=engine,index=False,if_exists='append')