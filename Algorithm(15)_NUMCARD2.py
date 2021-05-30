'''
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
이 수는 공백으로 구분되어져 있다.
이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

3 0 0 1 2 0 0 2

'''

import sys
a =sys.stdin.readline()
N = sys.stdin.readline().strip().split()
c = sys.stdin.readline()
M = sys.stdin.readline().split()
hashmap = {}

for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1
print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))

