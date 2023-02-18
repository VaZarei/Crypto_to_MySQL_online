# pip install yfinance

import yfinance as yf
from datetime import datetime, date, timedelta
from datetime import datetime

from sqlFunctons import *



def fetch_DataF(strTicker, strStart_Date, strEnd_Date, strInterval) :
    

    if str(type(strEnd_Date))  == "<class 'datetime.datetime'>" :
            strEnd_Date = (str(datetime.now())[0:10])
            print("---------- > End_Date = datetime.now \n\n")

    print("\n\n\nStart_Date : " , strStart_Date, "\nEnd_Date   : ", strEnd_Date, "\n\n")
    intervalDate, interval_from_Now = (count_date_Diff(str(strStart_Date), strEnd_Date))


    if (strInterval == "1m") :
        
        if intervalDate < 31 and interval_from_Now < 8 :

            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            
        
        else:
        
            delta = interval_from_Now - 29
            strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
            print("\n -------------- > Forced new start date: ", strStart_Date)
            print(" -------------- >            end   date: ", strEnd_Date , "\n")
            intervalDate, interval_from_Now = (count_date_Diff(str(strStart_Date), strEnd_Date))
        

            if intervalDate > 8 :
                
                decide = input("\n\"intervalDate > 8\"\nInterval between Start_Date and End_Date is more than 7 days, please choose constant:(start/end) : ")
                delta = intervalDate - 6
                
                if decide == "start" :

                    strEnd_Date = str((datetime.strptime(strEnd_Date, '%Y-%m-%d') - timedelta(days=delta)).date())
                    
                    print("\nStart_Date        : ", strStart_Date)
                    print("End_Date          : ", strEnd_Date)
                    print("interval          : ", strInterval ,"\n\n")

                    data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
                    

                if decide == "end" :

                    strStart_Date = str((datetime.strptime(str(strStart_Date), '%Y-%m-%d') + timedelta(days=delta)).date())

                    print("\nStart_Date        : ", strStart_Date)
                    print("End_Date          : ", strEnd_Date)
                    print("interval          : ", strInterval ,"\n\n")

                    data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
                    


    if (strInterval == "2m") or (strInterval == "5m") or  (strInterval == "15m") or (strInterval == "30m") :
        
        if interval_from_Now < 60 :
            
            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            print(data)

        else:
        
            delta = interval_from_Now - 59
            strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())

            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            print(data)
            
            

    if (strInterval == "60m") or (strInterval == "1h"):

        if interval_from_Now < 729 :
            
            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            

        else:
        
            delta = interval_from_Now - 729
            strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())

            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
            
            

    if (strInterval == "1d") or (strInterval == "5d")or (strInterval == "1wk")or (strInterval == "1mo")or (strInterval == "3mo"):
        
        
            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)

            

    return data            
        