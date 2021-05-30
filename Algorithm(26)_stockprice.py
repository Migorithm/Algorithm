'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은
기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices	            return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
'''



def solution(prices):
    answer =[]
    while len(prices) != 0:
        for i in range(1,len(prices)):
            if prices[0] >prices[i]:
                answer.append(i)
                del prices[0]
                break
        else:
            answer.append(len(prices)-1)
            del prices[0]
    return answer

def index(prices):
    for i in prices[1:]:
        if prices[0] > i:
            return prices.index(i)

def solution2(prices):
    answer = []
    while prices != []:
        if (index(prices)) is not None:
            answer.append(index(prices))
            del prices[0]
        else:
            answer.append(len(prices)-1)
            del prices[0]
    return answer


def solution3(prices):
    answer = []
    while prices != []:
        b = tuple(map(lambda x:x < prices[0],prices[1:]))
        if True in b:
            answer.append(b.index(True)+1)
            del prices[0]
        else:
            answer.append(len(prices)-1)
            del prices[0]
    return answer


def solution4(lst):
    answer = []
    for index, i in enumerate(lst, 1):
        for ind, j in enumerate(lst, 1):
            if i > j and index < ind:
                answer.append(ind - index)
                break
        else:
            answer.append(len(lst) - index)
    return answer

def solution5(prices):
    answer= []
    for i in range(len(prices)): #i itself will be an index
        for j in range(len(prices)):
            if prices[i] > prices[j] and j>i :
                answer.append(j-i)
                break
        else:
            answer.append(len(prices)-i-1)
    return answer

def solution6(prices):
    answer =[]
    for i in range(len(prices)):
        cnt = 0
        for j in prices[i+1:]: #j itself will be an index
            cnt +=1
            if prices[i] > j:
                answer.append(cnt)
                break
        else:
            answer.append(cnt)
    return answer

def solution7(prices):
    answer = []
    for index, i in enumerate(prices,1):
        for j in prices[index:]:
            if i > j:
                answer.append(prices[index:].index(j)+1)
                break
        else:
            answer.append(len(prices)-index)

    return answer

def solution8(prices):
    answer=[]
    index = 0
    while len(answer) != len(prices):
        cnt = index + 1
        while cnt <= len(prices) -1:
            if prices[index] > prices[cnt]:
                answer.append(cnt - index)
                index +=1
                break
            cnt+=1
        else:
            answer.append(cnt-index-1)
            index += 1
    return answer



print(solution8(([1, 2, 3, 2, 3])))

from functools import reduce
#b= (1,2,3,4,5)
#print(b.index(1))
#lst = [1,2,3,2,3]

#a = list(map(lambda x,y=lst[1] : lst.index(y)-lst.index(x) if y<x else len(lst[x:]),lst)) #y를 어떻게 specify하는가?
#print(a)



