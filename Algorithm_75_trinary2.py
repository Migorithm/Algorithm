#https://programmers.co.kr/learn/courses/30/lessons/68935


def solution(n):
    tmp = ''
    while n:               ####while n is NOT 0 (or False)
        tmp += str(n % 3)  #if dividable by 3, it will return 0 and '0' will be added to tmp.
        n = n // 3
    answer = int(tmp, 3)   #int can convert string to "xxx"-nary number
    return answer          #for example, int("00212",3) will become 23.

print(solution(45))

