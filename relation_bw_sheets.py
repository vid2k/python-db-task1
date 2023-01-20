from functools import reduce
import pandas as pd
import os
from pathlib import Path

def save_commondata_csv():
    from functools import reduce
    import pandas as pd
    import os
    from pathlib import Path
    # loading csv files from each dir to pandas dataframe, find common data and save it to files
    csv_files_dir_path = "./csv_files"
    list_of_dirs = os.listdir(csv_files_dir_path)
    for directory in list_of_dirs:
        path_to_csv = Path(f"{csv_files_dir_path}/{directory}")
        file_list = [str(f) for f in path_to_csv.glob('**/*') if f.is_file()]
        i = 0
        dataframes = []
        all_dfs = []
        final_dfs = []
        columns = []
        for file in file_list:
            # print(file)
            file_name_seprated = (str(file)).split("\\")
            varname = file_name_seprated[2][:-4]
            file_name = file_name_seprated[1]
            globals()[varname] = pd.read_csv(file)
            # print(varname)
            columns = globals()[varname].columns
            column_for_merge = columns[-1]
            dataframes.append(globals()[varname][column_for_merge])
            all_dfs.append(globals()[varname])
        common = list(reduce(lambda i, j: i & j, (set(x) for x in dataframes)))
        for dfs in all_dfs:
            final_dfs.append(dfs[dfs[f'{column_for_merge}'].isin(common)])
        common_df = pd.concat(final_dfs)
        common_df.drop_duplicates(subset=columns, keep="first", inplace=True) #flamie ka nahi chal raha
        common_df.to_csv(f"csv_files/{file_name}/{file_name}_common.csv", encoding='utf-8', index=False)
        print(f"Saving common csv file for {file_name}")