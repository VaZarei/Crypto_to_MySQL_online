

from os import stat
from pickle import EMPTY_DICT
import yfinance as yf
from datetime import date, timedelta
from datetime import datetime
import time


start = "2023-01-01" 
end = "2023-01-02"
end = datetime.now()
interval = "1m"

def count_date_Diff () :
    global start, end


    if str(type(end))  == "<class 'datetime.datetime'>" :
        end = (str(datetime.now())[0:10])
        print("yess")

    startDate = date(int(start[0:4]) , int(start[5:7]),  int(start[8:10]))
    endDate = date(int(end[0:4]) , int(end[5:7]),  int(end[8:10]))
    
    countDiff = endDate - startDate     # Count interval days
    print(countDiff)  # count enddate - start date

    ## mohasebeye boodan dar n rooze akhir :

    end_Now = end = (str(datetime.now())[0:10])
    end_wanted = date(int(end_Now[0:4]) , int(end_Now[5:7]),  int(end_Now[8:10]))
    countDiff_last = end_wanted - startDate

    print(" Endlast : ", countDiff_last)    # count now_Date - start Day for find last days

    return int(countDiff.days) , int(countDiff_last.days)


a,b = count_date_Diff()
print (a,b)



#if interval == "1m" :
#    print(str(datetime.now())[0:10])
#    dateNow = (str(datetime.now())[0:10])
#    endDate_Now = date(int(dateNow[0:4]) , int(dateNow[5:7]),  int(dateNow[8:10]))
#    
#    diff_date_now = endDate_Now - startDate
#   print(" diff date now :", diff_date_now.days)
#    
#
#    if int(diff_date_now.days) < 30 and int(countDiff.days) < 8 :
#        print(" Output Printable")