# pip install yfinance

import yfinance as yf
from datetime import datetime, date, timedelta
from datetime import datetime


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

    print("intervalDate      : ", intervalDate.days)
    print("interval_from_Now : ", interval_from_Now.days)
   
   
    return int(intervalDate.days) , int(interval_from_Now.days)  # count enddate - start date  ,  start Day for find last days

# Functions -----------------------------------------------------------------------------------------------------------------


ticker = "BTC-USD"
start_Date = "2010-01-01"  #%Y/%m/%d 
end_Date = "2023-02-10"
#end_Date = datetime.now()
intervall = "5d"   # 1m # 2m # 5m # 15m # 30m # 60m # 1h # 1d , 5d, 1wk, 1mo, 3mo

if str(type(end_Date))  == "<class 'datetime.datetime'>" :
        end_Date = (str(datetime.now())[0:10])
        print("---------- > End_Date = datetime.now \n\n")

print("\n\n\nStart_Date : " , start_Date, "\nEnd_Date   : ", end_Date, "\n\n")
intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))


if (intervall == "1m") :
    
    if intervalDate < 31 and interval_from_Now < 8 :
        print("Countable in 1m")
    
    else:
    
        delta = interval_from_Now - 29
        start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
        print("\n -------------- > Forced new start date: ", start_Date)
        print(" -------------- >            end   date: ", end_Date , "\n")
        intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
    

        if intervalDate > 8 :
            
            decide = input("\n\"intervalDate > 8\"\nInterval between Start_Date and End_Date is more than 7 days, please choose constant:(start/end) : ")
            delta = intervalDate - 6
            
            if decide == "start" :

                end_Date = str((datetime.strptime(end_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
                print("\n -------------- >     start date: ", start_Date)
                print(" -------------- > new end   date: ", end_Date , "\n")

            if decide == "end" :

                start_Date = str((datetime.strptime(str(start_Date), '%Y-%m-%d') + timedelta(days=delta)).date())
                print("\n------------------>  new Start Date: ", start_Date, "\n")

            intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
                    


if (intervall == "2m") or (intervall == "5m") or  (intervall == "15m") or (intervall == "30m") :
    
    if interval_from_Now < 60 :
        print("Countable in 2m or 5m or 15m or 30m : \n")

    else:
    
        delta = interval_from_Now - 59
        start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
        print("\n -------------- > Forced new start date: ", start_Date , "\n")
        intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
        
        

if (intervall == "60m") or (intervall == "1h"):

    if interval_from_Now < 729 :
        print("Countable in 60m")

    else:
    
        delta = interval_from_Now - 729
        start_Date = str((datetime.strptime(start_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
        print("\n -------------- > Forced new start date: ", start_Date , "\n")
        intervalDate, interval_from_Now = (count_date_Diff(str(start_Date), end_Date))
        


print("Start_Date        : ", start_Date)
print("End_Date          : ", end_Date)
print("interval          : ", intervall ,"\n\n")

data = yf.download(ticker, start_Date, end_Date, interval=intervall)

print(data)