"""
예제 1: abcde의 해시 값은 1 × 310 + 2 × 311 + 3 × 312 + 4 × 313 + 5 × 314 = 1 + 62 + 2883 + 119164 + 4617605 = 4739715

예제 2: zzz의 해시 값은 26 × 310 + 26 × 311 + 26 × 312 = 26 + 806 + 24986 = 25818이다

"""

import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline()[:-1]
answer = 0
m = 1234567891

for i in range(len(b)):
    r = (31**i)
    if (r >m):
        r = r%m #나머지만 취한다.
    answer += (ord(b[i])-96) *r
    if answer >m :
        answer = answer %m #나머지만 취한다.
print(answer)
