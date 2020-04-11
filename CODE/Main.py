from time import time

import Brick_Sort
import Bubble_Sort
import Bucket_Sort
import Comb_Sort
import Counting_Sort
import Cycle_Sort
import Gnome_Sort
import Heap_Sort
import Insertion_Sort
import Intro_Sort
import Merge_Sort
import Pigeonhole_Sort
import Quick_Sort
import Radix_Sort
import Selection_Sort
import Stooge_Sort
import Strand_Sort
import Tree_Sort
import Dataset

algo=[
    Brick_Sort, Bubble_Sort, Bucket_Sort,
    Comb_Sort, Counting_Sort, Cycle_Sort, 
    Gnome_Sort, Heap_Sort, Insertion_Sort,
    Intro_Sort, Merge_Sort, Pigeonhole_Sort,
    Quick_Sort, Radix_Sort, Selection_Sort,
    Stooge_Sort, Strand_Sort, Tree_Sort
    ]

algo_name=[
    'Brick_Sort', 'Bubble_Sort', 'Bucket_Sort',
    'Comb_Sort', 'Counting_Sort', 'Cycle_Sort', 
    'Gnome_Sort', 'Heap_Sort', 'Insertion_Sort',
    'Intro_Sort', 'Merge_Sort', 'Pigeonhole_Sort',
    'Quick_Sort', 'Radix_Sort', 'Selection_Sort',
    'Stooge_Sort', 'Strand_Sort', 'Tree_Sort'
    ]

time_set=dict()

def main():
    
    for i in range(len(algo)):
        array=Dataset.main()
        init=time()
        algo[i].main(array)
        time_set[algo_name[i]]=time()-init
        print("The Execution time of '",algo_name[i],"' is:",time()-init)
        print()

    max_time = max(time_set, key=time_set.get)
    print("The Maximum time taken by '",max_time,"' algorithm=",time_set[max_time])
    min_time = min(time_set, key=time_set.get)
    print("The Minimum time taken by '",min_time,"' algorithm=",time_set[max_time])
main()

