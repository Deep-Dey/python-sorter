# This program took String values from 'https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words'
# to perform sorting where number of Strings is given by the user 
# and store them into a TXT file named "Unsorted_Strings.txt"
#####################################################################################
def main(n):  
    from bs4 import BeautifulSoup
    import requests
    import csv

    dataset=list()
    with open('String_Dataset.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            dataset.append(row[0])

    dataset.reverse()
    itemset=dataset[0:n]
    for i in range(len(itemset)):
        itemset[i]=itemset[i].lower()
    
#################################################### Write to a TXT file in "..\FILES\" path   
    import os

    directory_path = os.path.join(os.getcwd(), 'FILES')
    if not os.path.exists(directory_path):
                os.mkdir(directory_path)

    file_path = os.path.join(directory_path, 'Unsorted_Strings.txt')

    f = open(file_path, 'w')
    for i in itemset:
        f.write(i)
        f.write(' ')
    f.close()

    return itemset
