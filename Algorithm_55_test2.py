'''
문제 설명
선희와 영수는 대학에서 문자열 이론을 공부하고 있다.
영수는 팰린드롬을 아주 좋아한다.
팰린드롬은 앞에부터 읽어도, 뒤에서부터 읽어도 같은 단어를 말한다.
선희는 영수를 임의의 문자열 s로 팰린드롬을 만들어 영수를 깜짝 놀래켜주고 싶어한다.
이때 선희은 문자열 s 뒤에 0개 이상의 문자를 추가해 팰린드롬을 생성하려 한다.
선희가 생성할 수 있는 가장 짧은 팰린드롬의 길이를 반환하라.

'''
from collections import deque
def solution(s):
    #주어진 문자열의 역이 되는 문자열 생성
    rs= s[::-1]
    #주어진 문자열(s)와 그 역(rs)가 같다면, 길이를 리턴.
    if s == rs:
        return len(s)
    for index in range(1,len(s)): #0,1,2,3
        #한글자씩 읽어가면서 어느 스트링의 어느 인덱스 이후 지점의 역이 역이 아닌 스트링과 일치하는지 검증.
        rs = s[:index-1:-1]

        cs = s[index:]
        if rs == cs and index != (len(s)-1):
            return len(cs) + index*2
    #만약 답을 위의 식에서 구하지 못했다면, 팰린드롬 형식이 아니라는 것.
    return len(s)*2 -1


s = "supep" #should be 7

print(solution(s))