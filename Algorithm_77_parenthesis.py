#https://programmers.co.kr/learn/courses/30/lessons/12909



def solution(s):
    la = []
    if s.startswith(")"):
        return False
    if not s.endswith(")"):
        return False
    for i in range(len(s)):

        if s[i] == "(":
            la.append(s[i])
        else:
            try:
                la.pop() #if it's not poppable, it is mismatched.
            except:
                return False
    else:
        if la != []:     #if it's not empty, it's going to be pack full of "("
            return False
        return True

s = "(((("

print(solution(s))



def is_pair(s):
    x = 0
    for w in s:
        if x < 0:  #if x is smaller than 0, break.
            break
        x = x+1 if w=="(" else x-1
        # if w == "(", x+1
        # else , x-1
    return x==0

