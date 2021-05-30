'''달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

input//
2
3
4

output//
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7

'''

#How can I put a turning point?
def snail(n):
    res=[]
    for i in range(1,n*n+1):
        if i <=n:
            res.append(i)


