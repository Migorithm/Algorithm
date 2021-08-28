def solution( instructions):
    answer = 0
    for i in instructions:
        if answer >= 360:
            answer %= 360
        #HALT사인을 받지 않는다면 연산을 계속한다..
        if i != "HALT":

            #계산의 용이성을 위해 TURN AROUND는 따로 처리해주었다.
            if i != "TURN AROUND":

                #word를 split하고,
                word = i.split()

                #요소가 1개 이상이라면 (즉, right x라면)
                if len(word) >1:

                    #다른 함수를 호출해 처리해준다. (parameter 2개)
                    answer = calculator(word[0],answer, word[1])
                else:
                    answer = calculator(i,answer)
            else :
                answer += 180

        #HALT사인 받은 경우, break.
        else:
            break
    if answer >=360:
        answer %= 360
    return answer



def calculator(direction,answer , angle=None):
    hash = {"RIGHT":90,
            "LEFT":-90,
            f"RIGHT {angle}":int(angle) if angle else None,
            f"LEFT {angle}":-int(angle) if angle else None}
    if answer + hash["{}".format(direction) + " {}".format(angle) if angle else f"{direction}"] <0:
        answer += 360 + hash["{}".format(direction) + " {}".format(angle) if angle else f"{direction}"]
    else:
        answer += hash["{}".format(direction) + " {}".format(angle) if angle else f"{direction}"]
    return answer

instructions = ["LEFT 45","LEFT 90", "TURN AROUND"]


print(solution(instructions))

