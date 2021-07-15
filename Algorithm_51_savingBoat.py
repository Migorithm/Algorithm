#https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3
#구명보트 개수의 최솟값



def solution(people, limit):
    cnt = 0
    people.sort(reverse=True)
    while True:
        scaler = limit
        while scaler >= 0 :
            scaler -= people.pop()
            nearest = sorted(filter(lambda i: scaler - i >= 0,people))
            if nearest !=[]:
                if (scaler - nearest[-1]>=0 ):
                    scaler -= nearest[-1] #second
                    people.remove(nearest[-1])
                    break
                else:
                    break
            else:
                break
        cnt +=1
        if people == []:
            break
    return cnt



from collections import deque
def solution2(people, limit):
    people.sort()
    deq = deque(people)
    cnt = 0
    while True:
        scaler = limit
        scaler -= deq.pop() #substract the biggest one first
        if deq != deque():
            if (scaler - deq[0]) >=0:
                scaler -= deq.popleft()
                cnt+=1
                if deq == deque():
                    break
                continue
            cnt+=1
            if deq == deque():
                break
        else:
            cnt+=1
            break
    return cnt

