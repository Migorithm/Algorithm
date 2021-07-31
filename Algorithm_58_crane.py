#https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

import numpy as np
import pandas as pd

def solution(board, moves):
    df = pd.DataFrame(board)
    moves = moves
    deck = []

    df.columns +=1
    cnt = 0
    for targetline in moves:
        #만약 해당 라인이 이미 비어있다면, pass
        if np.array(df[targetline]>0).sum() == 0:
            continue

        # need to find index whose value is not 0. -> 0이 아닌 값에대한 넘파이 어레이를 만들고 argmax로 인덱스를 구한다.
        index = np.array(df[targetline]>0).argmax()

        #deck 에 해당 값을 더해주고 빠진 인형에 대해선 0으로 처리해준다.
        deck.append(df.at[index,targetline])
        df.at[index,targetline] = 0

        #deck의 크기가 1보다 크다면 뒤의 두 값을 비교해보고 같으면 제거해준다.
        if len(deck) >1 :
            if deck[-1] == deck[-2]:
                deck.pop()
                deck.pop()
                cnt += 2
    return cnt


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

solution(board,moves)