# This program perform all kinds of sortings on String type Dataset as many time as user want(n) and
# show total time to execute each algorithm for n times and single time execution of each algorithm
############################################################################################
from time import time

import Brick_Sort
import Bubble_Sort
import Comb_Sort
import Cycle_Sort
import Gnome_Sort
import Heap_Sort
import Insertion_Sort
import Intro_Sort
import Merge_Sort
import Quick_Sort
import Selection_Sort
import Stooge_Sort
import Strand_Sort
import Tree_Sort
import Dataset_String
import Create_files_for_string
import copy
import sys
import Column_Chart

sys.setrecursionlimit(10 ** 6)

algo = [
    Brick_Sort, Bubble_Sort, Comb_Sort,
    Cycle_Sort, Gnome_Sort, Heap_Sort,
    Insertion_Sort, Intro_Sort, Merge_Sort,
    Quick_Sort, Selection_Sort, Stooge_Sort,
    Strand_Sort, Tree_Sort
]

algo_name = [
    'Brick_Sort', 'Bubble_Sort', 'Comb_Sort',
    'Cycle_Sort', 'Gnome_Sort', 'Heap_Sort',
    'Insertion_Sort', 'Intro_Sort', 'Merge_Sort',
    'Quick_Sort', 'Selection_Sort', 'Stooge_Sort',
    'Strand_Sort', 'Tree_Sort'
]

time_set = list()
total_time_set = list()
n = int(input("How many words(less than 3000) you want to sort...."))
c = int(input("How many times you want to perform sorting...."))
check_for_stooge = input("Do you want to run 'Stooge Sort'...."
                         "\nBecause it increases program execution time very high(""y/n)?")
dataset = Dataset_String.main(n)


def main():
    for i in range(len(algo)):
        time_count = 0
        if (check_for_stooge == 'N' or check_for_stooge == 'n') and algo_name[i] == 'Stooge_Sort':
            pass
        else:
            for j in range(c):
                array = copy.deepcopy(dataset)
                init = time()
                arr = algo[i].main(array)
                time_count += (time() - init)

            Create_files_for_string.main(arr, algo_name[i])
            total_time_set.append([algo_name[i], time_count])
            time_set.append([algo_name[i], time_count / c])

    flag = 1
    print("\n...The Execution time of each algorithm for", c, "times...\n")
    Column_Chart.main(total_time_set, flag, c)

    flag = 0
    print("\n...The Average Execution time of each algorithm is...\n")
    Column_Chart.main(time_set, flag, c)

main()
