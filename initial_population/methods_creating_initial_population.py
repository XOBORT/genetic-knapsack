from random import randint
from data import individual_size, pack, max_weight


def rand_encoding():
    codir = [randint(0, 1) for x in range(individual_size())]
    return codir

def rand_encoding_check():
    codir = [randint(0, 1) for x in range(individual_size())]
    weight = 0
    for i in range(0, individual_size()):
        if int(codir[i]) == 1:
            weight += pack()[i][2]
    if weight <= max_weight():
        return codir
    else:
        return rand_encoding_check()

def greedy_encoding():
    codir = [] * individual_size()
    codir.clear()
    codir = [0 for i in range(0, individual_size())]
    weight = 0
    temp_pack = pack().copy()
    temp_pack.sort(key=lambda x: x[2])
    temp_pack.sort(key=lambda x: x[1], reverse=True)
    for i in range(0, individual_size()):
        if weight <= max_weight():
            temp_weight = weight + temp_pack[i][2]
            if temp_weight > max_weight():
                continue
            else:
                codir[temp_pack[i][0]-1] = 1
                weight += temp_pack[i][2]
    temp_pack.sort(key=lambda x: x[0])
    return codir