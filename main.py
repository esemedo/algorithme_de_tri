from tri_a_bulle_opti import tri_a_bulle_opti
from tri_bulles_normal import tri_bulles
from tri_selection import tri_selection3
from tri_insertion import tri_insertion
import math
import random

algo_list = [tri_selection3, tri_insertion, tri_bulles, tri_a_bulle_opti]
def stat(min, max, step, nbr):
    #table_number = math.floor(((max-min)/step)+1)
    a = min
    table_list = []
    while (a <= max):
        intermediary_list = []
        for i in range (nbr):
            random_list = []
            for j in range (a):
                random_number = random.randint(1,1000)
                random_list.append((random_number))
            intermediary_list.append(random_list)
        a += step
        table_list.append(intermediary_list)
    for k in table_list:
        for m in algo_list:
            result = 0
            for l in k:
                result += m(l)
            print(m)
            print({len(l), (result / len(k))})
    #print(table_number)
    #print(table_list)

stat(10, 20, 5, 2)
