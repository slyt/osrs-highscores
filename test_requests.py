# Test requests made to OSRS highscores for performance
import time # Used to throttle requests
import helpers
import pandas as pd

skill = "defence"
page = 2
print("page: ", page)
df_page = helpers.get_page_as_df(skill=skill, page_number=page)
print(df_page)

time.sleep(5)

rank = 1_888_888
page_number_for_rank = helpers.rank_to_page_number(rank)
print("rank: {} page_number_for_rank: {}".format(rank, page_number_for_rank))
df = helpers.get_page_as_df(skill=skill, page_number=page_number_for_rank)
print(df)
