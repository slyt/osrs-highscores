# This saves each osrs highscore page as a pickled Dataframe.
# This is not as efficient as saving as a python dictionary, so 
# sample_defence_dict.py should be used instead.
import helpers
import time
import pandas as pd
import pickle

pickle_directory = "defence_pickles/"
skill = "defence"

sample_list = helpers.create_sample_list(3)

for page_number in sample_list:
    page_df = helpers.get_page_as_df(skill=skill, page_number=page_number)
    filename = skill + "_" + str(page_number)
    filepath = pickle_directory + filename
    data_dict = page_df.to_pickle(filepath)
    time.sleep(1) # Throttle requests to API (should probably do randomly)
