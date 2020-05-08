def main(n):  
    from bs4 import BeautifulSoup
    import requests
    import csv

    source = requests.get('https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words').text

    soup = BeautifulSoup(source, 'lxml')
    dataset=list()
    titles=soup.find('div', class_='field-item even')
    for data in titles.find_all('p'):
        dataset.append(data.text)

    data=dataset[1].split('\n\t')
    data.reverse()
    itemset=data[0:n]
    for i in range(len(itemset)):
        itemset[i]=itemset[i].lower()
    
#################################################### Write to a file    
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
