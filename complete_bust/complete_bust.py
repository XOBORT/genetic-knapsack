from data import max_weight, individual_size, pack
from complete_bust.full_list import full_list

def complete_bust():
    decision = full_list().copy()
    popul_price = [0 for i in range(len(decision))]
    popul_weight = [0 for i in range(len(decision))]
    for i in range(0, len(decision)):
        for j in range(0, individual_size()):
            if decision[i][j] == 1:
                popul_price[i] += pack()[j][1]
                popul_weight[i] += pack()[j][2]
    return popul_price, popul_weight, decision
    
def cutting_off_excess():
    temp_Arr = complete_bust()
    popul_price = temp_Arr[0]
    popul_weight = temp_Arr[1]
    decision = temp_Arr[2]
    for i in range(0, len(decision)):
        if popul_weight[i] > max_weight():
            popul_price[i] = 0
            popul_weight[i] = 0
    while True:
        return max(popul_price)