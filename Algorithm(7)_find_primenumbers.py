
from itertools import permutations
from functools import reduce

def solution(numbers):
    answer = 0
    candidate = []
    for j in range(1,len(numbers)+1):
        for i in permutations(numbers,j):
            b = reduce(lambda x,y:x+y if x != '0'else y,i) #조합수중 머리에 0이 오면 eval이 불가능 하므로. 
            candidate.append(eval(b))
    candidate = list(set(candidate)) # 세트화 시켜서 중복수를 제거해준다.
    for i in candidate:
        if i >1 and i%2 == 1 and i != 2:
            for j in range(2,i): #1과 자신을 제외한 숫자로 나눠지지 않아야.
                if i%j ==0: #따라서 나눠지면 더 볼 필요 없음
                    break
            else: #안나눠지는 경우,
                answer +=1
        elif i == 2: #i가 2인경우는 특별케이스로 넣어준다. 짝수중 유일한 소수
            answer+=1
        else:
            continue
    return answer

print(solution('011'))
