
from camelot.parsers import lattice
import tabula
import pandas as pd
import os

#pip install pandas
#pip install camelot-py[cv]
##pip install tabula-py

file="f5.pdf"

df_latt = tabula.read_pdf(file, pages='all', multiple_tables=True)
print(len(df_latt))

if len(df_latt)==1:
    tabula.convert_into(file, "output-tabula.csv", output_format="csv", pages='all')
    print("printing Using CSV method")
    
else: 
    writer=pd.ExcelWriter("multipleDF.xlsx", engine="openpyxl")
    for i in range(len(df_latt)):
        df_latt[i]=df_latt[i].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" "," "], regex=True)
        df_latt[i].to_excel(writer, sheet_name=('Sheet'+str(i)),index=False)
        #print(df_latt[i])
    writer.save()
    writer.close()
    df = pd.concat(pd.read_excel('multipleDF.xlsx', sheet_name=None), ignore_index=True)
    print("shape",df.shape)
    print(df)
    df.to_excel('outputFinal.xlsx', engine='xlsxwriter',index=False)
    print("printing Using XLSX method")
    os.remove("multipleDF.xlsx")
    '''
    writer=pd.ExcelWriter("multipleDF2.xlsx", engine="openpyxl")
    for i in range(len(df_strm)):
        df_strm[i]=df_strm[i].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" "," "], regex=True)
        df_strm[i].to_excel(writer, sheet_name=('Sheet'+str(i)),index=False)

    writer.save()
    df1 = pd.concat(pd.read_excel('multipleDF2.xlsx', sheet_name=None), ignore_index=True)
    print("shape",df1.shape)
    print(df1)

    df1.to_excel('outputFinal2.xlsx', engine='xlsxwriter',index=False)
    '''
