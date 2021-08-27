#https://programmers.co.kr/skill_checks/309133
"""
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를
두 집합의 합집합 크기로 나눈 값으로 정의

"""

def solution(str1, str2):
    string1 =str1.upper()
    string2 = str2.upper()

    lst1 = [string1[i] + string1[i+1] if (string1[i] + string1[i+1]).isalpha() else None for i in range(len(string1) -1)]
    lst2 = [string2[i] + string2[i + 1] if (string2[i]+ string2[i+1]).isalpha() else None for i in range(len(string2) - 1)]
    hap = set(lst1+lst2)
    intersection = 0
    for i in hap:
        if i:
            count_for_lst1 = lst1.count(i)
            count_for_lst2 = lst2.count(i)
            inter_i = min(count_for_lst1,count_for_lst2)
            intersection += inter_i

    total_size = len(lst1) + len(lst2) - intersection -lst1.count(None) -lst2.count(None)
    if intersection != 0:
        return int(intersection/total_size * 65536)
    else :
        ss = "".join(list(filter(lambda x : x.isalpha(),str1))).upper()
        sx = "".join(list(filter(lambda x : x.isalpha(),str2))).upper()
        if ss==sx:
            return 65536
        else:
            return 0

str1 = "aa1+aa2"

str2 = "AAAA12"
solution(str1,str2)

