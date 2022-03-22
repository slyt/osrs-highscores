# html_scrape.py is a simple example of parsing the 
# OSRS highscores from HTML into pandas using pandas.read_html()

import requests
import pandas as pd

base_url = "https://secure.runescape.com/m=hiscore_oldschool/overall"
skill_index = 1 # 1 = Attack
page = 1        # 1 = Frontpage

request_url = base_url + '?table=' + str(skill_index) + '&' + 'page=' + str(page)
response = requests.get(request_url)

df_list = pd.read_html(response.text, skiprows={0,0}) # For some reason row 0 was all NA, so need to skip
df = df_list[0]
df.index += 1 # 1 index instead of 0 to match highscore indexing
df.columns = ['Rank', 'Name', 'Level', 'XP']
print(df)