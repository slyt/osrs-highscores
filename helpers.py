# helper functions

import math
import requests
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
import os # Used to make directories


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

xp_level_table = [0,  # lvl 1
                  83,  # lvl 2
                  174,
                  276,
                  388,
                  512,
                  650,
                  801,
                  969,
                  1154,
                  1358,
                  1584,
                  1833,
                  2107,
                  2411,
                  2746,
                  3115,
                  3523,
                  3973,
                  4470,
                  5018,
                  5624,
                  6291,
                  7028,
                  7842,
                  8740,
                  9730,
                  10824,
                  12031,
                  13363,
                  14833,
                  16456,
                  18247,
                  20224,
                  22406,
                  24815,
                  27473,
                  30408,
                  33648,
                  37224,
                  41171,
                  45529,
                  50339,
                  55649,
                  61512,
                  67983,
                  75127,
                  83014,
                  91721,
                  101333,
                  111945,
                  123660,
                  136594,
                  150872,
                  166636,
                  184040,
                  203254,
                  224466,
                  247886,
                  273742,
                  302288,
                  333804,
                  368599,
                  407015,
                  449428,
                  496254,
                  547953,
                  605032,
                  668051,
                  737627,
                  814445,
                  899257,
                  992895,
                  1096278,
                  1210421,
                  1336443,
                  1475581,
                  1629200,
                  1798808,
                  1986068,
                  2192818,
                  2421087,
                  2673114,
                  2951373,
                  3258594,
                  3597792,
                  3972294,
                  4385776,
                  4842295,
                  5346332,
                  5902831,
                  6517253,
                  7195629,
                  7944614,
                  8771558,
                  9684577,
                  10692629,
                  11805606,
                  13034431,  # lvl 99
                  14391160,  # lvl 100 (virtual level)
                  15889109,
                  17542976,
                  19368992,
                  21385073,
                  23611006,
                  26068632,
                  28782069,
                  31777943,
                  35085654,
                  38737661,
                  42769801,
                  47221641,
                  52136869,
                  57563718,
                  63555443,
                  70170840,
                  77474828,
                  85539082,
                  94442737,
                  104273167,
                  115126838,
                  127110260,
                  140341028,
                  154948977,
                  171077457,
                  188884740,  # level 126 (virtual level)
                  200000000]  # max XP

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
        df['Page'] = page_number
        #print(df)
        #print(df.dtypes)
        return df

    else:
        print('Error: response status code {} for url {}'.format(response.status_code, request_url))




def create_sample_list(samples_to_take, population_size):
    ''' returns a list of random samples

    This returned list can be iterated over to provide random and unique samples
    '''
    #samples_to_take = 80_000 # There are 80_000 pages to query per skill
    
    samples = random.sample(range(1,population_size+1), samples_to_take)
    return samples



def binary_search(skill):
    # Get page 80_000 to determine minimum level
    start_page = 80_000 # TODO: Allow function to find arbetrary level pages
    max_page_level = 0
    df = get_page_as_df(skill=skill, page_number=start_page)

    # Save df so that another thread can plot in real time
    path = 'data/' + str(skill) + '/' # create directory if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)
        print("Created directory: ", path)
    df.to_csv(path + skill + '.csv', mode='a', index=False)

    start_level = df.at[25, 'Level']
    start_xp = df.at[25, 'XP']
    print('start_page={} start_level={} start_xp={}'.format(start_page, start_level, start_xp))

    current_level=start_level
    current_page = start_page
    max_page_level = current_level
    unique = pd.Series(df['Level']).unique() # Page contains all the same level

    # to run GUI event loop
    plt.ion()

    while max_page_level < 99:
        #df = get_page_as_df(skill=skill, page_number=current_page)
        #print(pd.Series(df['Level']))
        
        
        # Initial condition, always decrease
        delta = int(round(current_page/2))
        current_page = current_page - delta

        iteration = 0
        while len(unique) == 1: # While all levels on the page are the same
            print("Checking page {} ({})".format(current_page, skill))
            df = get_page_as_df(skill=skill, page_number=current_page)
            df.to_csv(path + skill + '.csv', mode='a', index=False, header=False)
            unique = pd.Series(df['Level']).unique() # Page contains all the same level
            if len(unique) != 1: # Termination condition
                break
            page_level = df.at[25, 'Level']
            delta=int(round(delta/2)) # Update delta
            if delta == 0: delta=1 # Just in case we ever round down to 0, we still want to progress
            print("skill={} iteration={} current_page={} delta={} page_level={} unique={}".format(skill, iteration, current_page, delta, page_level, unique))
            

            if page_level > current_level: # Increase
                current_page = current_page + delta
            else: # Decrease
                current_page = current_page - delta
            sleep_duration = random.uniform(1, 3) # Sleep for slightly random amount of time
            #print("... now sleeping for {}".format(sleep_duration))
            time.sleep(sleep_duration) # Throttle requests to API (should probably do randomly)
            iteration+=1
        
        page_url = request_page(skill=skill, page=current_page)
        max_page_level = max(unique)
        current_level = max_page_level # Now looking for the next level
        unique=[max_page_level] # Make sure algo doesn't skip inner loop on next iteration of outer loop
        print('skill={} Level change {} max_page_level {} on page {}: {}'.format(skill, unique, max_page_level, current_page, page_url))

        

    # Example Strength
    # Start page = 80_000
    # 80_000 = lvl 60 (280,228XP)
    # Looking for page where level is level != curr_level
    # Decrease by half (80_000 - 80_000/2) = 40_000 = lvl 80
    # Increase by half (40_009 + 40_000/2) = 60_000 = lvl 70
    # Increase by half (60_000 + 20_000/2) = 70_000 = lvl 65
    # Increase by half (70_000 + 10_000/2) = 75_000 = lvl 62
    # Increase by half (75_000 + 5_000/2) = 77_500 = lvl 61
    # Increase by half (77_500 + 2_500/2) = 78_750 = level 60
    # Decrease by half (78_750 - 1250/2) = 78_125 = level 60
    # Decrease by half (78_125 - 625/2) = 77_812 = Level 60
    # Decrease by half (77_812 - 313/2) = 77_655 = level 60
    # Decrease by half (77_655 - 157/2) = 77_576 = level 61
    # Increase by half (77_576 + 79/2) = 77_616 = level 61
    # Increase by half (77_616 + 40/2) = 77_636 = level 61
    # Increase by half (77_636 + 20/2) = 77_646 = level 61/60!!!
    # New start_page = 77_646

    


    # Alternate, more effiecient yet complex approach: 
    # Look at XP and calculate XP/page as we search