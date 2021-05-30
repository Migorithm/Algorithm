import sys

def binary_search(sequence,item):
    begin_index =0
    end_index = len(sequence) - 1
    while begin_index <= end_index:
        middle = begin_index+ (end_index - begin_index)//2
        middle_value = sequence[middle]
        if middle_value == item:
            return middle # point
        elif item < middle_value:
            end_index = middle -1
        else:
            begin_index = middle+1
    return None

