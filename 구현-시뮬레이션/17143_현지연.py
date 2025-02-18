# https://www.acmicpc.net/problem/17143

# 상어의 다음 위치 계산
def get_next_loc(i, j, speed, dir):

    if dir == 1 or dir == 2:
        cycle = (r * 2) - 2
        if dir == 1:    # 상
            i = speed + (cycle - i)
        else:           # 하
            i += speed
        
        i %= cycle
        if i >= r:
            return (cycle - i, j, 1)
        return (i, j, 2)

    else:   
        cycle = (c * 2) - 2
        if dir == 4:    # 좌
            j = speed + (cycle - j)
        else:           # 우
            j += speed
        
        j %= cycle
        if j >= c:
            return (i, cycle - j, 4)
        return (i, j, 3)

answer = 0

r, c, m = map(int, input().split()) # 격자판의 행, 열, 상어의 수

graph = [[0] * c for _ in range(r)] # 격자판

# 격자판에 각 상어의 정보 초기화
for _ in range(m):
    x, y, speed, direction, size = map(int, input().split())
    graph[x - 1][y - 1] = (speed, direction, size)  # (속력, 방향, 크기) 저장


for j in range(c):
    for i in range(r):
        # 낚시
        if graph[i][j]:
            answer += graph[i][j][2]
            graph[i][j] = 0
            break   # 땅과 제일 가까운 상어 한마리만 잡음

    # 모든 상어 움직이기
    new_graph = [[0 for _ in range(c)] for _ in range(r)]  # 상어들의 새 위치를 담을 공간
    for i in range(r):
        for j in range(c):
            if graph[i][j]:
                nx, ny, nd = get_next_loc(i, j, graph[i][j][0], graph[i][j][1]) # graph[i][j]에 있는 상어의 새로운 위치, 방향
                # 다른 상어가 이미 있다면 크기가 큰 상어 남기기
                if new_graph[nx][ny]:
                    new_graph[nx][ny] = max(new_graph[nx][ny], (graph[i][j][0], nd, graph[i][j][2]), key=lambda x: x[2])
                else:
                    new_graph[nx][ny] = (graph[i][j][0], nd, graph[i][j][2])
    graph = new_graph   # 격자판 업데이트

print(answer)