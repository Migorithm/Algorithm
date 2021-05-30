'''어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와
이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

signs의 길이는 absolutes의 길이와 같습니다.
signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을,
그렇지 않으면 음수임을 의미합니다.
'''
'''
absolutes	signs	result
[4,7,12]	[true,false,true]	9
[1,2,3]	[false,false,true]
'''


def solution(absolutes, signs):
    answer = 0
    for i,j in zip(absolutes,signs):
        if j == False:
            answer += (-i)
        else:
            answer += i
    return answer

