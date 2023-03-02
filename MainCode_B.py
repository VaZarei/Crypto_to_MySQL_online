from zeroKey import *
import sqlalchemy
import pandas as pd
import mysql.connector
 
from sqlalchemy import create_engine, text
from Fetch_YF_Functons import *
from datetime import datetime



ticker     =  "ada-usd"  # lower case
start_Date =  "2023-01-01"  #%Y/%m/%d 
#end_Date  =  "2023-02-10"
end_Date   =  datetime.now()
interval   =  "1d"  # ["1m", "2m", "5m", "15m", "30m", "60m", "1h", "1d", "5d", "1wk", "1mo", "3mo"] 
    
            


   


database_username = mySqlConf("user")
database_password = mySqlConf("pass")
database_ip       = '127.0.0.1'
database_name     = 'traderbot'


mydb = mysql.connector.connect(
  host="localhost",
  user= mySqlConf("user"),
  password= mySqlConf("pass"),
  database="traderbot"
)


database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
                                                        database_ip, database_name))




data = fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=interval)

table_name="{ticker}_{interval}".format(ticker= ticker.replace("-","") ,interval= interval)
frame = data.to_sql(con=database_connection, name=table_name , if_exists='replace')

mycursor = mydb.cursor()
query = """
        create database if not exists traderbot ;
        use traderbot ;
        """
mycursor.execute(query, multi=True)
mydb.commit()

# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# update table 

mycursor = mydb.cursor()
query = "update adausd_1d set Date = '11-01-11' where Date='2023-02-28' ; "
mycursor.execute(query)
mydb.commit()

# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# Create or insert  to table 

mycursor = mydb.cursor()
query = "INSERT INTO adausd_1d (Date, Volume) VALUES (%s , %s)"   # Edit on 1d timeframe
val = ["2024-01-01" , "254789"]
mycursor.execute(query, val)
mydb.commit()

# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# Delete from table

mycursor = mydb.cursor()            
query = " delete from adausd_1d where Date='2023-02-26';"
mycursor.execute(query)
mydb.commit()
# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# Read or select from table

query1 = text("select * from {table_name} where Date > '2023-02-01 12:45:00' ; ".format(table_name=table_name))     
query1 = text("select * from {table_name}  ; ".format(table_name=table_name))     

df = pd.read_sql(query1, database_connection.connect())
print(df)
# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
