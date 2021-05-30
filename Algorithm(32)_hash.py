import sys
from collections import defaultdict

N = sorted(map(int,sys.stdin.readline().split())) #turn into list.
M = map(int,sys.stdin.readline().split())

n_dic = defaultdict(int)
for i in N:
    n_dic[i] +=1

print(' '.join([str(n_dic[m]) for m in M]))











'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

3 0 0 1 2 0 0 2 
'''