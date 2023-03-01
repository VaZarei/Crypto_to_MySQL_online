
import time
from Fetch_YF_Functons import *



ticker = "BTC-USD"
start_Date = "2010-01-01"  #%Y/%m/%d 
end_Date = "2023-02-10"
end_Date = datetime.now()
interval = "2m"   # 1m # 2m # 5m # 15m # 30m # 60m # 1h # 1d , 5d, 1wk, 1mo, 3m
intervalArray = ["1m", "2m", "5m", "15m", "30m", "60m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]


for i in (intervalArray) :
    
    print(i)

    print (fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=i))
    time.sleep(5)


   
#print(intervalArray[0])
