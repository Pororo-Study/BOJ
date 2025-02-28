# 15685 드래곤 커브
# https://www.acmicpc.net/problem/15685

n = int(input())
answer = 0

dx = [0, -1, 0, 1]  # 우상좌하
dy = [1, 0, -1, 0]

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    y, x, d, g = map(int, input().split())  # y:행, x:열 
    
    dragon_direction = [d]  # 방향 리스트

    for j in range(g):  # 세대 수만큼 반복
        for k in range(2**(j)-1, -1, -1):   # len(dragon_d)-1 == 2**(j)-1
            dragon_direction.append((dragon_direction[k] + 1) % 4)
    # print(dragon_direction) # 최종 방향

    graph[x][y] = 1 # 시작점
    # print(f"({x}, {y})", end=" ")

    for d in dragon_direction:
        x += dx[d]
        y += dy[d]
        graph[x][y] = 1
        # print(f"({x}, {y})", end=" ")
    # print()

# 네 꼭짓점이 모두 색칠되어있는 1x1 정사각형의 개수 구하기
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            answer += 1

print(answer)