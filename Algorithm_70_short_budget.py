#https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    money = money
    for i in range(1,count+1):
        money -= i*price
    if money < 0:
        return abs(money)
    else:
        return 0



price = 3
money = 20
count =4

print(solution(price,money,count)) #10
