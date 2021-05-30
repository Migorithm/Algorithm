def solution(n, arr1, arr2):
    bi = [str(bin(i|j))[2:] for i,j in zip(arr1,arr2)]
    emp = []
    for i in bi:
        while len(i) != n:
            i = '0'+i
        hash = ''
        for j in i:
            hash += '#' if j != '0' else ' '
        emp.append(hash)
    return emp

print(solution(6,[46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 =	[27 ,56, 19, 14, 14, 10]

bi = [str(bin(i|j))[2:] for i,j in zip(arr1,arr2)]
print(bi)



'''
output =	["######", "###  #", "##  ##", " #### ", " #####", "### # "]
ar1 = list(map(lambda x : bin(x)[2:],arr1))
ar2 = list(map(lambda x : bin(x)[2:],arr2))
zipper = zip(ar1,ar2)
hap = [str(eval(i)+eval(j)) for i,j in zipper]



print(hap)
print(ar1)
print(ar2)
print(hash)
'''