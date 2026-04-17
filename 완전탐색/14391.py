# 종이 조각
# https://www.acmicpc.net/problem/14391

# 비트마스크
# 완전탐색
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)] # str로 저장

answer = 0

# 모든 경우의 수 (각 칸을 가로/세로로 나누는 경우)
for bit in range(1 << (n * m)): # 2^(n*m)
    total = 0

    # 가로 계산
    for i in range(n):
        num = "" # 현재 이어붙이고 있는 숫자
        for j in range(m):
            idx = i * m + j # 2차원 → 1차원 인덱스

            # 현재 칸이 가로(0)인 경우
            if (bit & (1 << idx)) == 0:
                num += board[i][j] # 숫자 이어붙이기
            else:
                if num: # num != ""
                    total += int(num) # 끊기면 지금까지 숫자 더하기
                    num = ""
        
        # 행 끝나면 마지막 숫자 더하기
        if num:
            total += int(num)

    # 세로 계산
    for j in range(m):
        num = "" # 현재 이어붙이고 있는 숫자
        for i in range(n):
            idx = i * m + j # 2차원 → 1차원 인덱스

            # 현재 칸이 세로인 경우
            if (bit & (1 << idx)) != 0:
                num += board[i][j]
            else:
                if num:
                    total += int(num)
                    num = ""

        # 열 끝나면 마지막 숫자 더하기
        if num:
            total += int(num)

    answer = max(answer, total) # 최댓값 갱신

print(answer)