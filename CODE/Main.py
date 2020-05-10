# This program wants to know from user that they want to calculate execution time of each algorithm
# for Integer/Numerical Dataset or String Dataset to go further
######################################################################################
def main():
    while(1):
        check=int(input("In which type of value you want to perform sorting?....\nPress 1 for 'Numerical values'\nPress 2 for 'String values'\n"))
        if check==1:
            import Main_Int
            break
        elif check==2:
            import Main_String
            break
        else:
            print("Wrong Input\nPlease try again...\n")

main()

