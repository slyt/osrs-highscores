# helper functions

import math
import requests
import pandas as pd


base_url = "https://secure.runescape.com/m=hiscore_oldschool/overall"

default_skills = {
    "overall":0,
    "attack":1,
    "defence":2,
    "strength":3,
    "hitpoints":4,
    "ranged":5,
    "prayer":6,
    "magic":7,
    "cooking":8,
    "woodcutting":9,
    "fletching":10,
    "fishing":11,
    "firemaking":12,
    "crafting":13,
    "smithing":14,
    "mining":15,
    "herblore":16,
    "agility":17,
    "thieving":18,
    "slayer":19,
    "farming":20,
    "runecraft":21,
    "hunter":22,
    "construction":23,
}

def request_page(skill='overall', page=1):

    skill_index = default_skills.get(skill.lower(), -1)
    if skill_index == -1:
        print("Error, invalid skill name supplied!")
    #print("Requesting skill {} (skill_index {}) page {}".format(skill, skill_index, page))

    request_url = base_url + '?table=' + str(skill_index) + '&' + 'page=' + str(page)
    #print('request_url: ', request_url)
    return request_url

def page_number_to_rank_range(page_number=1):
    # 1 = (1,25) 25-1 = 24
    # 2 = (26, 50) 50-26 = 24

    if page_number > 80_000 or page_number < 0:
        print("Error, page_number must be between 0 and 80,000. 0 and 1 are treated as the same page.")
        return (-1,-1)

    if page_number == 0: # 0 and 1 are treated the same page index on highscores
        page_number = 1
    last_rank_on_page = page_number * 25
    first_rank_on_page = last_rank_on_page - 24

    return (first_rank_on_page, last_rank_on_page)

def rank_to_page_number(rank):
    if rank <= 0 or rank > 2_000_000:
        print("Error: Highscores only rank from 1 to 2,000,000")
        return -1

    page_number = math.ceil(rank / 25) # 25 ranks per page
    return page_number

def get_page_as_df(skill, page_number):
    request_url = request_page(skill=skill, page=page_number)
    response = requests.get(request_url)
    if response:
        #print(response.text)
        df_list = pd.read_html(response.text, skiprows={0,0}) # For some reason row 0 was all NA, so need to skip
        df = df_list[0]
        df.index += 1 # 1 index instead of 0 to match higscore indexing
        df.columns = ['Rank', 'Name', 'Level', 'XP']
        #print(df)
        #print(df.dtypes)
        return df

    else:
        print('Error: response status code {} for url {}'.format(response.status_code, request_url))





