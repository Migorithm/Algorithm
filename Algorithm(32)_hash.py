import sys
from collections import defaultdict
sys.stdin.readline()
N = sorted(map(int,sys.stdin.readline().split())) #turn into list.
sys.stdin.readline().split()
M = map(int,sys.stdin.readline().split())

n_dic = defaultdict(int)
for i in N:
    n_dic[i] +=1

print(' '.join([str(n_dic[m]) for m in M]))











