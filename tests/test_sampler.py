# Test the sampler functionality

import random         # used to sample data
import seaborn as sns # used to visualize result
from timeit import default_timer as timer # Used to measure sampling performance

# We want to sample the entire population randomly without replacement
# so the samples_to_take == the populatino size
samples_to_take = 80_000 # There are 80_000 pages to query per skill


start = timer()
#print("population_size: {}".format(population_size))
samples = random.sample(range(1,samples_to_take+1), samples_to_take)
end = timer()
print(str(len(samples)) + " samples generated in " +  str(end-start) + " seconds.")
print("min: ", min(samples), " max: ", max(samples))

exit()

# This is very slow, likely due to the population needing to be re-allocated anor/or copied on each sample
population = set(range(1, samples_to_take+1)) # Index starting at 1, since high score page numbers are 1 indexed
samples = []
start = timer()
for i in range(samples_to_take):
    population_size = len(population)
    #print("population_size: {}".format(population_size))
    sample = random.sample(population, 1)
    sample = int(sample[0])
    population.remove(sample) # Remove the sample from the population
    samples.append(sample)
end = timer()
print(str(len(samples)) + " samples generated in " +  str(end-start) + " seconds.")


