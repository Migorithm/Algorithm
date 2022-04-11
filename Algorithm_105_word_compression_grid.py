#https://programmers.co.kr/learn/courses/30/lessons/60057


inp1="aabbaccc"
inp2="ababcdcdababcdcd"
inp3="abcabcdede"
inp4="abcabcabcabcdededededede"
inp5="xababcdcdababcdcd"
inp6 = "a"


def solution(s):
    if not len(s) >1:
        return 1
    MAX_LENGTH= int(len(s)/2)
    hash={}
    for i in range(1,MAX_LENGTH+1):
        hash[i] = []
        #For "gridify", get the index points. 
        grids= tuple(range(0,len(s)+1,i)) 
        
        cnt=1 #initialize cnt - 1
        for j in range(len(grids)-1):
            if hash[i][-1:] == [s[grids[j]: grids[j+1]]]: #Compare the value without causing error. If matched, increase cnt by 1
                cnt +=1
            else:                                         # If not matched, 
                if cnt >1:                                  
                    val = hash[i].pop()
                    hash[i].append(str(cnt)+val)
                    cnt=1 # reinitialize cnt -1 
                    hash[i].append(s[grids[j]: grids[j+1]])
                else:
                    hash[i].append(s[grids[j]: grids[j+1]])
        else:
            #To handle the case where the last letter is compressable
            if cnt >1:
                val = hash[i].pop()
                hash[i].append(str(cnt)+val)
            
            #If there is modulo, 
            if len(s) % i != 0:
                hash[i].append(s[-(len(s)%i):])
            
    answer =  2**63 - 1    #The biggest number allowed in Python
    for _,value in hash.items():
        if answer > len("".join(value)):
            answer = len("".join(value))
    return answer         
            
            
        
   

print(solution(inp1)) # 7
print(solution(inp2)) # 9
print(solution(inp3)) # 8
print(solution(inp4)) # 14
print(solution(inp5)) # 17
print(solution(inp6))
