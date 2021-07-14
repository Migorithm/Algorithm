#https://www.acmicpc.net/problem/10162

#100 - > 0, 1 ,4
#500 -> 1,2,0

import sys
def microwave():
    inp = int(sys.stdin.readline().strip())
    A = 300
    B = 60
    C = 10
    answer = [0,0,0]
    while inp !=0 :
        cntA, cntB, cntC = [300,1000],[60,1000],[10,1000] #random number
        if inp%A != inp:
            cntA[1] = inp//A  # ->
        if inp%B != inp:
            cntB[1] = inp//B  # error! cntB becntes 1 not
        if inp % C != inp:
            cntC[1] = inp//C

        # 최소이랑 비교했을때, 같으면, 나눠지지 않은것.
        if inp == inp % min(cntA[1], cntB[1], cntC[1]) :
            return -1

        else:
            # 두번째가 가장 작은놈을 인덱스로 하여, 나눌값을 정하겠다.
            idx = (cntA[1], cntB[1], cntC[1]).index(min(cntA[1], cntB[1], cntC[1]))
            answer[idx] +=1
            subtract = (cntA[0], cntB[0], cntC[0])[idx]
            inp = inp - subtract
    return answer
x = microwave()
print(" ".join(map(str,x)) if type(x) ==list else "-1")
