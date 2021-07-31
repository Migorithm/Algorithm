#https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque
def solution(priorities, location):
    deq = deque()
    for i in range(len(priorities)):
        deq.append((priorities[i],i)) #몇번쨰있는지.

    biggest = max(deq, key=lambda x: x[0])
    order = 0
    while deq != deque([]):
        number_to_compare = biggest[0]

        #덱에서 가장 큰 수라면
        if deq[0][0]==biggest[0]:
            #해당 수가 location에 일치하는 수라면 끝.
            if deq[0][1] == location:
                return order +1
            #일치하지 않는 경우에는 그냥 제거.
            else:
                deq.popleft()
                order +=1
                biggest = max(deq, key=lambda x: x[0])
                continue
        else: #가장 큰 수가 아니라면 넣고 빼준다.
            num = deq.popleft()
            deq.append(num)
            #그러나 이때는 order를 붙이지 않는다.


priorities = [2, 1, 3, 2]
location =2

print(solution(priorities,location))
