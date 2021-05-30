from functools import reduce
def solution(s):
    a = s.split()
    b = ''
    for i in a: #10개라고 할때, delimiter에 따라 구분 될 것.
        for j in range(len(i)):
            if j%2 ==0:
                b += i[j].upper()
            else:
                b += i[j].lower()
        b += ' '
    return b.strip()

print(solution("TrY HeLlO WoRlD"))