# 3085 사탕 게임
# https://www.acmicpc.net/problem/3085

def evaluate(graph):
    max_cnt = 1
    # 가로줄 확인
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    # 세로줄 확인
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if  graph[i][j] == graph[i-1][j]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    return max_cnt # 최댓값 반환

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))

dx = [0, 1] # 오른쪽, 아래 방향만 정의
dy = [1, 0]
answer = 1

for x in range(n): # 모든 칸을 돌면서
    for y in range(n):
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y] # 사탕 교환
                answer = max(answer, evaluate(board)) # 평가
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y] # 교환한 사탕 되돌리기

print(answer)