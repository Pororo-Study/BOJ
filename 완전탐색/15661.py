# 링크와 스타트
# https://www.acmicpc.net/problem/15661

# DFS
# python3 시간초과
# pypy3 성공
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

visited = [False] * n # 링크팀 여부

def dfs(idx):
    global answer

    # 팀 배분이 끝났으면 능력치 차이 계산
    if idx == n: 
        link = 0 # 링크팀의 능력치
        start = 0 # 스타트팀의 능력치

        for i in range(n):
            for j in range(i+1, n): # i, j 와 j, i 값이 중복되지 않도록
                if visited[i] and visited[j]: # 둘 다 링크팀이면
                    link += board[i][j] + board[j][i]
                elif not visited[i] and not visited[j]: # 둘 다 스타트팀이면
                    start += board[i][j] + board[j][i]

        answer = min(answer, abs(link - start)) # 최솟값 저장
        return

    visited[idx] = True
    dfs(idx + 1)

    visited[idx] = False
    dfs(idx + 1)

dfs(0)
print(answer)

# # combination으로 완전탐색
# # python3 시간초과
# # pypy3 성공
# from itertools import combinations

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# answer = float('inf')

# people = set(range(n)) # 사람들

# for k in range(1, n//2+1): # A, B 팀은 B, A 팀이어도 능력치의 차가 똑같기 때문에 중복 방지
#     for team_a in combinations(range(n), k): # k명을 순서상관없이 A팀에 배치하는 모든 경우

#         team_a = set(team_a) # A팀 명단
#         team_b = people - team_a # B팀 명단

#         # 능력치 각각 더하기
#         power_a, power_b = 0, 0
#         for i, j in list(combinations(team_a, 2)): # A팀에서 2명 뽑기
#             power_a += board[i][j] + board[j][i]

#         for i, j in list(combinations(team_b, 2)): # B팀에서 2명 뽑기
#             power_b += board[i][j] + board[j][i]

#         # 차이 구하기
#         answer = min(answer, abs(power_a - power_b))

# print(answer)