import yfinance as yf
import datetime

from datetime import date
from datetime import datetime, date, timedelta
from datetime import datetime




def count_date_Diff (start_Date, end_Date) :

    """ 
        This Function count deferent interval between start to end date
        The output is integer and only Date 
    """
    
   
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





def fetch_DataF(strTicker, strStart_Date, strEnd_Date, strInterval) :

    """
        This Function make fetch data from yahoo finance according to ticker, start and end date and timeframe(strinterval)
        output : if everything is normal is a data table
        output : if timeframe(strinterval) be incorrecy is "-1"
    """
    
    checkin = False

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
                    


    elif (strInterval == "2m") or (strInterval == "5m") or  (strInterval == "15m") or (strInterval == "30m") :
        
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
            
            

    elif (strInterval == "60m") or (strInterval == "1h"):

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
            
            

    elif (strInterval == "1d") or (strInterval == "5d")or (strInterval == "1wk")or (strInterval == "1mo")or (strInterval == "3mo"):
        
        
            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)

            
    else:
        
        checkin = True
    

    return data if checkin == False else (print("\n\n\n....> Fetch Data failed because ticker or interval are incorrect !\n\n\n\n"))







def fetch_DataF_O(strTicker, strStart_Date, strEnd_Date, strInterval) :

    """
        This Function make fetch data base online ask ,  from yahoo finance according to ticker, start and end date and timeframe(strinterval)
        output : if everything is normal is a data table
        output : if timeframe(strinterval) be incorrecy is "-1"
    """
    
    checkin = False

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
            print( " Delta : ", delta)
            print("start date :" , strStart_Date)
            strStart_Date = str((datetime.strptime(strStart_Date, '%Y-%m-%d') + timedelta(days=delta)).date())
            print("\n -------------- > Forced new start date: ", strStart_Date)
            print(" -------------- >            end   date: ", strEnd_Date , "\n")
            intervalDate, interval_from_Now = (count_date_Diff(str(strStart_Date), strEnd_Date))
        

            if intervalDate > 8 :
                
                decide = "end"
                delta = intervalDate - 6
                

                if decide == "end" :

                    strStart_Date = str((datetime.strptime(str(strStart_Date), '%Y-%m-%d') + timedelta(days=delta)).date())

                    print("\nStart_Date        : ", strStart_Date)
                    print("End_Date          : ", strEnd_Date)
                    print("interval          : ", strInterval ,"\n\n")

                    data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)
                    


    elif (strInterval == "2m") or (strInterval == "5m") or  (strInterval == "15m") or (strInterval == "30m") :
        
        if interval_from_Now < 60 :
            
            print("\nStart_Date        : " , strStart_Date)
            print("End_Date          : "   , strEnd_Date)
            print("interval          : "   , strInterval ,"\n\n")

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
            
            

    elif (strInterval == "60m") or (strInterval == "1h"):

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
            
            

    elif (strInterval == "1d") or (strInterval == "5d")or (strInterval == "1wk")or (strInterval == "1mo")or (strInterval == "3mo"):
        
        
            print("\nStart_Date        : ", strStart_Date)
            print("End_Date          : ", strEnd_Date)
            print("interval          : ", strInterval ,"\n\n")

            data = yf.download(strTicker, strStart_Date, strEnd_Date, interval=strInterval)

            
    else:
        
        checkin = True
    

    return data if checkin == False else (print("\n\n\n....> Fetch Data failed because ticker or interval are incorrect !\n\n\n\n"))


def interval_Online ( intMaxLen , strInterval) :
    
    if strInterval == "1m" :

        strStart_Date = str((datetime.now() - timedelta(days=1)).date())
        strEnd_Date     =  datetime.now()

        pass

    
    if strInterval == "2m" :
        pass

    
    if strInterval == "5m" :
        pass

    
    if strInterval == "15m" :
        pass

    
    if strInterval == "1h" :
        pass

    
    if strInterval == "1d" :
        pass

    
    if strInterval == "1m" :
        pass

    
    if strInterval == "1m" :
        pass

    
    if strInterval == "1m" :
        pass
    
    return strStart_Date, strEnd_Date