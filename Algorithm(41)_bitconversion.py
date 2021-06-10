#https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n,arr1,arr2):
    bit = list(map(lambda x,y:bin(x|y)[2:] , arr1,arr2))
    answer = []
    for i in bit:
        while len(i) != n :
            i = '0' + i
        str = i.replace('0',' ')
        str2 = str.replace('1','#')
        answer.append(str2)
    return answer


