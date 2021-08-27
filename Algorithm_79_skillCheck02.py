#https://programmers.co.kr/skill_checks/309127?challenge_id=955

def solution(phone_number):
    return "*"*len(phone_number[:-4]) +phone_number[-4:]


phone_number = "01033334444"

print(solution(phone_number))