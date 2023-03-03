import yfinance as yf

df = yf.download('AAPL', period='1d', interval='90m')
print(df)