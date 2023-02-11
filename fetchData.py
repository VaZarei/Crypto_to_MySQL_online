# pip install yfinance





import yfinance as yf
from datetime import date, timedelta
from datetime import datetime
import time


ticker = "ADA-USD"
start = "2018-05-10"
end = "2022-05-14"
#end = datetime.now()
interval = "5d"



# 1m : last 30 days
# 2m : last 60 days
# 5m : last 60 days
# 15m: last 60 days
# 30m: last 60 days
# 60m: last 730 days
# 90m: last 60 days
# 1h : last 730 days
# 1d , 5d, 1wk, 1mo, 3mo]

startDate = date(int(start[0:4]) , int(start[5:7]),  int(start[8:10]))
endDate = date(int(end[0:4]) , int(end[5:7]),  int(end[8:10]))

t = endDate - startDate
print(t.days)





if interval == "1m" :
    pass

if interval == "2m" :
    pass

if interval == "5m" :
    pass

if interval == "15m" :
    pass

if interval == "30m" :
    pass

if interval == "60m" :
    pass

if interval == "90m" :
    pass

if interval == "1h" :
    pass


data = yf.download(ticker, start, end, interval= interval)



print(data.head(10)) ,

