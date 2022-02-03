# This saves each osrs highscore page as a pickled diction.
# It takes care to batch the pickles so as to save space on disk.
# It also has random throttling so as to be kind to the OSRS highscore API

import helpers
import time
import pandas as pd
import pickle
import random

pickle_directory = "defence_pickles_dict/"
skill = "defence"

sample_list = helpers.create_sample_list(30)
list_of_dicts = []

# Since 1 page of data is about 1KB, but block size on disk is 4KB,
# we can increase disk utilzation by saving pages in batches
batch = []
max_batch_size = 10 


for idx, page_number in enumerate(sample_list):
    page_df = helpers.get_page_as_df(skill=skill, page_number=page_number)
    list_of_dicts.extend(page_df.to_dict('records'))
    batch.append(page_number) # Keep track of the page numbers in this batch

    # Only write to file if max_batch_size reached
    if len(batch) >= max_batch_size:
        filename = skill + "_" + str(idx+1) + ".pickle"
        filepath = pickle_directory + filename
        print("max_batch_size ({}) reached. Writing out these {} pages {} to file {}".format(max_batch_size, len(batch), batch, filename))
        with open(filepath, 'wb') as handle:
            pickle.dump(list_of_dicts, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
        # Reset for next batch
        list_of_dicts = []
        batch = []
    sleep_duration = random.uniform(1, 3) # Sleep for slightly random amount of time
    print("page_number={} idx={}... now sleeping for {}s".format(page_number, idx, sleep_duration))
    time.sleep(sleep_duration) # Throttle requests to API (should probably do randomly)

# Write out the final batch incase it wasn't a multiple of max_batch_size
if len(batch) > 0:
    filename = skill + "_" + "final" + ".pickle"
    filepath = pickle_directory + filename
    print("Writing final batch of size {} with pages {} to file {}".format(len(batch), batch, filename))
    with open(filepath, 'wb') as handle:
        pickle.dump(list_of_dicts, handle, protocol=pickle.HIGHEST_PROTOCOL)
