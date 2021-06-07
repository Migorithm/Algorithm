
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
from functools import reduce


def DSF(ins):
    l,n,p = map(int,ins)
    #ways = deque(tuple(map(int,sys.stdin.readline().replace('\n','').split())) for i in range(n))
    ways = deque([(4,2),(7,2),(4,3),(8,4),(1,7),(7,9)])
    road_taken= [p]
    point =[p]
    while len(point) < min(l,n+1) and ways != deque([]):
        if road_taken ==[]:
            break
        line = [i for i in ways if p in i]
        if line == []:
            try:
                road_taken.pop()  #backtracking!
                p = road_taken[-1]
                continue
            except:
                break
        path = reduce(lambda x,y: x if sum(x) < sum(y) else y, line)
        ways.remove(path)
        valid = list(filter(lambda x:x not in point,path))
        if valid != []:
           point.append(valid[0])
           road_taken.append(valid[0])
           p = point[-1]

    for i in point:
        if i == point[-1]:
            print(i)
        else:
            print(i, end=' ')


#DSF(sys.stdin.readline().split())
DSF(("7" ,"6", "2"))

