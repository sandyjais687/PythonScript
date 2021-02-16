#pip install "xlwt==1.3.0"
#pip install camelot-py
#pip install camelot-py[cv]
    # we check for tables with both methods
#pip install xlsxwriter
#pip install xlrd
import camelot
import pandas as pd

new_filename=r"d8.pdf"
lattice_tables = camelot.read_pdf(new_filename, flavor='lattice', pages='1-end',flag_size=True)
stream_tables = camelot.read_pdf(new_filename, flavor='stream', pages='1-end',flag_size=True)

    # the final tables
tables = []

    # we check whether the number of tables are the same
if len(lattice_tables) > 0 and len(stream_tables) > 0 and len(lattice_tables) == len(stream_tables):       
        # then we try to pick the best table
    for index in range(len(lattice_tables)):
            # we check whether the tables are both good enough
        if (lattice_tables[index].parsing_report) and (stream_tables[index].parsing_report):
            print("lattice",lattice_tables[index].parsing_report)
            print("stream",stream_tables[index].parsing_report)
                # they probably represent the same table
            if lattice_tables[index].parsing_report['page'] == stream_tables[index].parsing_report['page'] and lattice_tables[index].parsing_report['order'] == stream_tables[index].parsing_report['order']:
                total_lattice = 1
                total_stream = 1
                print("equal report")
                for num in lattice_tables[index].shape:
                    print("shape of lattice",lattice_tables[index].shape)
                    total_lattice *= num
                    print(num,total_lattice)
                for num in stream_tables[index].shape:
                    print("shape of strm",stream_tables[index].shape)
                    total_stream *= num
                    print(num,total_stream)

                    # we pick the table with the most cells
                if(total_lattice >= total_stream):
                    tables.append(lattice_tables[index])
                    print("printing latt")
                else:
                    tables.append(stream_tables[index])
                    print("printing strm")

            # if we have a different number of tables we just pick the object with the most number of tables
        elif (lattice_tables[index].parsing_report):
            tables.append(lattice_tables[index])
            print("printing latt")

        elif (stream_tables[index].parsing_report):
            tables.append(stream_tables[index])
            print("printing strm")
elif len(lattice_tables) >= len(stream_tables):
    tables = lattice_tables
    print("printing latt")
else:
    tables = stream_tables   
    print("printing strm") 

if tables is not None and len(tables) > 0:
        # let's check whether is TableList object or just a list of tables
    if isinstance(tables, camelot.core.TableList) is False:
        tables = camelot.core.TableList(tables)
    tables.export('output.xlsx', f='excel')
df = pd.concat(pd.read_excel('output.xlsx', sheet_name=None), ignore_index=True)
print("shape",df.shape)
df.to_excel('outputFinal.xlsx', engine='xlsxwriter')
