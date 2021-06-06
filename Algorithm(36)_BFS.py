
'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

4 5 1  N 정점의 갯수 , M 간선의 갯수, V 정점의 번호
1 2
1 3
1 4
2 4
3 4

1 2 4 3  -- DFS
1 2 3 4  -- BFS


5 5 3
5 4
5 2
1 2
3 4
3 1

3 1 2 5 4
3 1 4 2 5
'''

import sys
from collections import deque




def BSF(ins):
    l, n, p = map(int, ins)
    ways = deque(tuple(map(int, sys.stdin.readline().replace('\n', '').split())) for i in range(n))
    road_taken= deque()
    point =[p]
    while len(point) < min(l, n + 1) and ways != deque([]):
        line = list(filter(lambda x: p in x ,ways))
        if line != []:
            for i in line:
                ways.remove(i)
            order = sorted(map(lambda x: (x[0],x[1]) if x[0] ==p else (x[1],x[0]),line),key=lambda key :key[1])
            for i, j in order:
                point.append(j)
                road_taken.appendleft(j)
            p = road_taken.pop()
        else:
            try :
                p = road_taken.pop()
            except:
                print("No road")
                break
    for i in point:
        if i == point[-1]:
            print(i)
        else:
            print(i ,end= ' ')



BSF(sys.stdin.readline().split())
