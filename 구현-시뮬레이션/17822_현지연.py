# 원판 돌리기
# https://www.acmicpc.net/problem/17822
# 시뮬레이션 + BFS

from collections import deque

n, m, t = map(int, input().split())

dx = [0, 1, 0, -1] # 상하좌우 이동
dy = [1, 0, -1, 0]

graph = [] # 원판 위 숫자 행렬

# 원판 위 숫자 입력받아 저장하기
for _ in range(n):
    graph.append(list(map(int, input().split())))

# t번 반복
for _ in range(t): 
    x, d, k = map(int, input().split()) # x의 배수인 원판을 d방향으로 k칸 회전
    
    # 원판 회전
    for i in range(n):
        if (i+1) % x == 0: # 현재 반지름이 i+1인 원판이 x의 배수라면 
            if d == 0: # 시계방향
                temp = graph[i][-k:] + graph[i][:-k] # 슬라이싱으로 이어붙이기
            else: # 반시계방향
                temp = graph[i][k:] + graph[i][:k]
            graph[i] = temp
    
    total = 0 # 원판에 적힌 수의 합
    cnt = 0 # 원판에 적힌 수의 개수

    # 인접하면서 같은 수 모두 지우기
    check = False # 인접하면서 같은 수 존재 여부
    visited = [[False] * m for _ in range(n)] # 방문 여부
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0: # 아직 방문하지 않았고 지워진 수가 아니라면

                # 나중에 평균을 구하기 위해 미리 계산
                total += graph[i][j]
                cnt += 1

                value = graph[i][j] # 비교할 값

                # BFS
                q = deque([(i, j)])
                visited[i][j] = True
                delete_list = [(i, j)] # 지워야 할 수 위치 목록
                while q:
                    now_x, now_y = q.popleft()
                    for dir in range(4):
                        next_x = (now_x + dx[dir]) # 1번 원판과 N번 원판은 비교 불가
                        next_y = (now_y + dy[dir]) % m # 원형으로 비교
                        if 0<= next_x < n and not visited[next_x][next_y] and graph[next_x][next_y] == value:
                            q.append((next_x, next_y))
                            visited[next_x][next_y] = True
                            delete_list.append((next_x, next_y))

                # 인접하면서 같은 수가 2개 이상이라면 지우기
                if len(delete_list) >= 2:
                    check = True
                    for now_x, now_y in delete_list:
                        graph[now_x][now_y] = 0

    # 인접하면서 같은 수를 지웠거나, 원판에 남아있는 수가 없다면 넘어가기
    if check or cnt == 0:
        continue

    # 원판에 적힌 수의 평균을 구하기
    avg = total / cnt
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and graph[i][j] > avg: # 평균보다 큰 수는 1 빼기
                graph[i][j] -= 1
            elif graph[i][j] != 0 and graph[i][j] < avg: # 평균보다 작은 수는 1 더하기
                graph[i][j] += 1

# 원판에 적힌 수의 합 구하기
ans = 0
for i in range(n):
    for j in range(m):
        ans += graph[i][j]
print(ans)