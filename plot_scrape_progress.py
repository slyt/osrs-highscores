# This script plots real time data from a CSV that is being
# continuously updated by another script, data_gen.py
# See https://www.youtube.com/watch?v=Ercd-Ip5PfQ&t=3s

import random
from itertools import count
from matplotlib import animation
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from helpers import xp_level_table
import numpy as np

plt.style.use('fivethirtyeight')

skill = 'defence'

#print(xp_level_table)
level_table = list(range(1, 128))
#print(level_table)

x_vals = []#[0,1,2,3,4,5]
y_vals = []#[0,1,3,2,4,5]

#plt.plot(x_vals, y_vals)

index = count() # Generator that counts up

def animate(i):

    # Randomly generate y-data while incrementing x-data
    #x_vals.append(next(index))
    #y_vals.append(random.randint(0,5))
    
    # Read live data from CSV
    data = pd.read_csv('data/' + skill + '.csv')

    # TODO: Transform page numbers in into matrix and plot as a single image
    total_count = len(data['Page'])
    print(f'Total count: {total_count}')
    unique_count = len(pd.unique(data['Page']))
    print(f'Unique count: {unique_count}')

    # Get the frequency of each page occuring
    page_frequency_df = data['Page'].value_counts()
    page_frequency_df.index = page_frequency_df.index -1 # Offset by one since highscores index at 1
    

    # Initialize empty np array
    np_matrix = np.zeros(80_000)
    # Iterate over page_frequency_df (there's probably a vectorized way to do this)
    for index, value in page_frequency_df.iteritems():
        np_matrix[index] = value 
   
    np_grid = np_matrix.reshape((250, 320))
    #print(np_grid)
    plt.imshow(np_grid, cmap='hot', interpolation='nearest')
    plt.title(f"Heatmap of page scrape progress for {skill}")



    return
    exit() # TODO: Remove early exit and uncomment plotting code

    
    plt.cla() # clear all axis so that we don't keep writing over line
    plt.hist(data['Page'], bins=1000)
    plt.xlabel("Page")
    plt.ylabel("Count")

    fig = plt.figure()
    #plt.plot(data['Level'], y2, label='Channel 2')

    #plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), # Get current figure
                    animate, # Call animate function
                    interval=1000 # every 1000ms
                    )


plt.show()



