#https://programmers.co.kr/learn/courses/30/lessons/42860

import string

def solution(name):
    hash={}
    alpha = string.ascii_uppercase
    for i in range(len(alpha)):
        #넘버링 하여 딕셔너리에 보관한다.
        hash[alpha[i]]=i
    count = 0
    current = 'A'

    for i in name:
    #case1 현재위치("A")에서 주어진 위치로 가는 것이 가장 빠른 경우 (직접)
        case1 = hash[i]

    #case3 Z로 가서 가는 경우.
        #case3 = abs(hash[current] - hash['A']) +1 + abs(hash['Z'] - hash[i])
        case2 = 1 + hash['Z'] -hash[i]

    #마지막 케이스로 가서 이동하는 경우.
        route = min([case1, case2])

        if hash[i] >

        if i =="A":
            pass
        else:
            count += route +1
    #solution -> 3개 케이스에 따른 턴을 전부 다 넣어서 min값을 추출하여 더한다.

    return count -1



name = "JEROEN"
name2= "ZAAAZZZZZZZ"

solution(name2)

# J (9) -> E(5)