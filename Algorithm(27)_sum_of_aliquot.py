def solution(n):
    b= [i for i in range(1,n+1) if n%i ==0]
    return sum(b)

print(solution(12))

