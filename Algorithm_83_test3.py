def solution(candles):
    days = 0

    for i in range(1,len(candles)+1):
        candles.sort(reverse=True)
        #lengh check
        candidates = list(filter(lambda x : x>=1,candles))

        #number check
        if len(candidates) >= i:
            days+=1

            # substracting numbers (-1)
            for j in range(i):
                candles[j] -= 1
        else:
            break

        #substracting numbers (-1)



    return days

candles =  [2,2,2,4]

print(solution(candles))