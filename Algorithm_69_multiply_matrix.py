def solution(arr1, arr2):
    #axb * cxd 의 경우, axd 사이즈가 만들어질 것이며
    #b와 c는 같아야 한다.
    if len(arr1[0]) != len(arr2):
        return None

    # strategy 1  -> 빈 매트릭스를 만든다.
    empty_matrix = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]

    #strategy 2  -> 해당 값을 채워넣는다.
    for i in range(len(empty_matrix)):  #rows
        for j in range(len(empty_matrix[0])): #cols
            sum = 0
            #arr1 row값 고정... col만 이동 ->    ex  0,0   0,1   0,2
            #arr2 col값 고정... row만 이동 ->    ex  0,0   1,0   2,0
            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]
            empty_matrix[i][j] = sum
    print(empty_matrix)
    return empty_matrix



def solution2(arr1,arr2):
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*arr2)] for X_row in arr1]
    print(answer)
    #here, unpacking asterisk has been used to rearrange arr2.
    #number of X_row will decide the number of row of the matrix.
    return answer






arr1 =[[1, 4], [3, 2], [4, 1]]
arr2=[[3, 3], [3, 3]]

solution(arr1,arr2)


arr3 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr4 =  [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

solution2(arr3,arr4)