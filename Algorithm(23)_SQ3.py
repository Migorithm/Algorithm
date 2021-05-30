def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing = [0] * bridge_length# like a conveyor belt.
    cnt = 0
    while truck_weights != []: #일단 웨이팅 리스트를 비우자.
        if sum(crossing) + truck_weights[0] <= weight: #합한것 + 기다리는 첫번째 트럭이 탔을때 허용량 이하인 경우.
            crossing.pop(0)
            crossing.append(truck_weights[0])
            del truck_weights[0]
            cnt +=1
        else:                                          #이상인 경우
            if crossing[-1] + truck_weights[0] > weight: #막 다리에 진입한것과 대기중인 것의 합만으로 이미 기준치를 초과하면 다 건널때까지 기다려야 할 것. 따라서 바로 처리해준다.
                answer += cnt + bridge_length  #여기서 다리의 길이는 다리를 건너는 시간과 같다.
                crossing =[0]*(bridge_length-1) #initialize len-1까지.
                crossing.append(truck_weights[0]) #모든 개체가 다리를 건너는 순간 대기중인 트럭이 진입할 것.
                del truck_weights[0]
                cnt = 0
                continue
            elif crossing[0] != 0:
                cnt+=1
                crossing.pop(0)
                if sum(crossing) + truck_weights[0] <= weight:
                    crossing.append(truck_weights[0])
                    del truck_weights[0]
                else:
                    crossing.append(0)
            else:
                cnt+= 1
                crossing.pop(0)
                crossing.append(0)
    else:
        answer += cnt + bridge_length
        return answer


print(solution(100,100,[10]*10))
