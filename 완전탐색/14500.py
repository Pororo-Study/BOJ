# 테트로미노
# https://www.acmicpc.net/problem/14500
# 완전탐색 + DFS

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)] # 방문 여부
answer = 0
dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0]


def dfs(x, y, cnt, total): # 좌표, 칸 개수, 정수의 합 
    global answer

    # 테트로미노 완성됐으면 최댓값 저장하고 리턴
    if cnt == 4:
        answer = max(answer, total)
        return

    # 4 방향 검사
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True # 방문처리
            dfs(nx, ny, cnt+1, total + board[nx][ny])
            visited[nx][ny] = False # 되돌리기

# T자 전용
def t_shape(x, y):
    global answer
    cnt = 0 # 칸 수
    arr = [] # 칸에 쓰인 수 저장하는 리스트
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            arr.append(board[nx][ny]) # 칸에 적힌 정수 저장
            cnt +=1 
    # 상하좌우 모두 성공
    if cnt == 4:
        arr.sort()
        answer = max(answer, sum(arr[1:]) + board[x][y])

    # 이미 T자형이기 때문에 바로 계산
    elif cnt == 3:
        answer = max(answer, sum(arr) + board[x][y])

for i in range(n):
    for j in range(m):
        visited[i][j] = True # 방문처리
        dfs(i, j, 1, board[i][j])
        t_shape(i, j)
        visited[i][j] = False # 되돌리기

print(answer)


# 첫번째 코드
# 시간초과

# visited를 set으룔 사용해서 
# 매번 합 다시 계산

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# answer = 0
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# def dfs(x, y, visited, cnt):
#     global answer

#     if cnt == 4:
#         total = 0
#         for i, j in visited:
#             total += board[i][j]

#         if answer < total:
#             print(visited, total)
#         answer = max(answer, total)
#         return

#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
#             visited.add((nx, ny))
#             dfs(nx, ny, visited, cnt+1)
#             visited.remove((nx, ny))
        
# def t_shape(x, y):
#     global answer
#     cnt = 0
#     arr = []
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             arr.append(board[nx][ny])
#             cnt +=1
#     if cnt == 4:
#         arr.sort()
#         answer = max(answer, sum(arr[1:]) + board[x][y])
#     elif cnt == 3:
#         answer = max(answer, sum(arr) + board[x][y])

# for i in range(n):
#     for j in range(m):
#         visited = set([(i, j)])
#         dfs(i, j, visited, 1)
#         t_shape(i, j)


# print(answer)
