from osrs_highscores import Highscores
from osrs_highscores import Rankings
import json
import pandas as pd
import matplotlib.pyplot as plt

def add_commas(number):
    return ("{:,}".format(number))

def main():
    use_pickle = False
    skill = 'runecraft'

    if not use_pickle:
        ranks = Rankings()
        million = 1000000
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
        df_skill_distribution = pd.DataFrame({'rank', 'xp'})

        for rank in range(0, 1000002, 10):
            if rank == 0: # Offset first entry by one
                rank = 1
            skill_xp = int(ranks.get_rank_in_skill(skill, rank).xp) # TODO: Estimate time to complete processing
            new_row = {'rank':int(rank), 'xp':int(skill_xp)}
            print(new_row)
            df_skill_distribution = df_skill_distribution.append(new_row, ignore_index=True)

        print(df_skill_distribution.describe())
        df_skill_distribution.to_pickle(
            'xp_distribution-' + skill + '.pkl')  # Save to pickle file so we don't need to hit network

    else:  # load from pickle
        df_skill_distribution = pd.read_pickle('xp_distribution-' + skill + '.pkl')

    # TODO: Plot level (and virtual level) on right hand axes
    # TODO: Plot skill milestones

    # Plot data
    df_skill_distribution = df_skill_distribution.sort_values(by='rank', ascending=True)
    ax = df_skill_distribution.plot(kind='line',
                            x='rank',
                            y='xp',
                            title='Runescape XP distribution of {}'.format(skill),
                            #color=df_skill_list['colors'],
                            #width=0.5, # only for kind='bar'
                            legend=False)
    #for i, xp_amount in enumerate(df_skill_distribution["xp"]):
    #    plt.text(x=xp_amount, y=i, s=add_commas(xp_amount), color="black", va='center', size=1)
        #plt.text(s=str(pr) + '%', x=pr - 5, y=i, color="b",
        #         verticalalignment="center", horizontalalignment="left", size=10)
    ax.set_xlabel('rank')
    ax.set_ylabel('xp')
    plt.ticklabel_format(axis='y', style='plain')
    plt.ticklabel_format(axis='x', style='plain')
    plt.xticks(fontsize=8, rotation=45)
    plt.semilogy()
    plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
