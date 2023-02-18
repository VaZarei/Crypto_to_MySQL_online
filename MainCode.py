
import datetime
from datetime import date
from datetime import datetime, date, timedelta
from datetime import datetime


from fetchData import *
from sqlFunctons import *



ticker = "BTC-USD"
start_Date = "2010-01-01"  #%Y/%m/%d 
end_Date = "2023-02-10"
#end_Date = datetime.now()
interval = "3mo"   # 1m # 2m # 5m # 15m # 30m # 60m # 1h # 1d , 5d, 1wk, 1mo, 3mo

fetch_DataF(strTicker=ticker, strStart_Date=start_Date, strEnd_Date=end_Date, strInterval=interval)