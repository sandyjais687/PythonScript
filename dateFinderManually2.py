import re

from datetime import date, datetime

from date_extractor import extract_dates

def dateExt(text):
    mnth=["jan","fab","march"]
    pattern=r'\b(0?[1-9]|[12][0-9]|3[01])\b[^\w\d\r\n:](\w+)[^\w\d\r\n:](\d{4}|\d{2})'
    #pattern2=r"\b(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\b[^\w\d\r\n:](\d{4}|\d{2})"
    #for i in pattern:
    match = re.findall(pattern,text)
    print("length",len(match)) #we can put if condition 
    print(match)
    if len(match)==2:
        tup1=match[0]   #1st tuple from match list
        tup2=match[1]   #2nd tuple from match list
        tup1='/'.join(tup1) #converting to string by "/"
        tup2='/'.join(tup2)
        for frmt in ("%d/%m/%y","%d/%m/%Y","%d/%B/%Y","%d/%b/%Y","%d/%B/%y","%d/%b/%y"):
            try:
                date1 = datetime.strptime(tup1, frmt)
                date2 = datetime.strptime(tup2, frmt)
                print("matching with 2nd pattern but 2dates")
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
    if len(match)==1:
        tup1=match[0]
        tup1='/'.join(tup1)
        for frmt in ("%d/%m/%y","%d/%m/%Y","%d/%B/%Y","%d/%b/%Y","%d/%B/%y","%d/%b/%y","%m/%y","%b/%y","%B/%y","%m/%y","%b/%Y","%B/%Y"):
            try:
                date1 = datetime.strptime(tup1, frmt)
                print("matching with 2nd pattern but only 1 date")
                print(date1)
            except ValueError:
               pass

    if len(match)<=0:
        text=text.lower()
        #pattern2=r"(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)[^\w\d\r\n:](\d{4}|\d{2})"
        pattern2=r"(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)[^\w\d\r\n:](\d{4}|\d{2})"
        match = re.findall(pattern2,text)
        tup1=match[0]
        tup1='/'.join(tup1)
        
        for frmt in ("%m/%y","%b/%y","%B/%y","%m/%y","%b/%Y","%B/%Y"):
            try:
                date1 = datetime.strptime(tup1, frmt)
                print("matching with 2nd pattern")
                print(date1)
            except ValueError:
               pass  
            
        '''
        dates = extract_dates(tup1)
        print("matching with 2nd pattern")
        print(dates)'''

testData='''N. CHIMANLAL & CO. PVT. LTD.								
PAN No : AACCN2221P GSTIN No : 27AACCN2221P1ZD VAT TIN No : 27700506776V								
Pending Credit/Debit Note List of 								
M/s. M/S INDOCO REMEDIES LTD. (1009) (Upto Date : 05/02/2021)
'''
dateExt(testData)
