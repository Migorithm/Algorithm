'''quick sort.
sort out a list without using sorted() function.
[9,7,5,11,12,2,14,3,10,6]
[1,2,4,4,3,2,3]
-> [1,2,2,3,3,4,4]
'''


def quick_sort(lst,pivot):
    #base case
    if len(lst) <=1:
        return lst
    pt = pivot #suppose pivot = 0
    right_index = len(lst)-1
    done = pt <= right_index #check if indices are crossed.

    while done == True : #
        if  pt == 0 and right_index == 0:
            break
        done = (pt <= right_index)
        if not done or pt == 0 and right_index == 0 :
            break
        if lst[pivot] >= lst[pt] and lst[pivot] > lst[1]: # lst[0]이 lst[1]보다 크거나 같은 상태에서
            pt +=1 # lst[0] vs lst[0] -> lst[1] -> [2]-> [3] ... when lst[pt] > lst[pivot], it stops.
        elif lst[pivot] < lst[right_index]: # pivot보다 크거나 같으면 +1
            right_index -=1

        else:
            done = (pt <= right_index)
            if not done :
                break
            a = lst[pt] # value storing
            lst[pt] = lst[right_index]
            lst[right_index] = a  # exchange!
            done = (pt <= right_index)

    piv = lst[pivot]
    lst[pivot] = lst[right_index]
    lst[right_index] = piv
    a = lst[:right_index]
    b = lst[right_index:]
    del b[0]
    return     quick_sort(a,0) + [piv] + quick_sort(b,0)

print(quick_sort([8,5,3,11,32,43,30,2],0))
