from mutation.mutation_operators import *

def mutation_formation(mutation, individual):
    match mutation:
        case 1:
            gene(individual)
        case 2:
            saltation(individual)
        case 3:
            inversion(individual)
        case 4:
            translocation(individual)
        case 5:
            chromosome(individual)
