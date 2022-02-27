#https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
from collections import defaultdict
from itertools import combinations 
from functools import reduce

def solution(clothes):
    dic = defaultdict(int)
    for _,kind in clothes: 
        dic[kind] +=1
    result = sum(dic.values())
    if len(dic) == result:
        return 2**len(dic) -1 
    if len(dic) >1:
        for i in range(2,len(dic)+1):
            for j in combinations(dic.keys(),i):
                result+=reduce(lambda x,y: x*y ,tuple(map(lambda x : dic[x],j)))
    return result  
        

clothes = \
    [["yellowhat", "headgear"], 
     ["bluesunglasses", "eyewear"], 
     ["green_turban", "headgear"],
     ["jean","pants"],
     ["blackjean","pants"]
     
     ]
#5 + 5 + 5 + 2  = 17 


solution(clothes)


#Model 


def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes]) #same as defaultdict(int)
    print(cnt)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1  
            # reduce takes first element as initializer by default.
            # to replace it with 1, 1 was given as the last argument.
    return answer

clothes = \
    [["yellowhat", "headgear"], 
     ["bluesunglasses", "eyewear"], 
     ["green_turban", "headgear"],
     ["jean","pants"],
     ["blackjean","pants"]
     
     ]
solution(clothes)