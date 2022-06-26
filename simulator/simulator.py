
# Generate a database of highscores with 2_000_000 entries
# ['Rank', 'Name', 'Level', 'XP']
# XP ranging from 200_000_000 to 0

import pandas as pd
import random
from timeit import default_timer as timer # Used to measure sampling performance

from pyparsing import alphas8bit

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


def get_level(xp):
    '''
    get_level(): Returns the level for the given xp
    '''
    for index in range(len(xp_level_table) - 1, -1, -1):  # iterate backward
        if xp >= xp_level_table[index]:
            # print("{} is >= {} so level is {}".format(xp, xp_level_table[index], index + 1))
            return index + 1
    return -1

def generate_xp(level, n):
    # Generate a list of viable XP for a given level of length n

    start_xp = xp_level_table[level-1] 
    end_xp = xp_level_table[level] - 1 # Subtract 1 XP to stay within current level
    #print(f"start_xp: {start_xp}")
    #print(f"end_xp: {end_xp}")
    
    if level == 99:
        end_xp = xp_level_table[len(xp_level_table)-1] # Level 99 XP can go up to 200M

    
    xp_list = []
    for i in range(n): # TODO there's probably a better way to do this with random library
        xp_list.append(random.randint(start_xp,end_xp))
    xp_list.sort()
    #print(f"xp_list: {xp_list}, len: {len(xp_list)}")

    return xp_list

def generate_name(length):
    # Randomly generate a string of given length
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    for i in range(0, length):
        letter_index = random.randint(0, 25)
        name += alphabet_lower[letter_index]
    return name



def generate_uniform_data(number_of_players):
    
    entries_per_level = int(number_of_players / 99)
    remainder = number_of_players % 99.0
    print(f"entries per level: {entries_per_level}")
    print(f"remainder: {remainder}")

    # TODO: Distrubute the remainder somehow
    data_all = pd.DataFrame(columns={'Rank', 'Name', 'Level', 'XP'}) # Generate a dataframe per level
    print(data_all)

    rank = 0 # Need to count backward since highest XP is rank 1
    for level_block in range(99, 0, -1):
        start = timer()
        print(f"Generating data for level {level_block}")

        data_level = pd.DataFrame(columns={'Rank', 'Name', 'Level', 'XP'}) # Generate a dataframe per level

        xp_list = generate_xp(level_block, entries_per_level)
        for entry in range(entries_per_level+1, 1, -1): 
            #print(f"level block: {level_block}")
            #print(f"entry: {entry}")
            
            rank += 1
            
            #print(f"entry:{entry}, rank:{rank}, xp_list_len: {len(xp_list)}")

            data_level = data_level.append({
                "Rank": rank,
                "Name": generate_name(20),
                "Level": level_block,
                "XP": xp_list[entry-2] # Counting down is weird, so we minus 2
            }, ignore_index=True)
    
        data_all = data_all.append(data_level)

        # Save data to pickle per level so that the we can checkpoint our simulation
        directory = "simulated_output_per_level\\"
        filename = "simulated_data_" + str(number_of_players) + "_players_" + str(level_block) + "_level"
        #filename = "simulated_data_" + number_of_players + "_players" + level + "_level"
        print(f"Saving pickle checkpoint to {directory + filename}.pkl")
        data_level.to_pickle(directory + filename + '.pkl')  # Save to pickle file so we don't need to hit network

        end = timer()
        print(f"Level {level_block} completed in {str(end-start)} seconds.")
    return data_all


def main():

    number_of_players = 99*20_202 # 2_000_000 players / 99 = 20_202
    print(f"Simulating OSRS highscores with {number_of_players} players.")
    uniform_data = generate_uniform_data(number_of_players) 
    directory = "simulated_output\\"
    filename = "simulated_data_" + str(number_of_players) + "_players"
    #filename = "simulated_data_" + number_of_players + "_players" + level + "_level"
    uniform_data.to_pickle(directory + filename + '.pkl')  # Save to pickle file so we don't need to hit network
    print(uniform_data)

if __name__ == "__main__":
    main()