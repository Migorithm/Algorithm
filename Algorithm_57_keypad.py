#https://programmers.co.kr/learn/courses/30/lessons/67256
'''
맨처음 왼손은 * 키패드에
오른손은 # 키패드 위치에서 시작

왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.

가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는
두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.

--만약 두 엄지손가락의 거리가 같다면,
오른손잡이는 오른손 엄지손가락,
왼손잡이는 왼손 엄지손가락을 사용합니다.
'''


def solution(numbers, hand):
    answer = ""
    hash = {1:("L",[0,0]),4:("L",[1,0]),7:("L",[2,0]),3:("R",[0,2]),6:("R",[1,2]),9:("R",[2,2])}
    hash2 = {2: [0,1], 5: [1,1], 8: [2,1], 0: [3,1]}
    index= 0

    left = [3,0]
    right = [3,2]
    while len(answer) != len(numbers):
        cur = numbers[index]
        if cur in hash: #현재 밸류가 L 혹은 R에 전속되는 숫자인지 판별.
            answer += hash[cur][0] #L 혹은 R에 속하는 값이 들어갔을 것.
            if hash[cur][0] == "L":
                left = hash[cur][1] #현재 위치가 들어갈 것이다.
                index += 1
            else:
                right =hash[cur][1]
                index += 1
        else: #만약 2,5,8,0 중에 하나라면, 거리를 계산해야 할것.
            pos = hash2[cur]

            from_left = abs(pos[0]-left[0]) + abs(pos[1]-left[1])
            from_right = abs(pos[0]-right[0]) + abs(pos[1]-right[1])

            if from_left ==from_right:#왼쪽으로부터의 거리와 오른쪽으로부터의 거리가 같다면.
                if hand =='right':
                    answer += 'R'
                    right = pos
                    index+=1
                else:
                    answer += 'L'
                    left = pos
                    index+=1
            else: #같지 않다면, 더 작은 쪽을 구해준다.
                if from_right > from_left:
                    answer += 'L'
                    left = pos
                    index += 1
                else:
                    answer += 'R'
                    right = pos
                    index += 1
    return answer

