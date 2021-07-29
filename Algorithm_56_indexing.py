#https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    hash ={}
    for i in strings:
        if i[n] in hash:
            hash[i[n]].append(i)
        else:
            hash[i[n]] = [i]
    keys = sorted(hash.keys())
    answer = []
    for i in keys:
        hash[i].sort()
        answer.extend(hash[i])
    return answer

lst = ["ae","be","ce","ae"]
n1 = 1

lst2 =["abce", "abcd", "cdx"]
n2 = 2

solution(lst,n1)