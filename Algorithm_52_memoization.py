import time
hash = {1 : 1, 2 :1}

def memoization(n):
    if n in hash:
        return hash[n]
    else :
        hash[n] = memoization(n-1) + memoization(n-2)
        return hash[n]

def fibo(n):
    if n == 1:
        return 1
    if n ==2 :
        return 1
    return fibo(n-1) + fibo(n-2)

a = time.time()
print(memoization(40))
b = time.time()
print("time it takes with memoization : " + str(b-a) )


a = time.time()
print(fibo(40))
b = time.time()
print("time it takes: " + str(b-a) )
# 1 1 2 3 5 8 13 21