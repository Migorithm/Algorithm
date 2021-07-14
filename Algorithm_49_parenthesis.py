"""
https://programmers.co.kr/learn/courses/30/lessons/60058
"""

def solution(p):
    #base case
    if p =="":
        return ""
    u = ""
    v = ""
    for i in range(len(p)):
        u += p[i]
        if u.count("(") == u.count(")"):
            v += p[i+1:]
            break
    # recursive case
    if u.startswith("("):
        return u + solution(v)
    else:
        ru = "(" + solution(v) + ")"
        repl = u[1:-1].replace("(",".")
        repl2 = repl.replace(")","(")
        repl3 = repl2.replace(".",")")
        return ru + repl3



print(solution(")))(()())((("))

