'''
당신은 학교에서 집까지 도시를 거쳐 걸어가고 있다.
도시는 무한히 크며 모든 X값에는 수직 도로가 놓여있고 모든 Y에는 수평 도로가 놓여있다.
당신은 현재 (0, 0)에 있으며 (X, Y)에 있는 집에 가려고 한다.
집까지 가는 방법에는 두가지가 있다:
수평 혹은 수직으로 인접한 교차로를 거쳐 ( walkTime 초가 걸린다) 도로를 따라 걷는 것과
몰래 대각선으로 건너 ( sneakTime 초가 걸린다) 반대쪽 모서리로 가는 방법이 있다.

이미지에 나와있는 것처럼 걷거나 대각선을 가로지르는 8가지 방향 어느쪽으로도 가는 것이 가능하다 (예제 2번 참고).

'''



def solution(X, Y, walkTime, sneakTime):
    if sneakTime > walkTime:
        if sneakTime >= walkTime** 2 :
            return (abs(X) + abs(Y)) * walkTime
    #제곱한것보다는 작은 경우 -> 직선코스는 walkTime, 대각선 코스는sneakTime.
        else:
        #직선코스
            direct = (abs(X)-abs(Y))*walkTime
        #대각선코스
            diagonal = min(abs(X),abs(Y))*sneakTime
            return direct+diagonal
        #가로질러가는것도, 직선으로가는 것도 sneakTime이 나은 경우

    #sneak타임이 더 작거나 같다면,
    else:
        direct = (abs(X) - abs(Y))*sneakTime
        diagonal = min(abs(X), abs(Y)) * sneakTime
        return direct + diagonal




X = 4
Y = 2
walkTime = 3
sneakTime = 10
print(solution(X,Y,walkTime,sneakTime)) #18

X = 4
Y = 2
walkTime = 3
sneakTime = 5
print(solution(X,Y,walkTime,sneakTime)) #16

X = 2
Y = 0
walkTime = 12
sneakTime = 10
print(solution(X,Y,walkTime,sneakTime)) #20

X = 1000000
Y = 1000000
walkTime = 1000
sneakTime = 1000
print(solution(X,Y,walkTime,sneakTime)) #: 1000000000

X = 0
Y = 0
walkTime = 12
sneakTime = 25
print(solution(X,Y,walkTime,sneakTime)) #: 0

