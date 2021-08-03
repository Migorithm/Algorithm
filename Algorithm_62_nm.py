#https://www.acmicpc.net/problem/15650

#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을
#모두 구하는 프로그램을 작성하시오.

#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#고른 수열은 오름차순이어야 한다.

#permutation은 순서를 고려, 따라서 순서가 바뀌었지만 중복합이 나올 수 있다
#combination은 어떤 조합인지만 고려.
from itertools import combinations
import sys
N,M = map(int,sys.stdin.readline().split())

for i in combinations(range(1,N+1),M):
    print(" ".join(map(str,i)))


