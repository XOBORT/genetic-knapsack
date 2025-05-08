from processing_restrictions.ways_restrictions_processing import decoder
from random import choices
from data import popul_size

def B_tournament(population):
    temp_popul = population.copy()
    popul_price = decoder(temp_popul, 1)[0]
    population.clear()
    pr = choices([x for x in range(0, len(temp_popul))], 
                  [1/len(temp_popul) for x in range(0, len(temp_popul))], 
                   k= popul_size() * 2)
    for i in range(0, popul_size() * 2):
        if i == 0:
            population.append(temp_popul[popul_price.index(max(popul_price))])
        elif i % 2 == 0:
            population.append(temp_popul[popul_price.index(max(popul_price[pr[i]], popul_price[pr[i+1]]))])
    del temp_popul
    return population