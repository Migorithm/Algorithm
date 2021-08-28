def solution(tri):
    container = []
    while len(tri)!=1:
        smallest = tri.pop()
        for i in range(len(smallest)):

                #to check if it's alright.
            if str((tri[-1][i]) + (tri[-1][i + 1])).isnumeric():
                continue
            else:
                #to find the first index of "?" + slicing
                index_for_question = tri[-1][i:].index("?")
                if index_for_question == 0 :
                    question_index = i
                    corrected = str(abs(int(smallest[i]) - int(tri[-1][question_index+1]) +10 ))[-1]
                    corrected_one = tri[-1][:question_index] + corrected + tri[-1][question_index+1:]
                    tri[-1] = corrected_one


                else:
                    question_index = i+1
                    corrected = str(abs(int(smallest[i]) - int(tri[-1][question_index-1]) +10 ))[-1]
                    corrected_one = tri[-1][:question_index] + corrected + tri[-1][question_index+1:]
                    tri[-1] = corrected_one

        else:
            container.append(smallest)
    else:
        container.append(tri[-1])
    answer = container[::-1]
    return answer



#tri = ["794453","63898","9177","077","74","1"]
tri = ["7????3","?3?9?","9??7","0?7","?4","1"]

#tri2 = ["3255","579","26","8"]

tri2 = ["?2?5","57?","?6","8"]
print(solution(tri))

print(solution(tri2))