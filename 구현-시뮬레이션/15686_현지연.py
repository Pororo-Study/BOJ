from itertools import combinations

n, m = map(int, input().split())
graph = []          # 도시의 정보
house = []          # 집의 좌표
chicken = []        # 치킨집의 좌표
answer = int(1e9)   # 도시의 치킨 거리의 최솟값

# 집과 치킨집의 좌표를 저장하기
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 치킨집 m개를 뽑는 모든 경우의 수를 계산하고, 도시의 치킨 거리의 최솟값을 구함
for new_chicken in list(combinations(chicken, m)):  # 치킨집 m개를 뽑기
    chicken_distance = 0                            # 도시의 치킨 거리
    for h in house:
        min_distance = int(1e9)                     # 현재 집 기준 치킨 거리
        for c in new_chicken:
            # 집과 가장 가까운 치킨집 사이의 거리 구하기
            min_distance = min(min_distance, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        chicken_distance += min_distance            # 도시의 치킨 거리는 모든 집의 치킨 거리의 합
    answer = min(answer, chicken_distance)          # 도시의 치킨 거리의 최솟값 저장

print(answer)