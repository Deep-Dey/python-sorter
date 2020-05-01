from time import time

import Brick_Sort
import Bubble_Sort
#import Bucket_Sort
import Comb_Sort
#import Counting_Sort
import Cycle_Sort
import Gnome_Sort
import Heap_Sort
import Insertion_Sort
import Intro_Sort
import Merge_Sort
#import Pigeonhole_Sort
import Quick_Sort
#import Radix_Sort
import Selection_Sort
import Stooge_Sort
import Strand_Sort
import Tree_Sort
import Dataset_String
import copy
import sys

sys.setrecursionlimit(10**6) 

algo=[
    Brick_Sort, Bubble_Sort, Comb_Sort,
    Cycle_Sort, Gnome_Sort, Heap_Sort,
    Insertion_Sort, Intro_Sort, Merge_Sort,
    Quick_Sort, Selection_Sort, Stooge_Sort,
    Strand_Sort, Tree_Sort
    ]

algo_name=[
    'Brick_Sort', 'Bubble_Sort', 'Comb_Sort',
    'Cycle_Sort', 'Gnome_Sort', 'Heap_Sort',
    'Insertion_Sort', 'Intro_Sort', 'Merge_Sort',
    'Quick_Sort', 'Selection_Sort', 'Stooge_Sort',
    'Strand_Sort', 'Tree_Sort'
    ]

time_set=dict()
n=int(input("How many words(less than 3000) you want to sort...."))
c=int(input("How many times you want to perform sorting...."))
check_for_stooge=input("Do you want to run 'Stooge Sort'....\nBecause it increases program execution time very high(y/n)?")
dataset=Dataset_String.main(n)
def main():
    for i in range(len(algo)):
        time_count=0
        if (check_for_stooge=='N' or check_for_stooge=='n') and algo_name[i]=='Stooge_Sort':
            pass
        else:
            for j in range(c):
                array=copy.deepcopy(dataset)
                init=time()
                arr=algo[i].main(array)
                time_count+=(time()-init)

            print("The Execution time of '",algo_name[i],"' for",c,"time is:",time_count)
            time_set[algo_name[i]]=time_count/c

    print()
    for key,value in sorted(time_set.items(),key=lambda item: item[1]):
        print("The avarage time taken by '",key,"' algorithm is: ",value)

    print()
    max_time = max(time_set, key=time_set.get)
    print("The Maximum time taken by '",max_time,"' algorithm=",time_set[max_time])
    min_time = min(time_set, key=time_set.get)
    print("The Minimum time taken by '",min_time,"' algorithm=",time_set[min_time])

main()