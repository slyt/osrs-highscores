from operator import index
import pandas as pd
import glob
import pickle

list_of_files = glob.glob("defence_pickles/*")
print(list_of_files)


list_of_small_dfs = []

for file_path in list_of_files:
    f = open(file_path, "rb")
    small_df = pd.read_pickle(file_path)
    list_of_small_dfs.append(small_df)
    f.close()

#print(data_list)

merged_df = pd.concat(list_of_small_dfs, ignore_index=False)
print(merged_df.dtypes)
print(merged_df.describe())