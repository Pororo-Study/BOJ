n, m = map(int, input().split())                            # 보드의 크기
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]                   # 방문 여부

dx = [0, 0, -1, 1]  # 4 방향
dy = [1, -1, 0, 0]
answer = 0  # 정답

# 'T' 를 제외한 모든 도형
def dfs(x, y, total, cnt):
    global answer
    # 테트로미노 수들의 합 중에 최댓값 저장
    if cnt == 4:
          answer = max(answer, total)
          return
    # 가능한 4방향 모두 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, total + graph[nx][ny], cnt + 1)
                visited[nx][ny] = False

# 'T' 모양 도형
def t_shape(x, y):
    global answer
    arr = []    # 4방향에 쓰여있는 수 리스트
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            arr.append(graph[nx][ny])
    # 동서남북 중에 최솟값 하나만 빼고 나머지 합하기
    if len(arr) == 4:
        arr.sort()
        answer = max(answer, sum(arr[1:]) + graph[x][y])
    # 이미 'T' 모양 완성이므로 그냥 합하기
    elif len(arr) == 3:
        answer = max(answer, sum(arr) + graph[x][y])
    return

# 모든 좌표를 확인하면서 테트로미노 만들기
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        t_shape(i, j)
        visited[i][j] = False

print(answer)