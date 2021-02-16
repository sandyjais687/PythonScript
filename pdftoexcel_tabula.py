
from camelot.parsers import lattice
import tabula
import pandas as pd

file="d9.pdf"
# Read pdf into list of DataFrame
df_strm = tabula.read_pdf(file, pages='all', stream=True, multiple_tables=True)
df_latt = tabula.read_pdf(file, pages='all', lattice=True, multiple_tables=True)


writer=pd.ExcelWriter("multipleDF.xlsx", engine="xlsxwriter")
for i in range(len(df_latt)):
    df_latt[i]=df_latt[i].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" "," "], regex=True)
    df_latt[i].to_excel(writer, sheet_name=('Sheet'+str(i)),index=False)
    #print(df_latt[i])
writer.save()
df = pd.concat(pd.read_excel('multipleDF.xlsx', sheet_name=None), ignore_index=True)
print("shape",df.shape)
#df=df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r","_x000D_"], value=[" "," "," "], regex=True)
print(df)

df.to_excel('outputFinal.xlsx', engine='xlsxwriter',index=False)


writer=pd.ExcelWriter("multipleDF.xlsx", engine="xlsxwriter")
for i in range(len(df_strm)):
    df_strm[i]=df_strm[i].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" "," "], regex=True)
    df_strm[i].to_excel(writer, sheet_name=('Sheet'+str(i)),index=False)
    #print(df_latt[i])
writer.save()
df1 = pd.concat(pd.read_excel('multipleDF.xlsx', sheet_name=None), ignore_index=True)
print("shape",df1.shape)
#df=df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r","_x000D_"], value=[" "," "," "], regex=True)
print(df1)

df1.to_excel('outputFinal2.xlsx', engine='xlsxwriter',index=False)

'''
for i in range(len(df_latt)):   
    print("latt=============================================\n",df_latt[i])
    df_latt[i].to_excel(writer, sheet_name=None) '''
'''
r1, c1 = df_strm.shape
r2, c2 = df_latt.shape
print(r1,c1)
print(r2,c2)'''
#tabula.convert_into(file, "output-tabula.csv", output_format="csv", pages='all')
