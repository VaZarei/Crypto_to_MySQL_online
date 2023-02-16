
from threading import local
import yfinance as yf
from datetime import date, timedelta
from datetime import datetime
import time
import fetchData


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


