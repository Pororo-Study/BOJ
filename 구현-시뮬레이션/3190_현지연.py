from collections import deque
n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수

board = [[0] * n for _ in range(n)] # 보드
# 보드에 사과 위치 저장(2로 표시)
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2

l = int(input())    # 방향 변환 정보 개수
info = deque([])    # 방향 변환 정보
# 방향 변환 정보 저장
for _ in range(l):
    a, b = input().split()
    info.append((a, b))
a, b = info.popleft()   # 첫번째 방향 변환 정보 가져오기

t = 0               # 시간
direction = 0       # 뱀의 방향(동, 남, 서, 북 순서)
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 좌표 이동
dy = [1, 0, -1, 0]
x, y = 0, 0         # 뱀 머리 좌표
q = deque([(x, y)]) # 뱀 전체 좌표 큐
board[x][y] = 1     # 현재 뱀 위치 1로 표시

while True:
    t += 1
    nx = x + dx[direction]  # 다음 뱀 머리 좌표
    ny = y + dy[direction]

    if 0 <= nx < n and 0 <= ny < n: # 벽과 부딪히지 않은 경우
        # 자기자신의 몸과 부딪힌 경우
        if board[nx][ny] == 1:
            break
        # 사과를 먹은 경우
        elif board[nx][ny] == 2:
            q.append((nx, ny))  # 뱀의 머리 좌표를 큐에 추가 
            board[nx][ny] = 1   # 현재 뱀 위치 1로 표시
        # 빈칸으로 이동한 경우
        else:
            q.append((nx, ny))  # 뱀의 머리 좌표를 큐에 추가 
            board[nx][ny] = 1   # 현재 뱀 위치 1로 표시
            # 꼬리가 위치한 칸 비워주기
            tail_x, tail_y = q.popleft()    
            board[tail_x][tail_y] = 0
        x, y = nx, ny   # 뱀 머리 좌표 업데이트
    else:       # 벽에 부딪힌 경우
        break
    
    # a초가 끝난 뒤 방향 회전
    if t == int(a):
        # 왼쪽으로 90도 회전
        if b == 'L':
            direction = (direction - 1) % 4
        # 오른쪽으로 90도 회전
        else:
            direction = (direction + 1) % 4
        if info:
            a, b = info.popleft()         

print(t)