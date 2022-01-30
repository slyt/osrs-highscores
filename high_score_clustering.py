# TODO:
# Get player name and experience (xp) in every skill from OSRS
# Parse xp into pandas dataframe
# Run k-means clustering on xp and plot the results. 
# Correlate size of the points in the cluster with the number of elements in the cluster. 
#   Or rather, points that are far from cluster centers are larger. This will help to detect unique accounts.


import pandas as pd
from osrs_highscores import Highscores
from osrs_highscores import Rankings

def main():
    use_pickle = True

    if not use_pickle:
        print("Not using pickle file.")
    else:
        print("Using pickle file.")


if __name__ == '__main__':
    main()


 
