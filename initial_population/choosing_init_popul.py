from data import popul_size
from random import randint
from initial_population.methods_creating_initial_population import *

def choosing_initial_population(init_popul):
    match init_popul:
        case 1:
            return [rand_encoding() for x in range(popul_size())]
        case 2:
            return [rand_encoding_check() for x in range(popul_size())]
        case 12:
            temp_randint = randint(1, popul_size()-1)
            return [rand_encoding() for x in range(temp_randint)] + \
                [rand_encoding_check() for x in range(temp_randint, popul_size())]
        case 13:
            return [rand_encoding() for x in range(popul_size()-1)] + [greedy_encoding()]
        case 23:
            return [rand_encoding_check() for x in range(popul_size()-1)] + [greedy_encoding()]
        case 123:
            temp_randint = randint(1, popul_size()-2)
            return [rand_encoding() for x in range(0, temp_randint)] + \
            [rand_encoding_check() for x in range(temp_randint, popul_size() - 1)] + \
            [greedy_encoding()]