#https://www.acmicpc.net/problem/10872
"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
"""

import sys

def factorial(n):
    #base case
    if n <=1:
        return 1
    return factorial(n-1) * n

print(factorial(int(sys.stdin.readline())))

