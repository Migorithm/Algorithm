#https://programmers.co.kr/learn/courses/30/lessons/12951

from collections import deque
def solution(s):
    answer = ''
    deq = deque(map(lambda x:x.capitalize(),s.split()))
    index_count = []
    for i in range(len(s)):
        if s[i].isalnum() == False:
            index_count.append(i)
    i = 0
    while i < len(s):
        if i in index_count:
            answer += ' '
            i +=1
        else:
            put = deq.popleft()
            answer += put
            i += len(put)
    return answer

print(solution("3people unFollowed me"))


'''
I thought it would be easy but with the condition in which there may be more than two white spaces in between words and
both ends, it got more difficult. 
Even though I didn't use this function, title() makes all the words capitalized while keeping spaces, which is 
actually not applicable to this particular case as you can't have capital letters after numbers. 
'''
