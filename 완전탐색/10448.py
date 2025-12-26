# 10448 유레카 이론
# https://www.acmicpc.net/problem/10448

from itertools import combinations_with_replacement # 중복 허용 조합

t = int(input())
arr = [(i*(i+1))//2 for i in range(1, 45, 1)] # 삼각수 T_1 ~ T_44까지 계산하기
candidates = list(combinations_with_replacement(arr, 3)) # 3개의 데이터를 뽑아 순서를 고려하지 않고 나열. 중복 허용함

for _ in range(t):
    k = int(input())
    check = False # 3개의 삼각수의 합으로 표현될수 있는지 여부

    for candidate in candidates:
        if sum(candidate) == k:
            print(1)
            check = True
            break
    if not check:
        print(0)