# python-sorter

A **Python** package to apply multiple type of sorting algorithm on your data and also compare which sorting is fastes on your data. Visit the page for <a href="https://pypi.org/project/python-sorter/">python-sorter</a>

## Installation
    
    pip install python-sorter 

## Usage

    import data_sorter
    
    arr = [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
    
    ####### To perform sorting #########
    arr = data_sorter.bubble_sort(arr)
    print(arr)

    ##### To compare execution time between different algos ######
    
    # apply all sorting technique
    result = data_sorter.get_comparison(arr)

    # specify which sorting algorithm to apply
    result = data_sorter.get_comparison(arr, ['bubble_sort'])

    ##### To plot execution time between different algos ######

    # apply all sorting technique
    result = data_sorter.plot_comparison(arr)

    # specify which sorting algorithm to apply
    result = data_sorter.plot_comparison(arr, ['bubble_sort'])


# Available sorting algorithms

    - brick_sort
    - bubble_sort
    - bucket_sort (only for float data)
    - comb_sort
    - counting_sort (only for integer data)
    - cycle_sort
    - gnome_sort
    - heap_sort
    - insertion_sort
    - intro_sort
    - merge_sort
    - pigeonhole_sort (only for integer data)
    - quick_sort
    - radix_sort
    - selection_sort
    - stooge_sort
    - strand_sort
    - tree_sort