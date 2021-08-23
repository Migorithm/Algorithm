#https://programmers.co.kr/learn/courses/30/lessons/83201

#not using pandas
def solution(score):
    #reshape matrix
    lst = []
    for index,elements in enumerate(zip(*score)):
        if (elements[index] == min(elements) or elements[index] ==max(elements)) and elements.count(elements[index]) == 1:
            lst.append((sum(elements) - elements[index])/(len(elements)-1))
        else:
            lst.append(sum(elements)/len(elements))
    answer = ""
    for i in lst:
        if i >= 90:
            answer += "A"
        elif i >= 80:
            answer += "B"
        elif i >= 70:
            answer += "C"
        elif i >= 50:
            answer += "D"
        else:
            answer+= "F"
    return answer




score1 = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

solution(score1) #FBABD


# score2 = [[50,90],[50,87]]
# solution(score2)

#
# score3 = [[70,49,90],[68,50,38],[73,31,100]]
# solution(score3)