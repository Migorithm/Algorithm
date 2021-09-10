from PIL import Image
image = Image.open('keys/img.png')
image.show()

vertexList = ["0","1","2","3","4","5","6"]
edgeList = [(0,1),(0,2),(1,0),(1,3),(2,0),(2,4),(2,5),(3,1),(4,2),(4,6),(5,2),(6,4)]


def dfs(vertextList:list,edgeList:list):
    adjacentList=[[] for vertex in vertextList]

    for edge in edgeList:
        adjacentList[edge[0]].append(edge[1])

    stack = [2]
    visitedVertex = []
    while stack:
        current = stack.pop()
        for neighbor in adjacentList[current]: #0번부터
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex


print(dfs(vertexList,edgeList))