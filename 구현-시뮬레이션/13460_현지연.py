# 구슬 탈출 2
# https://www.acmicpc.net/problem/13460

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

rx, ry, bx, by = 0, 0, 0, 0 # bfs() 함수화를 위한 초기화
# 구슬의 좌표 구하기
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            rx, ry = i, j
        elif board[i][j] == "B":
            bx, by = i, j

q = deque([(rx, ry, bx, by, 1)])    # 큐
visited = {(rx, ry, bx, by)}        # 방문여부를 집합에 저장

# 구슬 끝까지 움직이기
def move(x, y, dx, dy):
    cnt = 0 # 움직인 칸 수
    while board[x+dx][y+dy] != "#": # 벽이 아닐때까지 이동
        if board[x+dx][y+dy] == "O":    # 구멍이면 0 반환
            return 0, 0, 0
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10:
            break
            
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i]) # 빨간 구슬 움직이기
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i]) # 파란 구슬 움직이기

            # 파란 구슬이 구멍에 들어간 경우 
            if nbx == 0 and nby == 0:
                continue
            
            # 빨간 구슬이 구멍에 들어간 경우 성공
            elif nrx == 0 and nry == 0:
                print(cnt)
                return

            # 두 구슬이 같은 칸에 있는 경우 많이 움직인 구슬을 한 칸 뒤로 보냄
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))
    print(-1)   # 실패

bfs()