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



ticker = "BTC-USD"
start_Date = "2010-01-1"  #%Y/%m/%d 
end_Date = "2023-02-10"
#end_Date = datetime.now()
intervall = "60m"   # 1m # 2m # 5m # 15m # 30m # 60m # 1h # 1d , 5d, 1wk, 1mo, 3mo

if str(type(end_Date))  == "<class 'datetime.datetime'>" :
        end_Date = (str(datetime.now())[0:10])
        print("end_Date = datetime.now")

print("First :", "start_Date: " , start_Date, "end_Date :", end_Date)
print("\n\n\n")



intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))



if (intervall == "1m") :
    print(" im in 1mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")




    if intervalDate < 31 and interval_from_Now < 8 :
        print("Countable in 1m")
    
    else:
    
        delta = interval_from_Now - 29
        start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
        print("forced new start date: ", start_Date)
        intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
    

        if intervalDate > 8 :
            
            decide = input("intervalDate > 8 ------ interval between start_date and end_date is more than 7 days, please write start or end for begin count:  ")
            delta = intervalDate - 6
            
            if decide == "start" :

                
                end_Date = str((datetime.strptime(end_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
                print("\n-----------------new End Date: ", end_Date)

                #intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
                

            if decide == "end" :

                start_Date = str((datetime.strptime(str(start_Date), '%Y-%m-%d') + timedelta(days=delta)).date())
                print("\n------------new Start Date: ", start_Date)

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
                    
                
            

if (intervall == "2m") or (intervall == "5m") or  (intervall == "15m") or (intervall == "30m") :
    print(" im in 2 ta 30 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")


    
    if interval_from_Now < 60 :
        print("Countable in 2m or 5m or 15m or 30m : \n")

    else:

    
        delta = interval_from_Now - 59
        start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
        print("forced new start date: ", start_Date)
        intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
        
        
        

        
            


if (intervall == "60m") or (intervall == "1h"):
    print(" im in 60 ya 1h mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")


    if interval_from_Now < 729 :
        print("Countable in 60m")

    else:
    
        delta = interval_from_Now - 729
        start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
        print("forced new start date: ", start_Date)
        intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
        
        
                        

        



data = yf.download(ticker, start_Date, end_Date, interval=intervall)

print(data)