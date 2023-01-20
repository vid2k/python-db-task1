import pandas as pd
import os
from pathlib import Path

# creating connection to mongodb database
import os
from pymongo import MongoClient

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb://localhost:27017"
client = MongoClient(connection_string)


# loading csv files from each dir to pandas dataframe and saving to mongodb
csv_files_dir_path = "./csv_files"
list_of_dirs = os.listdir(csv_files_dir_path)
for directory in list_of_dirs:
    db = client[directory] # created db if doesnt exist
    collections_present = db.list_collection_names()
    for collec in collections_present:
        db.drop_collection(collec) # drops if exisits else ignores
    path_to_csv = Path(f"{csv_files_dir_path}/{directory}")
    file_list = [str(f) for f in path_to_csv.glob('**/*') if f.is_file()]
    i = 0
    dataframes_and_name = []
    data_mongo = []
    for file in file_list:
        # print(file)
        file_name_seprated = (str(file)).split("\\")
        varname = file_name_seprated[2][:-4]
        globals()[varname] = pd.read_csv(file)
        dataframes_and_name.append([globals()[varname], varname])
    for df, df_name in dataframes_and_name:
        data = df.to_dict(orient="records")
        # database_name.some_collection.drop()
        db[df_name].insert_many(data)
print("Successfully added data to database")

