from random import choices, randint
from data import individual_size
from mutation.choosing_mutation import mutation_formation

def probability_of_mutation(mutation, individual):
    if choices([0, 1], [1, 9]) == [0]:
        mutation_formation(mutation, individual)

#Single-point crossover
def single_point(mutation, population, parent1, parent2):
    for i in range(0, randint(1, individual_size()-1)):
        parent1[i], parent2[i] = parent2[i], parent1[i]

    probability_of_mutation(mutation, parent1)
    population.append(parent1)
    probability_of_mutation(mutation, parent2)
    population.append(parent2)

#Duo-point crossover
def duo_point(mutation, population, parent1, parent2):
    point = [randint(1, individual_size()-1), randint(1, individual_size()-1)]
    for i in range(0, individual_size()):
        if i < min(point) or i >= max(point):
            parent1[i], parent2[i] = parent2[i], parent1[i]

    probability_of_mutation(mutation, parent1)
    population.append(parent1)
    probability_of_mutation(mutation, parent2)
    population.append(parent2)


#N-point crossower
def n_point(mutation, population, parent1, parent2):
    n = randint(3, individual_size()-1)
    point = [x for x in range(1,n+1)]
    for i in range(0, n+1):
        for j in range(0, individual_size()):
            if i == 0:
                if j < point[i]:
                    parent1[j], parent2[j] = parent2[j], parent1[j]
            elif i == n and j > point[i-1]-1 and i%2 == 0:
                parent1[j], parent2[j] = parent2[j], parent1[j]
            elif i%2 == 0 and i != n:
                    if j > point[i-1]-1 and j < point[i]:
                        parent1[j], parent2[j] = parent2[j], parent1[j]

    probability_of_mutation(mutation, parent1)
    population.append(parent1)
    probability_of_mutation(mutation, parent2)
    population.append(parent2)