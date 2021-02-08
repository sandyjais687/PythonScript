import re

from datetime import datetime

from date_extractor import extract_dates

def dateExt(text):
    #pattern = r'''"\d{2}"/"\d{2}"/"\d{4}"''' #and r"\d{2}:\d{2}:\d{1}"
    #m = re.match(pattern, text)
    #r'(\d{2}\S\[a-zA-Z]{3}\S\d{4})' #r'(\d{2}/\d{2}/\d{4})' and
    #pattern= r'(0?[1-9]|[12]\d|30|31)[^\w\d\r\n:](0?[1-9]|1[0-2])[^\w\d\r\n:](\d{4}|\d{2})'
    #pattern2= r'(0?[1-9]|[12]\d|30|31)[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'
    #pattern3= r'(\d{2})[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'
    
    pattern3= r'(\d{2}|\d)[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'
    match = re.findall(pattern3,text)
    print("length",len(match))
    tup1=match[0]   #1st tuple from match list
    tup2=match[1]   #2nd tuple from match list
    tup1='/'.join(tup1) #converting to string by "/"
    tup2='/'.join(tup2)
    
    tup=tup1+"\n"+tup2  #joining 2 strings together by \n
    print(tup)
    dates = extract_dates(tup)
    print(dates)
    a=dates[0]
    b=dates[1]
    #print(dates)
    if a>b:
        end_date=a
        start_date=b
        print("end date:",end_date)
        print("start date:",start_date)

    if b>a:
        end_date=b
        start_date=a
        print("end date:",end_date)
        print("start date:",start_date)

testData='''
MANOJ MEDICAL & GENERAL STORES
R-6/941/KAMDAR ROAD,LATUR,MOB-9370245680     ,,,,, LATUR
Stock and sales Statement from : 31/3/2021 to 1 January 21
Company : BERGEN ASTA Page : 1
'''
dateExt(testData)
