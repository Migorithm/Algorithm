#data = [3,5,8] - > find out the possible sums of numbers that are unique.

def data():
    data = [3,5,8]
    result = set()
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result.add(data[0]*i + data[1]*j + data[2]*k)
    print(result)
    #뽑거나, 뽑지않거나. 두가지의 수. 그리고 중복을 제거하기 위한 set()

data()
