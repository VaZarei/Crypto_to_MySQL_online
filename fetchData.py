# pip install yfinance





import yfinance as yf
from datetime import date, timedelta
from datetime import datetime
import time
import sqlFunctons


# Functions -----------------------------------------------------------------------------------------------------------------


def count_date_Diff (start_Date, end_Date) :

   
    if str(type(end_Date))  == "<class 'datetime.datetime'>" :
        end_Date = (str(datetime.now())[0:10])
        print("yess")

    startDate = date(int(start_Date[0:4]) , int(start_Date[5:7]),  int(start_Date[8:10]))
    endDate = date(int(end_Date[0:4]) , int(end_Date[5:7]),  int(end_Date[8:10]))
    
    countDiff = endDate - startDate     # Count interval days
    print(countDiff)  # count enddate - start date

    ## mohasebeye boodan dar n rooze akhir :

    end_Now = end = (str(datetime.now())[0:10])
    end_wanted = date(int(end_Now[0:4]) , int(end_Now[5:7]),  int(end_Now[8:10]))
    countDiff_last = end_wanted - startDate

    print(" Endlast : ", countDiff_last)    # count now_Date - start Day for find last days

    return int(countDiff.days) , int(countDiff_last.days)


# Functions -----------------------------------------------------------------------------------------------------------------



ticker = "ADA-USD"
start_Date = "2023-02-12"
end_Date = "2023-02-14"
#end_Date = datetime.now()
interval = "1m"



# 1m : last 30 days
# 2m : last 60 days
# 5m : last 60 days
# 15m: last 60 days
# 30m: last 60 days
# 60m: last 730 days
# 90m: last 60 days
# 1h : last 730 days
# 1d , 5d, 1wk, 1mo, 3mo]

startDate = date(int(start_Date[0:4]) , int(start_Date[5:7]),  int(start_Date[8:10]))
endDate = date(int(end_Date[0:4]) , int(end_Date[5:7]),  int(end_Date[8:10]))
 
countDiff = endDate - startDate
print(countDiff)







if interval == "1m" :
    print(str(datetime.now())[0:10])
    dateNow = (str(datetime.now())[0:10])
    endDate_Now = date(int(dateNow[0:4]) , int(dateNow[5:7]),  int(dateNow[8:10]))
    
    diff_date_now = endDate_Now - startDate
    print(" diff date now :", diff_date_now.days)
    

    if int(diff_date_now.days) < 30 and int(countDiff.days) < 8 :
        print(" Output Printable")

    

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


a,b= count_date_Diff(start_Date, end_Date)
print ("a: ", a , "b :", b)

#data = yf.download(ticker, start_Date, end_Date, interval= interval)



#print(data.head(10)) ,

