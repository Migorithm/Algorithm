#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    lst = sorted(citations,reverse=True)
    count = 0
    for i in range(len(lst)):
        if i+1 <= lst[i]:
            count +=1
    return count

""""h번" 이상 인용된 논문이 "h개" 이상이며, 나머지 논문들의 인용 횟수가 h회보다 작아야합니다.
문제상에 오류가 있다고 볼 수 있다. 

'이하'가 아닌 '미만' 이 되어야 한다. 
"""


citations = [3, 0, 6, 1, 5]
solution(citations)
