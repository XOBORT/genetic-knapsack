from initial_population.choosing_init_popul import choosing_initial_population
from parent_couple.methods_pair_selection import negative_mating
from selection.selection_operators import B_tournament
from processing_restrictions.ways_restrictions_processing import decoder
from data import repetitions

import random
#random.seed()

def main(init_popul, crossover, mutation):

    population = choosing_initial_population(init_popul)
    crossover = crossover
    mutation = mutation

    decision = []
    count_repetitions = 1
 
    while True:
        negative_mating(crossover, mutation, population)
        B_tournament(population)
        decision.insert(0, [population[0].copy()])
        temp_price_weight = decoder(decision[0], 0)
        popul_price = temp_price_weight[0]
        popul_weight = temp_price_weight[1]
        decision[0].append(popul_price[0])
        decision[0].append(popul_weight[0])

        if len(decision) > repetitions():
            #temp = (repetitions() if decision[i][1] == decision[i+1][1] else 0 for i in range(0, repetitions()))
            temp = 0
            for i in range(0, repetitions()):
                if decision[i][1] == decision[i+1][1]:
                    temp += 1

            if temp == repetitions():
                print("Finish")
                print(f"{count_repetitions}) Encoding - {decision[0][0]}    Price = {decision[0][1]}    Weight = {decision[0][2]}")
                return count_repetitions, decision[0][1]

        print(f"{count_repetitions}) Encoding - {decision[0][0]}    Price = {decision[0][1]}    Weight = {decision[0][2]}")
        count_repetitions += 1

if __name__ == "__main__":
    main()