# pip install yfinance





import yfinance as yf
from datetime import datetime

data = yf.download("ADA-USD", start="2021-11-10", end=datetime.now(), interval="1d")
print(data.tail(10))