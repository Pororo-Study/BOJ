graph = []  # 방
answer = 0  # 청소하는 칸의 개수

n, m = map(int, input().split())
x, y, d = map(int, input().split()) # 로봇 청소기가 있는 칸의 좌표, 방향

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] # 0123방향: 북동남서
dy = [0, 1, 0, -1]

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
    if graph[x][y] == 0:
        graph[x][y] = 2
        answer += 1
    
    check = False   # 주변 4칸 확인용

    # 현재 칸의 주변 4칸 확인
    for _ in range(4):
        # 반시계 방향으로 90도 회전
        if d == 0:
            d = 3
        else:
            d = d - 1

        nx = x + dx[d]  # 바라보는 방향 기준으로 앞쪽 칸
        ny = y + dy[d]

        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        if graph[nx][ny] == 0:
            x = nx
            y = ny
            check = True
            break
    
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if not check:
        nx = x - dx[d]
        ny = y - dy[d]
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진
        if graph[nx][ny] != 1:
            x = nx
            y = ny
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
        else:
            break
        
print(answer)