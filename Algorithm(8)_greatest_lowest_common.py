
def common_multiple(n,m):
    #recursive case
    for i in range(2,min((n),(m))):
        if m%i ==0 and n%i ==0:
            m /= i
            n /= i
            return i*common_multiple(int(n),int(m))
    #base case
    return n*m



def solution(n, m):
    counter =[]
    for i in range(min(m,n),1,-1):
        if m%i == 0 and n%i ==0:
            if m%n ==0 or n%m ==0:
                counter.extend([i,max(m,n)])
                return counter
            counter.append(i)
            break #넣고 끝. 공약수.
    if len(counter)==0:
        return [1,n*m]
    else:
        counter.append(common_multiple(n,m))
        return counter

    #공배수 구하기



print(solution(2,5))





