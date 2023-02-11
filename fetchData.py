# pip install yfinance





import yfinance as yf
from datetime import datetime


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

