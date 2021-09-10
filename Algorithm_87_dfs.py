# from PIL import Image
# image = Image.open('keys/img.png')
# image.show()


#condition : left first.

from collections import deque

vertexList = ["0","1","2","3,","4","5","6"]
edgeList = [(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]


def dfs(vertexList,edgeList,top,target):
    adjacentList= [[] for i in vertexList]
    for edge in edgeList:
        adjacentList[edge[0]].append(edge[1])
    #ready.
    deq = deque()
    deq.appendleft(top)
    visited =[]

    while deq:
        current = deq.pop()
        for neibour in adjacentList[current][::-1]: #Check current
            if neibour not in visited:
                deq.append(neibour) #hitting point.
        visited.append(current)
        if visited[-1] == target:
            return len(visited)
    print(visited)

dfs(vertexList,edgeList,2,4)

