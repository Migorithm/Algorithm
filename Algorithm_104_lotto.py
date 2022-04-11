#https://programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    answer =[]
    cnt =0
    for i in win_nums:
        if i in lottos:
            cnt +=1
            lottos.remove(i)
    answer.append(7- (cnt + lottos.count(0))) if cnt+lottos.count(0) >0 else answer.append(6)
    answer.append(7 - cnt) if cnt >= 2 else answer.append(6) 
    return answer

def solution(lottos:list,win_nums:list):
    cnt = 0
    alpha =0 
    win_nums.sort()
    for my_num in lottos:
        if my_num in win_nums:
            cnt +=1
        else:
            if my_num == 0:
                alpha+=1
    highest = 7-(cnt+alpha)
    lowest = 7-cnt
    if highest > 5:
        highest =6
    if lowest > 5:
        lowest = 6
    return [highest,lowest]

print(solution([1,2,3,4,5,6],[7,8,9,10,11,12]))
