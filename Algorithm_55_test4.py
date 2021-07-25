"""
price: 고객 i가 지출할 수 있는 제일 높은 가격과
cost : 각각 배송 비용이 담겨 있다.

매출을 극대화할 수 있는 물건의 가격을 반환하여라.
최적의 가격이 2가지 이상 존재한다면 더 작은 가격을 리턴하시오.
이윤을 남길 수 없다면 0을 리턴하시오."
"""

def solution(price, cost):
    #예상되는 수익 리스트
    potential_bf=[]

    for i in range(len(price)):
        how_much=0
        for j in range(len(cost)):
            #배송비보다 이익금이 많고, 현재 판매하는 물건이 소비자의 구매능력을 초과하지 않을 때,
            if price[i]-cost[j] >0 and price[i] <= price[j]:
                how_much +=price[i]-cost[j]
        potential_bf.append(how_much)

    #예상 수익리스트의 최저값이 0이라면, 예상수익이 없다는 것 -> 리턴 0
    if min(potential_bf) == 0:
        return 0

    index_list = []
    #최적 예상 수익이 같은 값이 있는지 확인
    if potential_bf.count(max(potential_bf)) >1:

        #가장 낮은 값의 인덱스 구하기.
        #1) 최고값에 해당하는 인덱스 전체를 구한다.
        max_value = max(potential_bf)
        while max_value in potential_bf:
            index_list.append(potential_bf.index(max(potential_bf)))
            potential_bf.remove(max_value)
        #2) 구한 인덱스들을 가지고 검색해본다.
        for_min =[]
        for i in index_list:
            for_min.append(price[i])
        return min(for_min)
    else:
        return price[potential_bf.index(max(potential_bf))]






#리스트의 길이 = 고객의 수
price = [13,17,14,30,19,17,55,16]#이것은 고객의 소비 능력에 해당하기때문에, 소비 능력이 높은 고객은 배송비용이 낮은 것에 대해서는 우려 ㄴㄴ
cost = [12,1,5,10,3,2,40,19]
print(solution(price,cost))
#22


