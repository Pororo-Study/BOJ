# 숫자 야구
# https://www.acmicpc.net/problem/2503

from itertools import permutations
from copy import deepcopy

n = int(input())
arr = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3)) # 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수 후보들

for _ in range(n):
    ask, strike, ball = map(int, input().split()) # 민혁이가 질문한 세 자리 수, 영수가 답한 스트라이크 개수, 볼의 개수
    ask = str(ask) # 자리수별로 비교를 위해 문자열로 형변환
    new_arr = [] # 살아남은 후보들을 저장하기 위한 리스트

    for c in arr: # 후보들
        s, b = 0, 0 # 후보의 스트라이크, 볼 개수 초기화
        for i in range(3): # 자릿수만큼 반복
            if c[i] == ask[i]: # 동일한 자리에 위치하면 스트라이크
                s += 1
            elif ask[i] in c: # 세 자리 수에 있긴 하나 다른 자리에 위치하면 볼
                b += 1
        if strike == s and ball == b:
            new_arr.append(c)
    
    arr = deepcopy(new_arr) # 다음 질문에 사용할 살아남은 후보들

print(len(arr))