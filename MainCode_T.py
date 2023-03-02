

from zeroKey import *
import sqlalchemy
import pandas as pd
import mysql.connector

 
from sqlalchemy import create_engine, text
from Fetch_YF_Functons import *
from datetime import datetime


# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------

ticker     =  "ada-usd"  # lower case
start_Date =  "2023-01-01"  #%Y/%m/%d 
#end_Date  =  "2023-02-10"
end_Date   =  datetime.now()
interval   =  "1d"  # ["1m", "2m", "5m", "15m", "30m", "60m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 


# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------    
            



mydb = mysql.connector.connect(
    
  host= mySqlConf("host"),
  user= mySqlConf("user"),
  password= mySqlConf("pass"),
  database=mySqlConf("database_name")

)


backTestInput = "yes"  # " no"
onlineFire    = "no"

if backTestInput == "yes" :
       

        data = fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=interval)

        table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= interval)
        frame = data.to_sql(con= database_connection() , name=table_name , if_exists='replace')














        # ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
        # Read or select from table

        query1 = text("select * from {table_name} where Date > '2023-02-01 12:45:00' ; ".format(table_name=table_name))     
        query1 = text("select * from {table_name}  ; ".format(table_name=table_name))     

        df = pd.read_sql(query1, database_connection().connect())
        print(df)
        # ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------



if onlineFire == "yes" :             # --------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
   ticker = yf.Ticker(ticker).info

   print (ticker)


    



