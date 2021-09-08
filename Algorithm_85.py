#https://programmers.co.kr/learn/courses/30/lessons/67257
"""


+ - *

+>*>-  - > o
+,*>-  - > x

-> factorial
if negative -> abs(x)


"""







import re
def solution(expression):
    answer = []
    combinations = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    for combination in combinations:
        operand = re.split('[*+-]',expression)
        operator = re.split('[0-9]+',expression)[1:-1]
        for comb in combination:
            while comb in operator:
                idx = operator.index(comb)
                operand[idx] = str(eval(operand[idx] + comb + operand[idx+1]))
                del operand[idx+1]
                del operator[idx]
        answer.append(abs(int(operand[0])))
    return max(answer)






print(solution("177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"))





