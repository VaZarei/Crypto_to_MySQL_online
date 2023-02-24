
import time
import zeroKey
import mysql.connector

from Fetch_YF_Functons import *



ticker = "BTC-USD"

start_Date = "2010-01-01"  #%Y/%m/%d 
end_Date = "2023-02-10"
#end_Date = datetime.now()

interval = "2m"   # 1m # 2m # 5m # 15m # 30m # 60m # 1h # 1d , 5d, 1wk, 1mo, 3m
intervalArray = ["1m", "2m", "5m", "15m", "30m", "60m", "1h", "1d", "5d", "1wk", "1mo", "3mo", "okok"]

#data = fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=interval)
#print(data)





mydb = mysql.connector.connect(
  host=zeroKey.mySqlConf.get("host") ,
  user=zeroKey.mySqlConf.get("user"),
  password=zeroKey.mySqlConf.get("pass")
)

print(mydb)


mycursor = mydb.cursor()

query1 = """
             Create DATABASE bottrader ;

             
             """

query2 = """
             drop database bottrader ;
             

             """

for result in mycursor.execute(query2 , multi=True) :
    print(result)


print("OK")
