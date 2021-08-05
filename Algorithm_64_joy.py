#https://programmers.co.kr/learn/courses/30/lessons/42860

import string

def solution(name):
    hash={}
    alpha = string.ascii_uppercase
    for i in range(len(alpha)):
        #넘버링 하여 딕셔너리에 보관한다.
        hash[alpha[i]]=i
    count = 0
    current="A"
    previous = "A"

    #case1 현재위치에서 주어진 위치로 가는 것이 가장 빠른 경우

    #case2 과거위치에서 주어진 위치로 가는 턴 +1 이 가장 빠른 경우
    #ex E에서 A로 가려는데 과거 위치가 B였던 경우. E->B->A 2턴 instead of E->D->C->B->A

    #case3 A에서 Z로, 혹은 Z에서 A로 이동후 가는 경우.
    #ex A에서 Y로 가려면, A->Z ->Y -> 2턴

    #solution -> 3개 케이스에 따른 턴을 전부 다 넣어서 min값을 추출하여 더한다.




name = "JEROEN"

solution(name)