from functools import reduce

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
    dataframes = []
    set_of_dataframes = []
    for file in file_list:
        # print(file)
        file_name_seprated = (str(file)).split("\\")
        varname = file_name_seprated[2][:-4]
        globals()[varname] = pd.read_csv(file)
        print(varname)
        # print(globals()[varname])
        dataframes.append(globals()[varname])
        column_for_merge = globals()[varname].columns[-1]
        set_of_dataframes.append(set(globals()[varname][column_for_merge]))
        # print(column_for_merge)
    # print(set_of_dataframes)
    set_of_dataframes = set(set_of_dataframes)
    common = set.intersection(set_of_dataframes)
    # set_of_dataframes = set(set_of_dataframes)
    # print(set_of_dataframes)
    # df_merged = reduce(lambda left, right: pd.merge(left, right, on=column_for_merge, how="inner"), dataframes)
    # common = set.intersection(set_of_dataframes)
    # print(common)
