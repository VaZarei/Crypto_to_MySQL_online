import yfinance as yf
import pandas as pd
from zeroKey import * 
from datetime import datetime
import sqlalchemy
from sqlalchemy import create_engine, text
import mysql.connector


ticker       =  "ada-usd"  # lower case
start_Date   =  "2023-03-02"  #%Y/%m/%d 

end_Date     =  datetime.now()
interval     =  "5m"  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
intervalA    =  ["1m", "2m", "5m", "15m", "30m", "1h", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 
intMaxLen = 14




def yfinann():
    datam = yf.download(ticker, start=start_Date, end=end_Date , interval="1m")
    print(datam)

yfinann()
def cal_online_Price ():

    intervalA    =  ["1m", "2m", "5m", "15m", "30m", "1h", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 

    for i in intervalA :

        if i == "1m" :

            table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= i)
            print(table_name)
            query1 = text("select * from {table_name} where Date > '2023-02-03 12:45:00' ; ".format(table_name=table_name))     
            query1 = text("select * from {table_name}  ; ".format(table_name=table_name))     

            sqlDf = pd.read_sql(query1, database_connection().connect())
            print(sqlDf)





#cal_online_Price()