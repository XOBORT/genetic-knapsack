from data import individual_size, pack, max_weight

def greedy_price(population, temp_price, param):
    temp_popul = population.copy()
    while True:
        price = 0
        weight = 0
        temp_popul[temp_price.index(min(temp_price))] = 0
        temp_price[temp_price.index(min(temp_price))] = 1000
        for i in range(0, individual_size()):
            if temp_popul[i] == 1:
                price += pack()[i][1]
                weight += pack()[i][2]
        if param == 0:
            population = temp_popul.copy()
        if weight <= max_weight():
            del temp_popul
            return weight, price

def decoder(population, param):
    popul_price = [0 for i in range(len(population))]
    popul_weight = [0 for i in range(len(population))]
    
    temp_price = [0 for i in range(individual_size())]
    for i in range(0, len(population)):
        for j in range(0, individual_size()):
            if population[i][j] == 1:
                popul_price[i] += pack()[j][1]
                popul_weight[i] += pack()[j][2]
                temp_price[j] = (pack()[j][1])
            else:
                temp_price[j] = (1000)

        if popul_weight[i] > max_weight():
            if param == 0:
                temp_weight_price = greedy_price(population[0], temp_price, param)
            else:
                temp_weight_price = greedy_price(population[i], temp_price, param)
            popul_price[i] = (temp_weight_price[0])
            popul_weight[i] = (temp_weight_price[1])
            
    return popul_price, popul_weight