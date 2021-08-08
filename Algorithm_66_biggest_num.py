#https://programmers.co.kr/learn/courses/30/lessons/42746

"""
앞의 숫자가 가장 큰것을 기준으로 정렬하여 붙이면 될 것으로 보인다.

1) 어떻게 정렬할 것인가? 람다를 이용, 스트링 변환 후 앞의 글자를 기준으로.
2) 그러나 만약 같은 값이 있다면? -> 흠.. 그럼 두번째, 세번째를 기준으로 정렬해주어야.

"""

from itertools import permutations ,groupby

def solution(numbers):
    lst = []
    for i in permutations(numbers,len(numbers)):
        lst.append(int("".join(map(str,i))))
        print(i)
    return str(max(lst))



def solution2(numbers):
    hash = {}
    answer = ""
    for i in numbers:
        if int(str(i)[0]) in hash:
            hash[int(str(i)[0])].append(str(i))
        else :
            hash[int(str(i)[0])] = [str(i)]
    for i in sorted(hash.keys(),reverse=True):
        if len(hash[i]) >1:
            order = []
            for i in permutations(hash[i],len(hash[i])):
                order.append(int("".join(i)))
            answer += str(max(order))
        else:
            answer+= str(hash[i][0])

    return answer



numbers= [6, 10, 2]
#6210
solution(numbers)

numbers2= [3, 30, 34, 5, 9]
#9534330
solution(numbers2)