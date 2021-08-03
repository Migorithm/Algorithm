#https://programmers.co.kr/learn/courses/30/lessons/42626

from collections import deque
def solution(scoville, K):
    #K가 scoville의 최소값보다 작으면 계산할 필요가 없다.
    if K <= min(scoville):
        return 0

    #K보다 작은 애들만 걸러준다.
    deq = deque(sorted(filter(lambda x : x<K,scoville)))

    #카운트를 위한 변수.
    cnt = 0
    while len(deq) > 1:
        a = deq.popleft()
        b = deq.popleft()
        c = a+ b*2
        cnt +=1
        if c <K:
            deq.append(c)
            deq = deque(sorted(deq))

#모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
    #어떤 경우인가? -> 1개만 남았고 그 값이 K보다 작은 경우.
    else:
        if len(deq) == 1:
            return -1
        return cnt




scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville,K))
