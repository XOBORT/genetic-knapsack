from crossover.crossover_operators import single_point, duo_point, n_point

def crossover_formation(crossover, mutation, population, parent1, parent2):
    match crossover:
        case 1:
            single_point(mutation, population, parent1, parent2)
        case 2:
            duo_point(mutation, population, parent1, parent2)
        case 3:
            n_point(mutation, population, parent1, parent2)