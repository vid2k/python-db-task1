from excel_to_csv import load_excel_save_to_csv
from relation_bw_sheets import save_commondata_csv
from connect_to_db import connect_to_database
from csv_to_df_to_mdb import save_to_db


print("""1. Reading excel workbooks inside "Workbooks" directory
 and saving csv files in "csv_files" directory for each workbook""")
load_excel_save_to_csv()

print("")

print("""2. Finding common data among the sheets in workbooks
 and saving it in each directory inside "csv_files" """)
save_commondata_csv()

print("")

print("""3. Create connection to mongodb local database""")
client = connect_to_database()

print("")

print("""4. Saving all workbook's csv files as named databases 
which contains csv files stored as documents""")
save_to_db(client)