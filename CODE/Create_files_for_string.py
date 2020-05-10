# This program create a TXT file for String Dataset after sorted by each algorithm
# and named each file as algorithm name
# All the files created in "..\FILES\STRING" path
############################################################################
def main(itemset,algo_name):
    import os

    directory_path = os.path.join(os.getcwd(), 'FILES\STRING')
    if not os.path.exists(directory_path):
                os.mkdir(directory_path)

    filename=str(algo_name) + ".txt"
    file_path = os.path.join(directory_path, filename)

    f = open(file_path, 'w')
    for i in itemset:
        f.write(i)
        f.write(' ')
    f.close()