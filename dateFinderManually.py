import re

from datetime import date, datetime

from date_extractor import extract_dates

def dateExt(text):
    #pattern = r'''"\d{2}"/"\d{2}"/"\d{4}"''' #and r"\d{2}:\d{2}:\d{1}"
    #m = re.match(pattern, text)
    #r'(\d{2}\S\[a-zA-Z]{3}\S\d{4})' #r'(\d{2}/\d{2}/\d{4})' and
    #pattern= r'(0?[1-9]|[12]\d|30|31)[^\w\d\r\n:](0?[1-9]|1[0-2])[^\w\d\r\n:](\d{4}|\d{2})'
    #pattern2= r'(0?[1-9]|[12]\d|30|31)[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'
    #pattern3= r'(\d{2})[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'
    
    #pattern3= r'(\d{2}|\d)[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'#working pattern

    pattern3= r'\b(0?[1-9]|[12][0-9]|3[01])\b[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'
    
    match = re.findall(pattern3,text)
    print("length",len(match)) #we can use len(match) to identify how many dates we got
    
    #if len(match)==2:
    tup1=match[0]   #1st tuple from match list
    tup2=match[1]   #2nd tuple from match list
    tup1='/'.join(tup1) #converting to string by "/"
    tup2='/'.join(tup2)
    for frmt in ("%d/%m/%y","%d/%m/%Y","%d/%B/%Y","%d/%b/%Y","%d/%B/%y","%d/%b/%y"):
        try:
            date1 = datetime.strptime(tup1, frmt)
            date2 = datetime.strptime(tup2, frmt)
            if date1>date2:
                start_date=date2
                end_date=date1
                print("start date:",start_date)
                print("end date:",end_date)
                

            if date2>date1:
                start_date=date1
                end_date=date2
                print("start date:",start_date)
                print("end date:",end_date)
        except ValueError:
            pass

        


testData='''
MANOJ MEDICAL & GENERAL STORES
R-6/941/KAMDAR ROAD,LATUR,MOB-9370245680     ,,,,, LATUR
Stock and sales Statement from : 01/jan/2021 to 29/jan/2021
Company : BERGEN ASTA Page : 1
'''
dateExt(testData)
