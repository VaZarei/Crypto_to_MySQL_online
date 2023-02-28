
import time
import zeroKey

from sqlalchemy import create_engine
import sqlalchemy
import pymysql
import pandas as pd
 

from Fetch_YF_Functons import *



ticker = "bnb-usd"  # lower case

start_Date = "2023-01-01"  #%Y/%m/%d 
#end_Date = "2023-02-10"
end_Date = datetime.now()

interval = "5m"   # 1m # 2m # 5m # 15m # 30m # 60m # 1h # 1d , 5d, 1wk, 1mo, 3m
intervalArray = ["1m", "2m", "5m", "15m", "30m", "60m", "1h", "1d", "5d", "1wk", "1mo", "3mo", "okok"]

data = fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=interval)





database_username = zeroKey.mySqlConf.get("user")
database_password = zeroKey.mySqlConf.get("pass")
database_ip       = '127.0.0.1'
database_name     = 'traderbot'



database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))

con = database_connection
if con :
    print("\n\nThe Connection is okey ...  ! \n\n")


name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= interval)
frame = data.to_sql(con=database_connection, name=name , if_exists='replace')

print("frame :", frame)









query1 = """
             Create DATABASE IF NOT EXISTS bottrader  ;
             use bottrader;
             

             
             """

query2 = """
             drop database IF EXISTS bottrader ;
             

             """



