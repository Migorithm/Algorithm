#https://programmers.co.kr/learn/courses/30/lessons/43162



def solution(n, computers):
    lst=[]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if computers[i][i] != computers[j][j] and computers[i][j] ==1 :
                lst.append((i,j))
    print(lst)

    answer = 0
    return answer

computers= [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

#(0,1),(1,0)
print(solution(3,computers))