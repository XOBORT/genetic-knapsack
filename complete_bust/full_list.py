from data import individual_size

def length():
    length = int(individual_size() * "1", 2)
    return length

def full_list():
    binary = []
    full_list = []
    for i in range(1, length()+1):
       binary.append(bin(i).replace("0b", "", 1))
       #print(binary[i-1])
    for j in range(len(binary)):
        if len(binary[j]) < individual_size():
            binary[j] = (individual_size()-len(binary[j]))*"0" + binary[j]
        binary[j] =  list(binary[j])
        full_list.append(list(map(int, binary[j])))
    return full_list