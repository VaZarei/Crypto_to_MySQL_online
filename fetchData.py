# pip install yfinance





from ast import Break
from pydoc import doc
import yfinance as yf

from datetime import datetime, date, timedelta
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
    intervalDate = endDate - startDate  
    end_Now = end = (str(datetime.now())[0:10])
    end_wanted = date(int(end_Now[0:4]) , int(end_Now[5:7]),  int(end_Now[8:10]))
    interval_from_Now = end_wanted - startDate

    print("intervalDate: ", intervalDate.days)
    print("interval_from_Now: ", interval_from_Now.days)
   
   
    return int(intervalDate.days) , int(interval_from_Now.days)  # count enddate - start date  ,  start Day for find last days



# Functions -----------------------------------------------------------------------------------------------------------------



ticker = "ADA-USD"
start_Date = "2023-01-1"  #%Y/%m/%d
end_Date = "2023-02-10"
#end_Date = datetime.now()
interval = "2m"

print("First :", "start_Date: " , start_Date, "end_Date :", end_Date)
print("\n\n\n")



# 1m : last 30 days and interval be 7 days or below
# 2m : last 60 days
# 5m : last 60 days
# 15m: last 60 days
# 30m: last 60 days
# 60m: last 730 days
# 90m: last 60 days
# 1h : last 730 days
# 1d , 5d, 1wk, 1mo, 3mo]


intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))



if interval == "1m" :


    if intervalDate < 31 and interval_from_Now < 8 :
        print("Countable in 1m")
    
    delta = interval_from_Now - 29
    start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
    print("forced new start date: ", start_Date)
    intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
    
    
    if interval_from_Now > 31 :
        decide = input(" ---- interval_from_Now > 31 ---- interval between start_date and end_date is more than 30 days, please write start or end for begin count:  ")
        
        
        if decide == "start" :
            end_Date = str((datetime.strptime(end_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
            print("new end date1: ", end_Date)

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            

        if decide == "end" :

            
            start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
            print("new start date: ", start_Date)
            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            

    if intervalDate > 8 :
        
        decide = input(" ----- intervalDate > 8 ------ interval between start_date and end_date is more than 7 days, please write start or end for begin count:  ")
        delta = intervalDate - 7
        
        if decide == "start" :

            
            end_Date = str((datetime.strptime(end_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
            print("new end date1: ", end_Date)

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            
   
        if decide == "end" :

            start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
            print("new start date:111111 ", start_Date)

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            
        
    

if interval == "2m" :
    
    if intervalDate < 60 and interval_from_Now < 60 :
        print("Countable in 1m")
    
    delta = interval_from_Now - 59
    start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
    print("forced new start date: ", start_Date)
    intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
    
    
    if interval_from_Now > 60 :
        decide = input(" ---- interval_from_Now > 31 ---- interval between start_date and end_date is more than 30 days, please write start or end for begin count:  ")
        
        
        if decide == "start" :
            end_Date = str((datetime.strptime(end_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
            print("new end date1: ", end_Date)

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            

        if decide == "end" :

            
            start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
            print("new start date: ", start_Date)
            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            

    if intervalDate > 60 :
        
        decide = input(" ----- intervalDate > 8 ------ interval between start_date and end_date is more than 7 days, please write start or end for begin count:  ")
        delta = intervalDate - 7
        
        if decide == "start" :

            
            end_Date = str((datetime.strptime(end_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
            print("new end date1: ", end_Date)

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            
   
        if decide == "end" :

            start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
            print("new start date:111111 ", start_Date)

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
            
        

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



data = yf.download(ticker, start_Date, end_Date, interval=interval)

print(data)