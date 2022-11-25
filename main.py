from tri_a_bulle_opti import tri_a_bulle_opti
from tri_bulles_normal import tri_bulles
from tri_selection import tri_selection
from tri_insertion import tri_insertion
import random

algo_list = [tri_selection, tri_insertion, tri_bulles, tri_a_bulle_opti]
result_file = "result.txt"
def stat(min, max, step, nbr):
    with open(result_file, 'w') as f:
        f.write("")
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
    for m in algo_list:
        with open(result_file, 'a') as f:
            f.write(m.__name__ + '\n')
            print(m.__name__)
            for k in table_list:
                result = 0
                for l in k:
                    result += m(l)
                moyenne = len(l), (result / len(k))
                print(moyenne)
                f.write(f"{moyenne}\n")

stat(12, 122, 7, 100)