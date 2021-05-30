def solution(nums):
    a = set(nums)
    if len(a) >= int(len(nums)/2):
       return int(len(nums)/2)
    else:
        return len(a)


print(solution([3,3,3,2,2,2]))

def solution(nums):
    return int(len(nums) / 2) if int(len(nums) / 2) <= len(set(nums)) else len(set(nums))