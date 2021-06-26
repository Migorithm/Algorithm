from collections import defaultdict
from functools import reduce
from collections import deque
from itertools import islice

#https://www.youtube.com/watch?v=LPzN8jgbnvA


def solution(phone_book):

    a = len(min(phone_book,key=len))
    b = defaultdict(int)
    for i in phone_book:
        b[i[:a]] +=1
    if sum(b.values()) != len(b):
        return False
    else:
        return True


def solution2(phone_book):
    a = sorted(phone_book,key=len)
    j = 0
    while j < len(a):
        b = defaultdict(int)
        for i in a[j:]:
            b[i[:len(a[j])]] +=1
        if sum(b.values()) != len(b):
            return False
        else:
            j+=1
    else:
        return True


#deque
def solution3(phone_book):
    a = deque(sorted(phone_book,key=len))
    while a != deque([]):

        for i in islice(a,1,len(a)):
            if i[:len(a[0])] == a[0]:
                return False
            else:
                continue
        a.popleft()
    return True


def solution4(phone_book):
    a = sorted(phone_book,key=len)
    hash = defaultdict(int)
    j = 0
    while j < len(a):
        for i in a[j:]:
            if a[j] == i[:len(a[j])] :
                hash[a[j]] +=1
        if len(hash) != sum(hash.values()):
            return False
        j+=1
    return True

def solution5(phone_book):
    phoneBook = sorted(phone_book)
    print(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1,p2)
        if p2.startswith(p1):
            return False
    return True



def solution6(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    #해쉬 안에 1로 저장해준다.
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            #temp에 번호들을 하나씩 저장하고 만약 그 번호가 hash의 키와 같고 본인이 따온 번호 그 자체가 아니라면.
            if temp in hash_map and temp != phone_number:
                print(temp)
                answer = False
    return answer

print(solution6(["1919999","180032","180"]))


