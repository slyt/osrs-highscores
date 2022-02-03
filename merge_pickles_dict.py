# This script takes the pickled dictionaries collected
# from sample_defence_dict.py and merges them into 
# a single pandas dataframe.
import pandas as pd
import glob
import matplotlib.pyplot as plt
import matplotlib
from pyparsing import col

list_of_files = glob.glob("defence_pickles_dict/*")
print(list_of_files)

list_of_dicts = []

for idx, file_path in enumerate(list_of_files):
    print('idx={} loading file: {}'.format(idx, file_path))
    f = open(file_path, "rb")
    data_dict = pd.read_pickle(file_path)
    list_of_dicts.extend(data_dict)
    f.close()


# It's more efficient to create a list of dicts,
# then merge them into a single dataframe at the end,
# insead of continuously appendign dicts to a dataframe
merged_df = pd.DataFrame(list_of_dicts)
merged_df = merged_df.sort_values(['Rank'], ascending=True)

# Verify the dataframe looks good
print(merged_df.dtypes)
print(merged_df.describe())


# Plot the results
# TODO: Use seaborn to make it easier

#define colors to use
color_1 = 'steelblue'
color_2 = 'red'

#define subplots
fig,ax = plt.subplots()

ax.plot(merged_df['Rank'], merged_df["XP"], color=color_1)
ax.set_xlabel('Rank', fontsize=14) #add x-axis label
ax.set_ylabel('XP', color=color_1, fontsize=16)

ax2 = ax.twinx() #define second y-axis that shares x-axis with current plot

ax2.plot(merged_df['Rank'], merged_df['Level'], color=color_2)
ax2.set_ylabel('Level', color=color_2, fontsize=16) #add second y-axis label
ax.title.set_text('Defence XP vs Defence Rank')
plt.ticklabel_format(style='plain') 
plt.show(block=False) # Required to see plot in VSCode
input('press <ENTER> to continue')
