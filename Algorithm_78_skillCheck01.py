#https://programmers.co.kr/skill_checks/309127
def solution(n):
    if n%2 ==0:
        return "수박"*(int(n/2))
    else:
        return "수박"*(int(n/2)) + "수"

str = "수박수박수박수"

print(solution(4))