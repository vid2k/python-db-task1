import pandas as pd
import os
from pathlib import Path
# loading csv files from each dir to pandas dataframe
csv_files_dir_path = "./csv_files"
list_of_dirs = os.listdir(csv_files_dir_path)
for directory in list_of_dirs:
    path_to_csv = Path(f"{csv_files_dir_path}/{directory}")
    file_list = [str(f) for f in path_to_csv.glob('**/*') if f.is_file()]
    i = 0
    for file in file_list:
        # print(file)
        file_name_seprated = (str(file)).split("\\")
        varname = file_name_seprated[2][:-4]
        # print(varname)
        # i += 1
        # varname = f"df_{i}"
        globals()[varname] = pd.read_csv(file)
        print(varname)
        print(globals()[varname])
