import pandas as pd
import numpy as np
from collections import deque

def solution(n, computers):
    df = pd.DataFrame(computers)
    clusters=[]
    for i in range(n):
        cluster = list(df.loc[i][df.loc[i]==1].index) #-> cluster
        #a= df.loc[i][df.loc[i]==1].index
        clusters.append(cluster)
    print(clusters)

    #여기서 겹침이 없는 애들만 모아준다. 어떻게? 점진적 병합!
    deq = deque()
    while len(deq) != n:
        a= clusters.pop()
        print(a)
        for i in a:
            print(i)
            lst =list(filter(lambda x:i in x,clusters))
            #lst의 길이가 2 이상일 수..... 평탄화 시킨다.
            print(lst)

        break




#
# df = pd.DataFrame([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# print(df) #return2
#
# df2 = pd.DataFrame([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
#
# print(df2) #return 1


test1 = [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]

solution(len(test1),test1)

