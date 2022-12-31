import matplotlib.pyplot as plt
from pprint import pprint
from typing import Optional
import time
import sys

from data_sorter.algos import *

sys.setrecursionlimit(10 ** 6)

g_algo_name: list = [
    'brick_sort',
    'bubble_sort',
    'bucket_sort',
    'comb_sort',
    'counting_sort',
    'cycle_sort',
    'gnome_sort',
    'heap_sort',
    'insertion_sort',
    'intro_sort',
    'merge_sort',
    'pigeonhole_sort',
    'quick_sort',
    'radix_sort',
    'selection_sort',
    'stooge_sort',
    'strand_sort',
    'tree_sort'
]

def get_comparison(arr: list, algo_names: Optional[list]=[], set_NA: Optional[any]='NA') -> dict:
    '''
    This function return execution time for sorting the given dataset with provided algorithms.\n
    `arr` take the input as list for sorting\n
    `algo_names` take name of the algorithms want to perform. Keep it blank to test on all available algorithms.\n
    If algorithm perform sorthing it will return execution time in `Seconds`\n
    Otherwise it will return `NA`

    '''
    if not algo_names:
        algo_names = g_algo_name
    result: dict = {}
    for algo_name in algo_names:
        try:
            start_time = time.time()
            result[algo_name] = getattr(sys.modules[__name__], algo_name)(arr)
            result[algo_name] = time.time() - start_time
        except Exception as e:
            result[algo_name] = set_NA
    return result

def plot_comparison(arr: list, algo_names: Optional[list]=[]):
    '''
    This function return execution time for sorting the given dataset with provided algorithms.\n
    `arr` take the input as list for sorting\n
    `algo_names` take name of the algorithms want to perform. Keep it blank to test on all available algorithms.\n
    It plots the result as bar chart. Here `-ve` value means sorting not possible
    '''
    result: dict = get_comparison(arr, algo_names, -1.0)
    
    algo_names = list(result.keys())
    exec_time = list(result.values())
    pprint(result)

    plt.bar(range(len(result)), exec_time, tick_label=algo_names)
    plt.axhline(y = 0, color = 'r', linestyle = '-')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()