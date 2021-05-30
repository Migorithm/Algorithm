
def solution(lottos, win_nums):
    answer =[]
    cnt =0
    for i in win_nums:
        if i in lottos:
            cnt +=1
            lottos.remove(i)
    answer.append(7- (cnt + lottos.count(0))) if cnt+lottos.count(0) >0 else answer.append(6)
    answer.append(7 - cnt) if cnt >= 2 else answer.append(6)
    return answer


print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))


'''
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
'''


win_nums1 = [31, 10, 45, 1, 6, 19]
lottos1= [44, 1, 0, 0, 31, 25]


win_nums2 = [38, 19, 20, 40, 15, 25]
lottos2= [0, 0, 0, 0, 0, 0]
