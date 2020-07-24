import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def main(time_set, flag, c):
    df_total_time = pd.DataFrame(data=time_set, columns=['Algorithm Name', 'Execution Time'])
    print(df_total_time)
    if flag == 1:
        title = 'Execution time of algorithms for ' + str(c) + ' times'
    else:
        title = 'Average Execution time of algorithms'

    choice = input("Do you want to see the details as Bar Chart......(y/n)")
    if choice == 'y':
        sns.set_style("ticks")
        plt.figure(figsize=(30, 20))
        plt.barh(df_total_time['Algorithm Name'], df_total_time['Execution Time'], align='center', color='blue')
        plt.xlabel('Execution Time(ms)', fontsize=15)
        plt.ylabel('Algorithm Names', fontsize=15)
        plt.xticks(fontsize=10, rotation='vertical')
        plt.yticks(fontsize=10)
        plt.title(title, fontsize=15)

        for index, value in enumerate(df_total_time['Execution Time']):
            plt.text(value, index, str(value), fontsize=10)
        plt.show()

    if flag == 1:
        print('\n...Minimum Execution time taken for ' + str(c) + ' times execution...')
        print(df_total_time[df_total_time['Execution Time']==df_total_time['Execution Time'].min()])
        print('\n...Maximum Execution time taken for ' + str(c) + ' times execution...')
        print(df_total_time[df_total_time['Execution Time']==df_total_time['Execution Time'].max()])
    else:
        print('\n...Minimum Execution time taken for single time(or Average) execution...')
        print(df_total_time[df_total_time['Execution Time']==df_total_time['Execution Time'].min()])
        print('\n...Maximum Execution time taken for single time(or Average) execution...')
        print(df_total_time[df_total_time['Execution Time']==df_total_time['Execution Time'].max()])
