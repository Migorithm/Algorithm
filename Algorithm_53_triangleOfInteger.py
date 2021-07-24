#https://programmers.co.kr/learn/courses/30/lessons/43105

#[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# 30

from collections import deque
def solution(triangle):
    #모든경로 탐색 후 최대값인 것을 고를 것
    #1. 탐색의 마지막 depth을 정해주어야.   **
    #2. 탐색제한조건 [0][0] -> [1][0] , [1][1] 을 걸어주어야. **
    #3. 재귀적? -> yes. maybe backtracking.

    #basecase
    if len(triangle) ==0:
        return 0
    answer = []

    lst=[triangle[0][0]]
    for i in range(1,len(triangle)):
        innerlst=[]
        this_number_plus1=0
        this_number_plus2=0

        for j in range(0,len(triangle[i])-1): #0~~

            this_number_plus1 = triangle[i][j]
            this_number_plus2 = triangle[i][j+1] #out of index.
            innerlst.append(this_number_plus1)
            innerlst.append(this_number_plus2)
        for k in range(2**i-1):
            inte = len(lst)
            lst.append(lst[k] + this_number_plus1)
            lst.append(lst[k] + this_number_plus2)
            if k == inte:

                break




    print(answer)
    return
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])


"""
[

0[7], 
1[3, 8], 
2[8, 1, 0], 
3[2, 7, 4, 4], 
4[4, 5, 2, 6, 5]

]

"""