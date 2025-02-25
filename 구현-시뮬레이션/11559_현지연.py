# https://www.acmicpc.net/problem/11559

from collections import deque

def bfs(x, y, color, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    xylist = [(x, y)]
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny]==color:
                queue.append((nx, ny))
                visited[nx][ny] = True
                xylist.append((nx, ny))
                cnt += 1
    return cnt, xylist  # 같은색 뿌요 상하좌우 연결 개수, 좌표 리스트

answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 필드 초기화
graph = [[0] * 6 for _ in range(12)]
for i in range(12):
    line = input()
    for j in range(6):
        graph[i][j] = line[j]

# 연쇄가 끊길때까지 반복
while True:
    visited = [[False] * 6 for _ in range(12)]  # 방문 여부
    check = False                               # 연쇄 여부
    # 뿌요 터뜨리기
    for i in range(11, -1, -1):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                cnt, xylist = bfs(i, j, graph[i][j], visited)
                if 4 <= cnt:    # 4개 이상이면 터뜨리기
                    for k, l in xylist:
                        graph[k][l] = '.'
                    check = True
    if check:
        answer += 1
    else:
        break
    # 뿌요 아래로 떨어뜨리기
    for j in range(6):
        queue = deque() # 빈 공간 큐
        for i in range(11, -1, -1):
            if graph[i][j] == '.':
                queue.append(i)
            else:
                if queue:
                    graph[queue.popleft()][j] = graph[i][j]
                    graph[i][j] = '.'
                    queue.append(i)

print(answer)