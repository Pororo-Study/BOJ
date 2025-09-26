# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
import copy

# BFS로 바이러스 퍼뜨리기
def spread_virus(graph):
    q = deque(virus_list)
    cnt = 0 # 바이러스가 추가로 퍼진 칸의 수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0: # 빈칸일때만
                q.append((nx, ny))
                graph[nx][ny] = 2
                cnt += 1
    return cnt

n, m = map(int, input().split()) # 지도의 세로, 가로 크기
dx = [1, 0, -1, 0] # 동서남북 이동방향
dy = [0, 1, 0, -1]
answer = 0 # 안전 영역의 최대 크기
graph = [] # 지도
blank_list = [] # 초기 빈칸들의 좌표 리스트
virus_list = [] # 초기 바이러스들의 좌표 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            blank_list.append((i, j))
        elif graph[i][j] == 2:
            virus_list.append((i, j))

candidates = list(combinations(blank_list, 3)) # 초기 빈칸들의 좌표 리스트에서 3개의 좌표를 뽑아 순서를 고려하지 않고 나열하는 모든 경우

for a, b, c in candidates:
    new_graph = copy.deepcopy(graph) # 지도에 영향을 주지 않기 위해 복사본 만들기
    
    # 벽 3개 세우기
    new_graph[a[0]][a[1]] = 1
    new_graph[b[0]][b[1]] = 1
    new_graph[c[0]][c[1]] = 1

    # 안전 영역 구하기
    safe_cnt = len(blank_list) - spread_virus(new_graph) - 3 # 빈칸의 수 - 새로 퍼진 바이러스 수 - 설치한 벽 수

    if answer < safe_cnt:
        answer = safe_cnt

print(answer)