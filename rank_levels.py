# This script calculates the level required to achieve a certain rank in a Old School Runscape skill
from osrs_highscores import Highscores
from osrs_highscores import Rankings
import json
import pandas as pd
import matplotlib.pyplot as plt

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


def add_commas(number):
    return ("{:,}".format(number))


def main():
    use_pickle = True
    rank = 1000000  # 1,000,000

    if not use_pickle:
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
        list_xp_to_rank = []
        list_rank_levels = []
        for skill_name in labels['skill_list']:
            rank_xp = int(ranks.get_rank_in_skill(skill_name, rank).xp)
            rank_level = get_level(rank_xp)
            print(
                "{skill_name}: {rank_xp} xp (lvl {rank_level}) for rank {rank}.".format(
                    skill_name=skill_name,
                    rank_xp = add_commas(int(rank_xp)),
                    rank_level=rank_level,
                    rank=rank))
            list_xp_to_rank.append(rank_xp)
            list_rank_levels.append(rank_level)

        df_skill_list['xp_to_rank'] = list_xp_to_rank
        df_skill_list['rank_level'] = list_rank_levels
        df_skill_list.to_pickle(
            'rank_levels_' + str(
                rank) + '.pkl')  # Save to pickle file so we don't need to hit network

    else:  # load from pickle
        df_skill_list = pd.read_pickle('rank_levels_' + str(rank) + '.pkl')

    # TODO: Normalize based on XP per hour. Project time to reach rank based on XP per hour rates.

    # Plot data
    df_skill_list = df_skill_list.sort_values(by='xp_to_rank', ascending=False, ignore_index=True)
    ax = df_skill_list.plot(kind='barh',
                            x='skill_list',
                            y='xp_to_rank',
                            title='Runescape XP till rank {}'.format(rank),
                            color=df_skill_list['colors'],
                            width=0.8,
                            legend=False)
    for index, row in df_skill_list.iterrows():
        text = add_commas(row['xp_to_rank']) + 'xp - lvl ' + str((row['rank_level']))
        print(text)
        plt.text(x=row['xp_to_rank'],
                 y=index,
                 s=text,
                 color="black",
                 va='center',
                 ha='left',
                 size=10)
        # plt.text(s=str(pr) + '%', x=pr - 5, y=i, color="b",
        #         verticalalignment="center", horizontalalignment="left", size=10)
    ax.set_xlabel('XP')
    ax.set_ylabel('Skill')
    plt.ticklabel_format(axis='x', style='plain')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
