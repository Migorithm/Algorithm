#https://programmers.co.kr/learn/courses/30/lessons/83201


#1using numpy and pandas
import numpy as np
import pandas as pd
def solution(scores):
    df = pd.DataFrame(scores)
    lst = []
    for i in range(df.shape[1]):
        a = df.loc[:,i].values
        count = a == a[i]

        if (a[i] == max(a) or a[i] == min(a)) and count.sum() ==1: #다른 값으로 같을때 ensure못한다.

            lst.append(float(a.sum() - a[i])/(df.shape[1]-1))


        else:
            lst.append(float(a.sum())/df.shape[1])
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

