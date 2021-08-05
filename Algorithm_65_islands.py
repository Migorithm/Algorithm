#https://programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    #n이 주어진 이유?  -> n개 만큼의 섬이 있으니까! 하나의 파라미터가 될 것.
    #costs[i][0] - costs[i][1] 이 이어진다..


    #연결성이 track되어야 한다.
    #연결성에 대한 체크가 필요하다.
    #결국 모든 섬들이 연결되어있다는 확인..
    #+ 가장 낮은 가격.
    #연결의 갯수는 n-1개가 될 것이다.

    #가격 낮은 것으로 정렬
    costs.sort(key=lambda x:x[2])
    island = []
    connection = []
    answer = 0
    for i,j,k in costs:
        connected = i,j
        if i in island and j in island:
            #이 경우 후보군이 3개. i -> j, i ->
            #근데 가격비교? 어차피 가격 오름차순인데? 가격비교가 아니라 연결성 검증.
            #i나 j와 연결된 놈들 중 물고물고물고 물어서... j나 i로 연결시켜줄 애들이 있을까? -> 없으면 추가.

            continue
        else:
            island.append(i)
            island.append(j)
            connection.append([i,j])
            answer += k
            if len(connection) == n-1:
                break


    return answer



#test cases
ns = [5,5,4,5,6,5,5]
costs = [[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]],[[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] ,
         [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] , [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] ,
         [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]],
         [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]],
         [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]],
         [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]]]
answers = [15,8,9,104,11,6,8,8]

for i,j,k in zip(ns,costs,answers):
    answer = solution(i,j)
    if answer == k:
        print("정답")
    else:
        print("리턴값 : ",answer)
        print("정답은 : ",k)
