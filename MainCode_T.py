

import zeroKey
import sqlalchemy
import pandas as pd
import pymysql
 
from sqlalchemy import create_engine, text


from Fetch_YF_Functons import *
from mainView import *


ticker = initialVar.ticker 
start_Date = initialVar.start_Date 
end_Date = initialVar.end_Date
interval = initialVar.interval
intervalArray = initialVar.interval

data = fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=interval)


database_username = zeroKey.mySqlConf.get("user")
database_password = zeroKey.mySqlConf.get("pass")
database_ip       = '127.0.0.1'
database_name     = 'traderbot'



database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
     
     
                                                        database_ip, database_name))
engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
                                                        database_ip, database_name))   

con = database_connection
name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= interval)
frame = data.to_sql(con=database_connection, name=name , if_exists='replace')











query =text( """
              Create DATABASE IF NOT EXISTS bottraderr ; 
              
              

            """)

query1 = text(" use bottraderr ; ")
            
  
con = engine.connect()       
con.execute(query) 

            

