import importlib,sys
importlib.reload(sys)
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_CONNECT_STRING = 'mysql+pymysql://admin:Monster3~@172.16.147.177/JD_Stations?charset=utf8'

pinyin = "shanxi"
fileName = "JDstations_" + pinyin + "_gaode.xlsx"
tableName = "JDstations_" + pinyin + "_gaode"
inputpath = "G:\\work\\logistica\\stations\\JDStations\\stations\\gaode\\"

engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

# 读取csv文件
# csv_data = pd.read_csv(inputpath + csvName,encoding='utf-8')
# print(csv_data.shape)
# pd.io.sql.to_sql(frame=csv_data,name=tableName,con=engine,index=False,if_exists='append')

# 读取xlsx文件
xlsx_data = pd.read_excel(inputpath + fileName,encoding='utf-8')
print(xlsx_data.shape)
pd.io.sql.to_sql(frame=xlsx_data,name=tableName,con=engine,index=False,if_exists='append')