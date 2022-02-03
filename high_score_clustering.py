# TODO:
# - [X] Implement random sampler for each page of highscores
# - [x] Parse XP tables into pandas dataframe
# - [ ] Get player name and experience (xp) in every skill from OSRS
# - [ ] Run k-means clustering on xp and plot the results. 
# - [ ] Correlate size of the points in the cluster with the number of elements in the cluster. 
# - [ ]  Or rather, points that are far from cluster centers are larger. This will help to detect unique accounts.


import pandas as pd
from osrs_highscores import Highscores
from osrs_highscores import Rankings
import helpers # helper functions

def main():
    use_pickle = True
    rank = 1_000
    print(rank)

    if not use_pickle:
        print("Not using pickle file.")
        
        # Get top ranks and xp for every skill
        ranks = Rankings()

        labels = {'skill_list': ['attack', 'hitpoints', 'mining',
                                 'strength', 'agility', 'smithing',
                                 'defence', 'herblore', 'fishing',
                                 'ranged', 'thieving', 'cooking',
                                 'prayer', 'crafting', 'firemaking',
                                 'magic', 'fletching', 'woodcutting',
                                 'runecraft', 'slayer', 'farming',
                                 'construction', 'hunter'],
                  'colors': ['#440b05', '#7b7a6c', '#27281e',
                             '#025736', '#0f0f32', '#595943',
                             '#6177c0', '#054207', '#698aae',
                             '#2e3e0c', '#3d2231', '#521e5b',
                             '#dfe0e4', '#483626', '#a85b00',
                             '#a2967d', '#032727', '#8e703a',
                             '#9b9d8e', '#100f0d', '#123311',
                             '#928774', '#564f36']
                  }

        df_skill_list = pd.DataFrame(labels)

        player_stats = {}
        for skill_name in labels['skill_list']:
            current_rank_obj = ranks.get_rank_in_skill(skill_name, rank)
            xp = int(current_rank_obj.xp)
            level = get_level(xp)
            username = current_rank_obj.username
            
            print(
                "{skill_name}: {rank_xp} xp (lvl {rank_level}) for rank {rank}. {username}'s current xp: {user_current_xp} (lvl {user_level}). XP difference to rank {rank}: {xp_difference_to_rank}".format(
                    skill_name=skill_name,
                    rank_xp = helpers.add_commas(int(rank_xp)),
                    rank_level=get_level(rank_xp),
                    rank=rank,
                    username=username,
                    user_current_xp=helpers.add_commas(int(user_current_xp)),
                    user_level=get_level(user_current_xp),
                    xp_difference_to_rank=(xp_difference_to_rank)))
        

    else:
        print("Using pickle file.")


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
    for index in range(len(xp_level_table) - 1, -1, -1):  # iterate backward
        if xp >= xp_level_table[index]:
            # print("{} is >= {} so level is {}".format(xp, xp_level_table[index], index + 1))
            return index + 1
    return -1

if __name__ == '__main__':
    main()


 
