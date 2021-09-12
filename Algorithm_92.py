def getTheGroups(n, queryType, students1, students2) ->list[int]:
    # Write your code here
    answer = []
    group= []
    for i,j,k in zip(queryType,students1,students2):
        if i != "Total":
            group.append((j-1,k-1))
        else:
            # DFS!
            edgeList = []
            for node1,node2 in group:
                edgeList.append((node1,node2))
                edgeList.append((node2,node1))
            adjacentList = [[] for vertex in range(n)]

            for edge in edgeList:
                adjacentList[edge[0]].append(edge[1])

            stack = [j-1]
            visitedVertex = []
            while stack:
                current = stack.pop()
                for neighbor in adjacentList[current]:
                    if not neighbor in visitedVertex:
                        stack.append(neighbor)
                visitedVertex.append(current)
            size_of_group1 = len(visitedVertex)

            stack = [k-1]
            visitedVertex = []
            while stack:
                current_node = stack.pop()

                for neighbor in adjacentList[current_node]:
                    if not neighbor in visitedVertex:
                        stack.append(neighbor)
                visitedVertex.append(current_node)
            size_of_group2 = len(visitedVertex)
            answer.append(size_of_group1+size_of_group2)
            group=[] #initialization
    return answer






queryType=["Total"]
student1 = [1]
student2 = [2]
getTheGroups(2,queryType,student1,student2)
#return [3]

"""
#1 -> query type    friends or total

#2,3 -> students 1, students 2  -> ID

"""

