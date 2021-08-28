#message는 오직 소문자만을 가지거나 ('a'-'z') 혹은 오직 숫자만을 가진다 ('0'-'9').

def solution(code, message):
    #딕셔너리를 이용, meesage의 형태에 상관없이 답을 매핑할 것이다.

    hash_key_alpha ={}
    hash_key_num= {}

    for i in range(1,len(code)+1):
        #우선, ascii 코드에 맞춰 연산한후 스트링 처리한다.
        conversion = str(i)
        if len(conversion) ==1:
            #0을 추가해, 순서상의 오류를 없앤다.
            conversion = "0"+conversion
        #알파벳을 키로하여 숫자를 맵핑
        hash_key_alpha[code[i-1]] = conversion

        #숫자를 키로하여 알파벳을 맵핑
        hash_key_num[conversion] = code[i-1]

    #순수하게 알파벳으로만 이루어져있다면,
    if message.isalpha():
        answer = ""
        for i in message:
            answer += hash_key_alpha[i]
        return answer

    #순수하게 숫자로만 이루어져 있다면 2단위씩 끊어서 진행.
    else:
        answer =""

        for i in range(0,len(message),2):
            answer += hash_key_num[message[i] +message[i+1]]
        return answer

print(solution("abcdefghijklmnopqrstuvwxyz",  "a"))
print(solution("abcdefghijklmnopqrstuvwxyz",  "1409030516120125"))