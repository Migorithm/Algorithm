


'''두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수,
solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.


n	m	return
3	12	[3, 12]
2	5	[1, 10]
'''

def solution(n, m):
    answer = []
    #최소 공약수
    for i in range(2, m+1):
        if m%i ==0 and n%i == 0:
            answer.append(i)
            break
    else:
        answer.append(1)
    #최소 공배수 (recursive?)
    answer.append(lcm(m,n))
    return answer

def lcm(m,n):
    for i in range(2,max(int(m),int(n))): #둘중 큰놈:
        if m%i ==0 and n%i ==0:
            a = i
            return a * lcm(divmod(m,i)[0],divmod(n,i)[0])
    #base case
    return m*n
print(solution(15,39))