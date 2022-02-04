# helper functions

import math
import requests
import pandas as pd
import random
import time


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
    start_level = df.at[25, 'Level']
    start_xp = df.at[25, 'XP']
    print('start_page={} start_level={} start_xp={}'.format(start_page, start_level, start_xp))

    current_level=start_level
    current_page = start_page
    max_page_level = current_level
    unique = pd.Series(df['Level']).unique() # Page contains all the same level


    while max_page_level < 99:
        #df = get_page_as_df(skill=skill, page_number=current_page)
        #print(pd.Series(df['Level']))
        
        
        # Initial condition, always decrease
        delta = int(round(current_page/2))
        current_page = current_page - delta

        iteration = 0
        while len(unique) == 1: # While all levels on the page are the same
            #print("Checking page {}".format(current_page))
            df = get_page_as_df(skill=skill, page_number=current_page)
            unique = pd.Series(df['Level']).unique() # Page contains all the same level
            if len(unique) != 1: # Termination condition
                break
            page_level = df.at[25, 'Level']
            delta=int(round(delta/2)) # Update delta
            if delta == 0: delta=1 # Just in case we ever round down to 0, we still want to progress
            print("iteration={} current_page={} delta={} page_level={} unique={}".format(iteration, current_page, delta, page_level, unique))
            

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
        print('Level change {} max_page_level {} on page {}: {}'.format(unique, max_page_level, current_page, page_url))

        

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