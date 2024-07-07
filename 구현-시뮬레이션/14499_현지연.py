n, m, x, y, k = map(int, input().split())                   # 지도의 크기, 주사위 좌표, 명령의 개수
graph = [list(map(int, input().split())) for _ in range(n)] # 지도
move_arr = list(map(int, input().split()))                  # 명령 리스트
dx = [0, 0, -1, 1]  # 동서북남 이동방향
dy = [1, -1, 0, 0]
dice = [0] * 6      # 주사위

for move in move_arr:
    nx = x + dx[move - 1]   # 명령대로 지도 이동
    ny = y + dy[move - 1]

    if nx < 0 or n <= nx or ny < 0 or m <= ny:  # 범위를 벗어난 경우 무시
        continue

    if move == 1:   # 동
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif move == 2: # 서
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif move == 3: # 북
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
    else:           # 남
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]

    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[2]
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사
    else:
        dice[2] = graph[nx][ny]
        graph[nx][ny] = 0   # 칸에 쓰여 있는 수는 0이 됨

    x, y = nx, ny   # 좌표 업데이트
    print(dice[0])  # 주사위의 윗 면에 쓰여 있는 수를 출력