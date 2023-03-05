import yfinance as yf
import pandas as pd

from zeroKey import * 
from datetime import datetime
import sqlalchemy
from sqlalchemy import create_engine, text
import mysql.connector
import time
from Fetch_YF_Functons import *


ticker       =  "ada-usd"  # lower case
start_Date   =  "2023-03-02"  #%Y/%m/%d 

end_Date     =  datetime.now()
interval     =  "5m"  # ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
intervalA    =  ["1m", "2m", "5m", "15m", "30m", "1h", "90m",  "1d", "5d", "1wk", "1mo", "3mo"] 
intMaxLen = 14




def yfinann():
    datam = yf.download(ticker, start=start_Date, end=end_Date , interval="1m")
    print(datam)
    
    if (datam.empty) :
        print("True")
    else:
        print("False") 
   

#yfinann()


        
def updateData() :
        
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
                        
                       print("\n>>>>>>>>>>>>>>>  May be internet connection is failed because download is failed !\n")
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

        return data_online

updateData()
       