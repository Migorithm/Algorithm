#https://programmers.co.kr/learn/courses/30/lessons/92334


#Production event handling
class Subscriber:
    def __init__(self,user,reported):
        self.user = user
        self.reported = reported
    def update(self):
        print(f"{self.user} : {self.reported} has been suspended")
        return f"{self.reported} has been suspended"
    
class Publisher:
    def __init__(self):
        self.subscribers=dict()
    def register(self,sub:Subscriber):
        if self.subscribers.get(sub.reported):
            self.subscribers[sub.reported].append(sub)
        else:
            self.subscribers[sub.reported] = [sub] 
    def notify(self,k):
        for _,users in self.subscribers.items():
            if len(users)>=k:
                for user in users:
                    print(user)
                    user.update()
pub= Publisher()
muzi=Subscriber("muzi","frodo")
frodo=Subscriber("frodo","neo")
muzi2=Subscriber("muzi","neo")
apeach=Subscriber("apeach","muzi")
apeach2=Subscriber("apeach","frodo")

pub.register(muzi)
pub.register(frodo)
pub.register(muzi2)
pub.register(apeach)
pub.register(apeach2)
pub.notify(2)


#For test
def solution(id_list, report, k):
    dic =dict()
    reporters = {reporter:0 for reporter in id_list }
    for repo in set(report):
        reporter,reported = repo.split()
        if dic.get(reported):
            if reporter not in dic[reported]:
                dic[reported].append(reporter)
        else:
            dic[reported] = [reporter]
            
    for v in dic.values():
        if len(v) >=k:
            for i in v:
                reporters[i] +=1
            
    answer = list(reporters.values())
    return answer