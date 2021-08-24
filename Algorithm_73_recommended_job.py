#https://programmers.co.kr/learn/courses/30/lessons/84325

"""
개발자가 사용하는 언어의 (언어 선호도)*(직업군 언어 점수)의 총합이 가장 높은 직업군을 return 하도록 solution 함수

"""
def solution(table, languages, preference):
    #hash map만들기.
    lst  = [i.split() for i in table]
    point_table = {i[0]:i[-1:0:-1] for i in lst}

    area = {i:0 for i in point_table.keys()}
    for i,j in zip(languages,preference): #language당 preference
        for k in point_table:
            if i in point_table[k]:
                language_point = point_table[k].index(i) +1
                area[k] += language_point*j

    num  =0 # to keep tract of the maximum number

    close_to_answer = {}
    for value,key in area.items():
        if key not in close_to_answer:
            close_to_answer[key] = [value]
            if key > num:
                num = key
        else:
            close_to_answer[key].append(value)

    return sorted(close_to_answer[num])[0]



table =["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]

languages = ["PYTHON", "C++", "SQL"]

preference = [7, 5, 5]

print(solution(table,languages,preference)) #HARDWARE


table2=["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]

languages2=["JAVA", "JAVASCRIPT"]

preference2 = [7, 5]

print(solution(table2,languages2,preference2))