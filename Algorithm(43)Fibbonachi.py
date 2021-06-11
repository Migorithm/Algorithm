#https://programmers.co.kr/learn/courses/30/lessons/12945
import sys
sys.setrecursionlimit(10**7)

dictionary ={1:1, 2:1}
def solution(n):
    if n in dictionary:
        return dictionary[n] #해당 키가 이미 dict에 있다면, 그 결과를 리턴한다.(따라서 재귀함수를 더 많이 돌릴 필요가 없도록)
    else :
        output = (solution(n-1) + solution(n-2))%1234567
        dictionary[n] = output
        return (solution(n-1) + solution(n-2))%1234567

"""
the technique used above is often called memorization. 
"""