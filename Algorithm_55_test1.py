def solution(number, dictionary):
    answer = []
    for i in number:
        #주어진 i를 길이라고 보고, 그 길이와 일치하는 요소들로 필터링해준 첫번째 요소는 알파벳순서에서 가장 우선하는 요소일 것이다.
        lst = sorted(filter(lambda x:len(x)==int(i),dictionary))[0]
        #해당 요소를 빈 리스트에 더해준다.
        answer.append(lst)
        #중복되는 것을 없애기 위해 지워준다.
        dictionary.remove(lst)
    return " ".join(answer)



number = "11111111122"
dictionary = ["a","b","d","c","a","e","f","z","zz","za","az","e"]
print(solution(number,dictionary))