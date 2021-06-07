"""
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
7
6
1 2
2 3
1 5
5 2
5 6
4 7

4
"""
import sys
from functools import reduce
from collections import deque

def warm(n,r):
    n , r = map(int,(n, r))
    cont = [tuple(map(int,sys.stdin.readline().split())) for i in range(r)]
    road_taken = deque()
    road_taken.append(1)
    point=[1]
    check_point = 1
    while 1:
        coms = list(filter(lambda x : check_point in x,cont))
        if coms ==[]:
            try :
                check_point = road_taken.pop()
                continue
            except:
                break
        p = reduce(lambda x,y :x if sum(x)<sum(y) else y,coms)
        check_point = p[0] if p[0] not in point else p[1]
        cont.remove(p)
        if check_point in point:
            continue
        else:
            point.append(check_point)
            road_taken.append(check_point)
    print(len(point)-1)

warm(sys.stdin.readline() ,sys.stdin.readline())