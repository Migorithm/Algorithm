#https://programmers.co.kr/learn/courses/30/lessons/68935


def solution(n):
    place = 0
    place_holder =[]
    while True:
        if 3**place <= n:
            place +=1
        else:
            if place ==0:
                break
            else:
                n -= 3**(place-1)
                place_holder.append(place-1)
                place =0
    a = ""
    for i in place_holder:
        a += '1'+ ('0' * i) + " "
    value = str(eval("+".join(a.split())))
    answer = 0
    for index,i in enumerate(value):
        if i !="0":
            answer += int(i)*3**index

    return answer



print(solution(125)) #229


