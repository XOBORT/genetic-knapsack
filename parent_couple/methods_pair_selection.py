from data import popul_size
from random import choices
from processing_restrictions.ways_restrictions_processing import decoder
from crossover.choosing_crossover import crossover_formation

def negative_mating(crossover, mutation, population):
    popul_price = decoder(population, 1)[0]

    temp_price = [1/popul_price[x] if popul_price[x]!= 0 else 0 for x in range(len(popul_price))]
    left = choices([x for x in range(len(popul_price))], 
                  [(popul_price[x]/sum(popul_price)) if popul_price[x]!= 0 else 0 for x in range(len(population))], 
                  k = len(population))
    right = choices([x for x in range(len(popul_price))], 
                  [((1/popul_price[x])/(sum(temp_price))) if popul_price[x]!= 0 else 0 for x in range(len(population))], 
                  k = len(population))
    for i in range(0, int(popul_size()/2)):
        crossover_formation(crossover,
                            mutation,
                            population,
                            population[left[i]].copy(),
                            population[right[i]].copy())
    del left
    del right