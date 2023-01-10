from random import randint
from random import shuffle
import random
from collections import Counter
#Data
L = 15
Popul = 50
initial_population = [] * Popul * 2
initial_price = [] * Popul
initial_weight = [] * Popul
init_popul = 0
cross = 0
mut = 0
M = []
uniformity = 0

#Create list №/Price/Weight
P = 100
pack = [[1, 1, 5],
        [2, 29, 14],
        [3, 23, 14],
        [4, 16, 22],
        [5, 2, 30],
        [6, 17, 8],
        [7, 8, 17],
        [8, 1, 28],
        [9, 17, 19],
        [10, 21, 12],
        [11, 28, 25],
        [12, 16, 10],
        [13, 18, 16],
        [14, 27, 22],
        [15, 6, 10]]

###################################### Methods select initial population\|/
#Random encoding without check
def encoding():
    codir = [] * L
    codir.clear()
    for i in range(0, L):
        codir.insert(i, randint(0, 1))
    return codir

#Random encoding with check
def encoding_check():
    codir = [] * L
    codir.clear()
    Pver = 0
    for i in range(0, L):
        codir.insert(i, randint(0, 1))
        #check
        if int(codir[i]) == 1:
            Pver += int(pack[i][2])
    if Pver <= P:
        return codir
    else:
        return encoding_check()

#Greedy algorithm 
def greedy_algorithm():
    codir = [] * L
    codir.clear()
    codir = [0 for i in range(0, L)]
    Cmax = 0
    Pmax = 0
    pack.sort(key=lambda x: x[2])
    pack.sort(key=lambda x: x[1], reverse=True)
    for i in range(0, L):
        if Pmax <= P:
            pop = Pmax + pack[i][2]
            if pop > P:
                continue
            else:
                codir[(int(pack[i][0])-1)] = 1
                Pmax += pack[i][2]
                Cmax += pack[i][1]
    pack.sort(key=lambda x: x[0])
    return codir
###################################### Methods select initial population/|\

###################################### Selection parent couple\|/
#Negative associative mating
def negative_mating():
    global initial_population, initial_price, initial_weight
    decoder(initial_population, initial_price, initial_weight, 1)
    #'''
    t = sorted(initial_price)
    left = [] * int(len(t)/2)
    right = [] * int(len(t)/2)
    for i in range(0, int(Popul/2)):
        left.insert(i, t[i])
    for i in range(0, int(Popul/2)):    
        right.insert(i, t[i+int(Popul/2)])
    shuffle(left)
    shuffle(right)
    for i in range(0, int(Popul/2)):
        sel_cross(initial_population[initial_price.index(left[i])], initial_population[initial_price.index(right[i])])
    t.clear()
    left.clear()
    right.clear()
###################################### Selection parent couple/|\

###################################### Processing restrictions way \|/
#Decoder, greedy algorithm
def decoder(arr1, arr2, arr3, param):
    arr2.clear()
    arr3.clear()
    C_test = []
    for i in range(0, len(arr1)):
        C_test.clear()
        Pver = 0
        Cver = 0
        for j in range(0, L):
            if int(arr1[i][j]) == 1:
                Pver += int(pack[j][2])
                Cver += int(pack[j][1])
                C_test.append(pack[j][1])
            else:
                C_test.append(1000)
            if Pver <= P and j == L-1:
                arr2.append(Cver)
                arr3.append(Pver)
            elif Pver > P and j == L-1: 
                arr_test = arr1[i].copy()
                while Pver > P and Pver != P:
                    Pver = 0
                    Cver = 0
                    if param == 0:
                        arr1[i][C_test.index(min(C_test))] = 0
                    elif param == 1:
                        arr_test[C_test.index(min(C_test))] = 0
                    C_test[C_test.index(min(C_test))] = 1000
                    for g in range(0, L):
                        if param == 0:
                            if int(arr1[i][g]) == 1:
                                Pver += int(pack[g][2])
                                Cver += int(pack[g][1])
                        elif param == 1:
                            if int(arr_test[g]) == 1:
                                Pver += int(pack[g][2])
                                Cver += int(pack[g][1])
                arr_test.clear()            
                arr2.append(Cver)
                arr3.append(Pver)
###################################### Processing restrictions way /|\

###################################### Crossover operators \|/
#Choosing crossover
def sel_cross(arr1, arr2):
    if cross == 1:
        single_cross(arr1, arr2)
    elif cross == 2:
        duo_cross(arr1, arr2)
    elif cross == 3:
        n_cross(arr1, arr2)

#Single-point crossover
def single_cross(arr1, arr2):
    global initial_population
    arr11 = arr1.copy()
    arr22 = arr2.copy()
    Temp = randint(1, L-1)
    for i in range(0, Temp):
        arr11[i], arr22[i] = arr22[i], arr11[i]

    Pc = random.choices([0, 1], weights = [1, 9])
    if Pc[0] == 1:
        sel_mut(arr11)
        initial_population.append(arr11)
    Pc = random.choices([0, 1], weights = [1, 9])
    if Pc[0] == 1:
        sel_mut(arr22)
        initial_population.append(arr22)

#Duo-point crossover
def duo_cross(arr1, arr2):
    global initial_population
    arr11 = arr1.copy()
    arr22 = arr2.copy()
    point = [randint(1, L-1), randint(1, L-1)]
    for i in range(0, L):
        if i < min(point) or i >= max(point):
            arr11[i], arr22[i] = arr22[i], arr11[i]

    Pc = random.choices([0, 1], weights = [1, 9])
    if Pc[0] == 1:
        sel_mut(arr11)
        initial_population.append(arr11)
    Pc = random.choices([0, 1], weights = [1, 9])
    if Pc[0] == 1:
        sel_mut(arr22)
        initial_population.append(arr22)


#N-point crossower
def n_cross(arr1, arr2):
    global initial_population
    arr11 = arr1.copy()
    arr22 = arr2.copy()
    n = randint(3, L-1)
    #print(f"n = {n}")
    point = [x for x in range(1,n+1)]
    for i in range(0, n+1):
        for j in range(0, L):
            if i == 0:
                if j < point[i]:
                    arr11[j], arr22[j] = arr22[j], arr11[j]
            elif i == n and j > point[i-1]-1 and i%2 == 0:
                arr11[j], arr22[j] = arr22[j], arr11[j]
            elif i%2 == 0 and i != n:
                    if j > point[i-1]-1 and j < point[i]:
                        arr11[j], arr22[j] = arr22[j], arr11[j]

    Pc = random.choices([0, 1], weights = [1, 9])
    if Pc[0] == 1:
        sel_mut(arr11)
        initial_population.append(arr11)
    Pc = random.choices([0, 1], weights = [1, 9])
    if Pc[0] == 1:
        sel_mut(arr22)
        initial_population.append(arr22)
###################################### Crossover operators /|\

###################################### Mutation operators \|/
#Probability of mutation depending on uniformity
def uniform():
    global uniformity
    uniformity = 0
    arr1 = initial_population.copy()
    arr2 = [] * Popul
    for i in range(0, Popul):
        arr2.append(''.join(map(str, arr1[i])))
    arr1.clear()
    for i in range(0, Popul):
        arr1.append(int(arr2[i]))
    uniformity = Popul - len(set(arr1))
    #print(f"copies - {uniformity}")
    a = 0

#Choosing mutation
def sel_mut(arr):
    if mut == 1:
        gene_mutation(arr)
    elif mut == 2:
        saltation(arr)
    elif mut == 3:
        inversion(arr)
    elif mut == 4:
        translocation(arr)
    elif mut == 5:
        chrom_mutation(arr)

#Gene mutation
def gene_mutation(arr):
    #Pm = random.choices([0, 1], weights = [9, 1], k= 1)
    #Pm = random.choices([0, 1], weights = [1, uniformity], k= 1)
    Pm = random.choices([0, 1], weights = [Popul, uniformity], k= 1)
    if Pm[0] == 1:
        a = randint(0, L-1)
        if arr[a] == 1:
            arr[a] = 0
        else:
            arr[a] = 1

#Macromutation
def saltation(arr):
    #Pm = random.choices([0, 1], weights = [9, 1], k= 1)
    Pm = random.choices([0, 1], weights = [Popul, uniformity], k= 1)
    if Pm[0] == 1:
        point = [randint(1, L-1), randint(1, L-1)]
        for i in range(0, 2):
            if arr[point[i]] == 1:
                arr[point[i]] = 0
            else:
                arr[point[i]] = 1

def inversion(arr):
    #Pm = random.choices([0, 1], weights = [9, 1], k= 1)
    Pm = random.choices([0, 1], weights = [Popul, uniformity], k= 1)
    if Pm[0] == 1:
        point = [randint(1, L-1), randint(1, L-1)]
        for i in range(0, L):
            if i > min(point) or i <= max(point):
                if arr[i] == 1:
                    arr[i] = 0
                else:
                    arr[i] = 1

def translocation(arr):
    #Pm = random.choices([0, 1], weights = [9, 1], k= 1)
    Pm = random.choices([0, 1], weights = [Popul, uniformity], k= 1)
    if Pm[0] == 1:
        point = [randint(1, L-1), randint(1, L-1)]
        for i in range(0, L):
            if i < min(point) or i >= max(point):
                if arr[i] == 1:
                    arr[i] = 0
                else:
                    arr[i] = 1

#Chromosome mutation
def chrom_mutation(arr):
    #Pm = random.choices([0, 1], weights = [9, 1], k= 1)
    Pm = random.choices([0, 1], weights = [Popul, uniformity], k= 1)
    if Pm[0] == 1:
        for i in range(0, L):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
###################################### Mutation operators /|\

###################################### Strategy for the formation of the next generation \|/
#β - tournament 
def B():
    global initial_population
    B = []
    '''
    #Generation formation strategies G = 1
    for g in range(Popul, len(initial_population)):
        B.append(initial_population[g])
        #Replace probability
        ver = random.choices([x for x in range(0, len(B))], weights = [1/Popul for x in range(0, len(B))], k= Popul * 2)
    '''
    #Generation formation strategies G ∈ (0, 1)
    B = initial_population.copy()
    B_price = [0 for x in range(0, len(B))]
    B_weight = [0 for x in range(0, len(B))]
    decoder(B, B_price, B_weight, 1)
    initial_population.clear()
    ver = random.choices([x for x in range(0, len(B))], weights = [1/len(B) for x in range(0, len(B))], k= Popul * 2)
    j = 0
    for i in range(0, Popul):
        initial_population.append(B[B_price.index(max(B_price[ver[j]], B_price[ver[j+1]]))])
        j +=2
    B.clear()
    I = initial_population.copy()
    decision(I)
###################################### Strategy for the formation of the next generation /|\

################## Decision forming 
def decision(arr):
    global M
    arr[0] = [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    decoder(arr, initial_price, initial_weight, 0)
    temp = initial_price.index(max(initial_price))
    M.insert(0, [arr[temp], initial_price[temp], initial_weight[temp]])
    a = 0
################## Choosing operators
def sel():
    global init_popul, cross, mut, initial_population
    if init_popul == 0:
        while init_popul != 1 and init_popul != 2 and init_popul != 123 and init_popul != 12 and init_popul != 13 and init_popul != 23:
            print("Choose the method of forming the initial population, you can combine, you cannot select only 3.")
            print("Random - 1, Random with constraint control - 2, greedy algoritm - 3")
            init_popul = int(input())
            #print(init_popul)
            if init_popul != 1 and init_popul != 2 and init_popul != 123 and init_popul != 12 and init_popul != 13 and init_popul != 23:
                print("ERROR")

    if init_popul == 1:
        initial_population = [encoding() for x in range(0, Popul)]

    elif init_popul == 2:
        initial_population = [encoding_check() for x in range(0, Popul)]

    elif init_popul == 12:
        t = randint(1, Popul-1)
        initial_population = [encoding() for x in range(0, t)]
        for i in range(0, Popul - t):
            initial_population.append(encoding_check())

    elif init_popul == 13:
        initial_population = [encoding() for x in range(0, Popul-1)]
        initial_population.append(greedy_algorithm())

    elif init_popul == 23:
        initial_population = [encoding_check() for x in range(0, Popul-1)]
        initial_population.append(greedy_algorithm())

    elif init_popul == 123:  
        t = randint(1, Popul-2)
        initial_population = [encoding() for x in range(0, t)]
        for i in range(0, Popul - 1 - t):
            initial_population.append(encoding_check())
        initial_population.append(greedy_algorithm())

    if cross == 0:
        while cross != 1 and cross != 2 and cross != 3:
            print("Choose crossovers operators.")
            print("Single-point - 1, Duo-point - 2, n-point - 3")
            cross = int(input())
            #print(cross)
            if cross != 1 and cross != 2 and cross != 3:
                print("ERROR")

    if mut == 0:
        while mut != 1 and mut != 2 and mut != 3 and mut != 4 and mut != 5:
            print("Choose mutation operators.")
            print("Gene - 1, Macromutation: Saltation - 2, Inversion - 3, Translocation - 4 Chromosomal - 5")
            mut = int(input())
            #print(mut)
            if mut != 1 and mut != 2 and mut != 3 and mut != 4 and mut != 5:
                print("ERROR")

def main(val1, val2, val3):
    global init_popul, cross, mut
    init_popul = val1
    cross = val2
    mut = val3
    print(f"{init_popul}{cross}{mut}")
    sel()
    ii = 1
    while 0 < 1:
        uniform()
        #print(f"copies - {uniformity}")
        negative_mating()
        B()

        C = 5
        if len(M) > C:
            temp = 0
            for i in range(0, C):
                if M[i][1] == M[i+1][1]:
                    temp += 1

            if temp == C:
                print("Finish")
                print(f"{ii}) Encoding - {M[0][0]}    Price = {M[0][1]}    Weight = {M[0][2]}")
                break

        print(f"{ii}) Encoding - {M[0][0]}    Price = {M[0][1]}    Weight = {M[0][2]}")
        ii += 1
    return ii

if __name__ == "__main__":
    main(0, 0, 0)