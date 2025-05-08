from random import randint
from data import individual_size

def gene(individual):
    a = randint(0, individual_size()-1)
    if individual[a] == 1:
        individual[a] = 0
    else:
        individual[a] = 1

def saltation(individual):
    point = [randint(1, individual_size()-1), randint(1, individual_size()-1)]
    for i in range(0, 2):
        if individual[point[i]] == 1:
            individual[point[i]] = 0
        else:
            individual[point[i]] = 1

def inversion(individual):
    point = [randint(1, individual_size()-1), randint(1, individual_size()-1)]
    for i in range(0, individual_size()):
        if i > min(point) or i <= max(point):
            if individual[i] == 1:
                individual[i] = 0
            else:
                individual[i] = 1

def translocation(individual):
    point = [randint(1, individual_size()-1), randint(1, individual_size()-1)]
    for i in range(0, individual_size()):
        if i < min(point) or i >= max(point):
            if individual[i] == 1:
                individual[i] = 0
            else:
                individual[i] = 1

def chromosome(individual):
    for i in range(0, individual_size()):
        if individual[i] == 1:
            individual[i] = 0
        else:
            individual[i] = 1