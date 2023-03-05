

from zeroKey import *
import sqlalchemy
import pandas as pd
import mysql.connector
import time

 
from sqlalchemy import create_engine, text
from Fetch_YF_Functons import *
from datetime import datetime


# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------

ticker       =  "ada-usd"  # lower case
start_Date   =  "2015-01-02"  #%Y/%m/%d 

#end_Date     =  "2023-02-10"
end_Date     =  datetime.now()
interval     =  "5m"  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
intervalA    =  ["1m", "2m", "5m", "15m", "30m", "60m", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 
intMaxLen = 14

# ------------------------------------------------ --------------------------------------------- ------------------------------------------- ---------------------------    
backTestInput = "no"  # " no"
onlineFire    = "yes"
           



mydb = mysql.connector.connect(
    
  host= mySqlConf("host"),
  user= mySqlConf("user"),
  password= mySqlConf("pass"),
  database=mySqlConf("database_name")

)



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
    
        
        #intervalA = ["90m"]
        
        end_Date     =  str((datetime.now() + timedelta(days=1)).date())
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>/////   Date Time Now : ", end_Date)
        
        

        data_online = {}

        for i in intervalA :
                
                
                _checkEmpty = True
                errorCounter = 1
             

                try :
                     
                     data = fetch_DataF_O(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=i)         
                     data_online[i] = data
                     table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= i)
                     frame = data.to_sql(con= database_connection() , name=table_name , if_exists='replace')
                     
                     print("Try for fetch and push  in interval : " ,i , " ---------- > OK!\n")
              

                     
                except :
                       print("\n>>>>>>>>>>>>>>>  may be internet connection is failed because download is failed !\n")
                       while _checkEmpty :
                                errorCounter +=1

                                print("\nErrorCounter :", errorCounter)

                                data = fetch_DataF_O(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=i)
                                if data.empty:
                                       
                                        time.sleep(3)
                                        print( "\nData is Empty.I'm Tring again... ")
                                else:
                                         _checkEmpty= False
                                         data_online[i] = data
                                         table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= i)
                                         frame = data.to_sql(con= database_connection() , name=table_name , if_exists='replace')
                                         print("Data.Empty: ", data.empty)
                
                time.sleep(1)
  
        
        print(" Test ::::::::::::::::::::")
        print(data_online["60m"])
        #print(data)

        #print(data_online.values())
        #print(data_online.keys())

        



