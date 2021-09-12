def paperCuttings(textLength, starting, ending):
    lst=[]
    for i,j in zip(starting,ending):
        lst.append(range(i,j+1))
    lst = list(set(lst))
    cnt= 0
    print(lst)
    while lst:
        current = lst.pop()
        for i in lst:
            if not set(current).intersection(set(i)):
                cnt+=1
    return cnt

def paperCuttings2(textLength, starting, ending):
    lst=[]
    for i,j in zip(starting,ending):
        lst.append((i,j+1))
    lst = list(set(lst))
    cnt= 0
    while lst:
        current = lst.pop()
        for i in lst:
            comparator = range(i[0],i[1])
            if current[0] not in comparator and current[1] not in comparator:
                cnt+=1
    return cnt
print(paperCuttings2(10,[1,1,6,7],[5,3,8,10]))