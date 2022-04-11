#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record): #3.10 
    Last_name_dict=dict()
    temp = []
    for event in record:
        env = event.split()
        match env[0]:
            #Enter
            case "Enter":
                temp.append([env[1],"님이 들어왔습니다."])
                Last_name_dict[env[1]] = env[2]
            #Leave
            case "Leave":
                temp.append([env[1],"님이 나갔습니다."])
            #Change
            case _:
                Last_name_dict[env[1]] = env[2]
    result = list(map(lambda x : Last_name_dict[x[0]] + x[1],temp))
    return result
    
def solution(record): #below 3.10
    Last_name_dict=dict()
    temp = []
    for event in record:
        env = event.split()
        if env[0]=="Enter":
            temp.append([env[1],"님이 들어왔습니다."])
            Last_name_dict[env[1]] = env[2]
        elif env[0] == "Leave":
            temp.append([env[1],"님이 나갔습니다."])
        else:
            Last_name_dict[env[1]] = env[2]
    result = list(map(lambda x : Last_name_dict[x[0]] + x[1],temp))
    return result
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))


