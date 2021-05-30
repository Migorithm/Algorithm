import string
from functools import reduce
import re

def solution(new_id):
    answer = []
    for i in range(len(new_id)):
        if new_id[i] in string.ascii_letters + '-_.1234567890' :
            if new_id[i].isalpha():
                answer.append(new_id[i].lower())
            else:
                answer.append(new_id[i])
    while len(answer) != 0:
        if answer[0] == '.':
            del answer[0]
            continue
        if answer[-1] == '.':
            del answer[-1]
            continue
        break
    if answer == []:
        return 'aaa'
    if len(answer) <=2:
        while len(answer)!=3:
            answer.append(answer[-1])
    answer = (reduce(lambda x,y:x+y if not x[-1] == y == '.'else x,answer)) ## conversion.
    if len(answer) >15:
        return answer[:15] if answer[:15][-1] != '.' else answer[:14]
    else :
        return answer



def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st

print(solution("=.="))
