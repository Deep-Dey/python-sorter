import Merge_Sort

def Strand_Sort(input_list):
    output_list=list()
    
    while len(input_list) > 0:
        sub_list=[input_list.pop(0)]
        pos=0

        while pos<len(input_list):
            if input_list[pos]>sub_list[-1]:
                sub_list.append(input_list.pop(pos))
            else:
                pos+=1

        temp_list=output_list+sub_list  ## For calling the module
        output_list=Merge_Sort.merge(temp_list, output_list, sub_list) ## Module
        
    return output_list

def main(a):
    a=Strand_Sort(a)
    #print("The sorted list is:", a)