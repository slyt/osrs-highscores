# This script plots real time data from a CSV that is being
# continuously updated by another script, data_gen.py
# See https://www.youtube.com/watch?v=Ercd-Ip5PfQ&t=3s

import random
from itertools import count
from matplotlib import animation
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from helpers import xp_level_table

plt.style.use('fivethirtyeight')

skill = 'defence'

print(xp_level_table)
level_table = list(range(1, 128))
print(level_table)

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
    
    plt.cla() # clear all axis so that we don't keep writing over line
    plt.scatter(data['Rank'], data['Level'])
    plt.xlabel("Rank")
    plt.ylabel("Level")

    fig = plt.figure()
    #plt.plot(data['Level'], y2, label='Channel 2')

    #plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), # Get current figure
                    animate, # Call animate function
                    interval=1000 # every 1000ms
                    )


plt.show()



