

import zeroKey
import sqlalchemy
import pandas as pd
import pymysql
 
from sqlalchemy import create_engine, text


from Fetch_YF_Functons import *
from mainView import *



ticker            = initialVar.ticker 
start_Date        = initialVar.start_Date 
end_Date          = initialVar.end_Date
interval          = initialVar.interval
intervalArray     = initialVar.interval

database_username = zeroKey.mySqlConf.get("user")
database_password = zeroKey.mySqlConf.get("pass")
database_ip       = '127.0.0.1'
database_name     = 'traderbot'

database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
                                                        database_ip, database_name))




data = fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=interval)



query = (("Create DATABASE IF NOT EXISTS traderbot"), ("use traderbot"))
         
for i in query :
 print(i)
 database_connection.connect().execute(text(i))


table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= interval)
frame = data.to_sql(con=database_connection, name=table_name , if_exists='replace')


database_connection.connect().execute(text("drop DATABASE IF EXISTS traderbott"))




            

