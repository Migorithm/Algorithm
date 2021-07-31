#https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    lst = []
    for i in s:
        if len(lst)>1:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()
        lst.append(i)
    else:
        if len(lst)>1:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()
    #last check
    print(lst)

    #애초에 홀수였다면 다 짝지어 질 수 없다. 따라서 조건식은 len(lst)>=1 이 되어야 한다.
    return 0 if len(lst) >=1 else 1

s = 'bggggbgegeegeg'

print(solution(s))